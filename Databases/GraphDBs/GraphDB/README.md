# GraphDB

GraphDB is a wrapper providing graph traversal functionality over SQLite3 for Python.
Check out [Recommendation Example](Recommendation.ipynb) for sample usage.

Inspired by [Simple-Graph](https://github.com/dpapathanasiou/simple-graph) but even simpler
## Basic Usage

Create DB

```python
from GraphDB.GraphDB import GraphDB
db = GraphDB("test.sqlite")
```

Add node

```Python
db.add_node({'name': 'p1', 'type': 'person', "id": 1})
db.add_node({'name': 'p2', 'type': 'person', "id": 2})
```

Add edge

```python
db.add_ege(1, 2, {'action': 'likes'})
```

Draw Graph

```python
import networkx as nx
G = db.to_networkx()
nx.draw(G)
```

Get Edges with the property "action = features"

```python
eout = db.get_edges(source=5, predicate={'action': 'features'})
```

Get Nodes

```python
db.get_nodes()
```

Search Nodes

```python
db.get_nodes(predicate={'name': 'p1'})
```
Search in set of nodes

```python
nodes = db.get_nodes(predicate={'type': 'person'})
db.get_nodes(nodes=nodes, predicate={'name': 'p1'})
```
