#!/usr/bin/env python3

"""
GraphDB.py
"""

import json
import sqlite3

import networkx as nx


class GraphDB:

    def __init__(self, db_file):
        self.db_file = db_file
        self.initialize()

    def atomic(self, cursor_exec_fn):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = TRUE;")
        results = cursor_exec_fn(cursor)
        connection.commit()
        connection.close()
        return results

    def initialize(self):
        def _init(cursor):
            cursor.executescript(self.SCHEMA)

        return self.atomic(_init)

    def add_node(self, data):
        assert data["id"] is not None, "id is not specified"

        def _add_node(cursor):
            cursor.execute("INSERT INTO nodes VALUES(json(?))", (json.dumps(data),))

        return self.atomic(_add_node)

    def get_node(self, identifier):
        def _find_node(cursor):
            results = cursor.execute("SELECT body FROM nodes WHERE json_extract(body, '$.id') = ?",
                                     (identifier,)).fetchall()
            if len(results) == 1:
                return GraphDB._parse_search_results(results).pop()
            return results

        return self.atomic(_find_node)

    def get_nodes(self, nodes=None, predicate=None, operator="="):
        def _find_node(cursor):
            search = " WHERE 1=1 "
            if predicate:
                search += "AND " + " AND ".join(
                    ["json_extract(nodes.body, '$.{}') {} '{}'".format(k, operator, str(predicate[k])) for k in
                     predicate.keys()])
            if nodes:
                search += " AND nodes.id IN {}".format(GraphDB._get_identifier_string(nodes))
            results = cursor.execute("SELECT * FROM nodes {}".format(search)).fetchall()
            if len(results) >= 0:
                return GraphDB._parse_search_results(results)
            return results

        return self.atomic(_find_node)

    def update(self, data):
        assert data["id"] is not None, "id is not specified"

        def _update(cursor):
            current_data = self.get_node(data["id"])
            updated_data = {**current_data, **data}
            cursor.execute("UPDATE nodes SET body = json(?) WHERE id = ?",
                           (json.dumps(updated_data), data["id"],))

        return self.atomic(_update)

    def add_ege(self, source_id, target_id, properties={}):
        def _connect_nodes(cursor):
            cursor.execute("INSERT INTO edges VALUES(?, ?, json(?))", (source_id, target_id, json.dumps(properties),))

        return self.atomic(_connect_nodes)

    def remove_nodes(self, identifier):
        def _remove_node(cursor):
            tuplestr = GraphDB._get_identifier_string(identifier)
            cursor.execute("DELETE FROM edges WHERE source IN {} OR target IN {}".format(tuplestr, tuplestr))
            cursor.execute("DELETE FROM nodes WHERE id IN {}".format(tuplestr))

        return self.atomic(_remove_node)

    def get_edges(self, source=None, target=None, predicate=None, operator="="):
        def _get_connections(cursor):
            search_source = ""
            search_target = ""
            if source is not None:
                search_source = "source IN {}".format(GraphDB._get_identifier_string(source))
            if target is not None:
                search_target = "target IN {}".format(GraphDB._get_identifier_string(target))

            search = "{}{}{}{}".format("WHERE " if source or target else "", search_source,
                                       " AND " if source and target else "", search_target)

            if predicate is not None:
                search += "AND " + " AND ".join(
                    ["json_extract(properties, '$.{}') {} '{}'".format(k, operator, str(predicate[k])) for k in
                     predicate.keys()])
            return cursor.execute("SELECT * FROM edges {}".format(search)).fetchall()

        return self.atomic(_get_connections)

    def find_outbound_neighbors(self, source, predicate=None, operator="="):
        def _find_outbound_neighbors(cursor):
            search = ""
            if predicate is not None:
                search = "AND " + " AND ".join(
                    ["json_extract(nodes.body, '$.{}') {} '{}'".format(k, operator, str(predicate[k])) for k in
                     predicate.keys()])
            return cursor.execute(
                "SELECT * FROM nodes JOIN edges ON nodes.id=edges.target WHERE edges.source IN {} {}".format(
                    GraphDB._get_identifier_string(source),
                    search)).fetchall()

        return self.atomic(_find_outbound_neighbors)

    def find_inbound_neighbors(self, target, predicate=None, operator="="):
        def _find_inbound_neighbors(cursor):
            search = ""
            if predicate is not None:
                search += " AND ".join(
                    ["json_extract(nodes.body, '$.{}') {} '{}'".format(k, operator, str(predicate[k])) for k in
                     predicate.keys()])
            return cursor.execute(
                "SELECT * FROM edges WHERE target IN {}".format(GraphDB._get_identifier_string(target),
                                                                search)).fetchall()

        return self.atomic(_find_inbound_neighbors)

    def get_target_nodes(self, target):
        def _find_node(cursor):
            results = cursor.execute("SELECT body FROM nodes WHERE json_extract(body, '$.id') IN {}".format(
                GraphDB._get_identifier_string(target, property=1).replace("'", ""))).fetchall()
            if len(results) >= 1:
                return GraphDB._parse_search_results(results)
            return results

        return self.atomic(_find_node)

    def get_source_nodes(self, target):
        def _find_node(cursor):
            results = cursor.execute("SELECT body FROM nodes WHERE json_extract(body, '$.id') IN {}".format(
                GraphDB._get_identifier_string(target, property=0).replace("'", ""))).fetchall()
            if len(results) >= 1:
                return GraphDB._parse_search_results(results)
            return results

        return self.atomic(_find_node)

    def find_neighbors(self, identifier):
        tuplestr = GraphDB._get_identifier_string(identifier)

        def _find_neighbors(cursor):
            return cursor.execute(
                "SELECT * FROM edges WHERE source = {} OR target = {}".format(tuplestr, tuplestr)).fetchall()

        return self.atomic(_find_neighbors)

    def to_networkx(self, nodes=None):

        def _find_nodes(cursor):
            search = ""
            if nodes:
                search += "WHERE id IN {}".format(GraphDB._get_identifier_string(nodes))
            return cursor.execute("SELECT DISTINCT * FROM nodes {}".format(search)).fetchall()

        results = self.atomic(_find_nodes)
        _nodes = GraphDB._parse_search_results(results)
        graph = nx.Graph()
        for node in _nodes:
            print(node)
            graph.add_node(int(node["id"]), properties=node)
        edges_in = self.get_edges(source=_nodes)
        edges_out = self.get_edges(target=_nodes)
        edges = set(edges_in + edges_out)
        for edge in edges:
            graph.add_edge(int(edge[0]), int(edge[1]), properties=edge[2])
        return graph

    @staticmethod
    def _get_property(dictionary, property):

        if isinstance(dictionary, int) or isinstance(dictionary, str):
            return [dictionary]

        if not isinstance(dictionary, list):
            dictionary = [dictionary]

        if isinstance(dictionary, list):
            dictionary = list(map(lambda x: x[property], dictionary))

        return dictionary

    @staticmethod
    def _get_identifier_string(ids, property="id"):
        ids = GraphDB._get_property(ids, property)
        string = str(tuple(ids))
        if len(ids) < 2:
            string = string.replace(",", "")
        return string

    @staticmethod
    def _parse_search_results(results, idx=0):
        return [json.loads(item[idx]) for item in results]

    SCHEMA = """CREATE TABLE IF NOT EXISTS nodes (
        body TEXT,
        id   TEXT GENERATED ALWAYS AS (json_extract(body, '$.id')) VIRTUAL NOT NULL UNIQUE
    );

    CREATE INDEX IF NOT EXISTS id_idx ON nodes(id);

    CREATE TABLE IF NOT EXISTS edges (
        source     TEXT,
        target     TEXT,
        properties TEXT,
        FOREIGN KEY(source) REFERENCES nodes(id),
        FOREIGN KEY(target) REFERENCES nodes(id)
    );

    CREATE INDEX IF NOT EXISTS source_idx ON edges(source);
    CREATE INDEX IF NOT EXISTS target_idx ON edges(target);"""
