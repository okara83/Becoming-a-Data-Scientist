
--SQL Server Aggregate Functions

--COUNT example

SELECT COUNT(*)
--SELECT *
FROM production.products WHERE list_price > 500;

CREATE TABLE tab(
val INT
);

INSERT INTO tab(val)
VALUES(1),(2),(2),(3),(null),(null),(4),(5)

SELECT * FROM tab

SELECT COUNT(*) FROM tab -- 8

SELECT COUNT(DISTINCT VAL) FROM tab --  5

SELECT COUNT(VAL) FROM tab -- 6

SELECT category_name, COUNT(*) product_count
FROM
production.products p
INNER JOIN production.categories c
ON p.category_id = c.category_id
GROUP BY category_name

SELECT category_name, COUNT(*) product_count
FROM
production.products p
INNER JOIN production.categories c
ON p.category_id = c.category_id
GROUP BY category_name
HAVING COUNT(*) > 30
ORDER BY product_count DESC;


SELECT brand_name, COUNT(*) product_count
--SELECT *
FROM production.products p
INNER JOIN production.brands b
ON p.brand_id = b.brand_id
--WHERE b.brand_name = 'Electra'
GROUP BY brand_name
HAVING COUNT(*) > 20
ORDER BY product_count ASC;

--MAX example

SELECT MAX(list_price) max_list_price
FROM production.products;

SELECT *
FROM production.products
WHERE list_price =  11999.99

SELECT *
FROM production.products
WHERE list_price = (SELECT MAX(list_price) max_list_price
FROM production.products);

SELECT brand_name, MAX(list_price)
FROM production.products p
INNER JOIN production.brands b
ON p.brand_id = b.brand_id
GROUP BY brand_name

SELECT brand_name, MAX(list_price)
FROM production.products p
INNER JOIN production.brands b
ON p.brand_id = b.brand_id
GROUP BY brand_name
HAVING MAX(list_price) > 1000

SELECT MIN(list_price) FROM production.products p;

SELECT * FROM production.products p
WHERE p.list_price = (SELECT MIN(list_price) FROM production.products p);

SELECT category_name, MIN(list_price) FROM
production.products p
INNER JOIN production.categories c
ON p.category_id = c.category_id
GROUP BY category_name

--SUM example

SELECT * FROM production.products -- 321 ??

SELECT SUM(quantity) FROM production.stocks -- 13511
SELECT SUM(quantity) FROM sales.inventory -- 13466

SELECT product_id, SUM(quantity) stock_count
FROM production.stocks
GROUP BY product_id

SELECT store_id, SUM(quantity) stock_count
FROM production.stocks
GROUP BY store_id

SELECT * FROM production.stocks;
SELECT * FROM sales.stores;

SELECT order_id, SUM(quantity*list_price*(1-discount))
FROM sales.order_items
GROUP BY order_id;

SELECT * FROM sales.order_items;


100 %20 --> 80
100*(1-0.20) --> 80

--AVG Example

SELECT AVG(list_price) FROM production.products;

SELECT CAST(ROUND(AVG(list_price),2) AS DEC(10,2)) FROM production.products;

--decimal(20,2)

-- STDEV example

SELECT * FROM production.products;

SELECT MIN(list_price), MAX(list_price), STDEV(list_price)
FROM production.products;










































































