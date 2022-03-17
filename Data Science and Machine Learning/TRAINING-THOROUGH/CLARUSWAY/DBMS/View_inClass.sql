-- SQL Server Views

SELECT product_name, brand_name, list_price
FROM production.products p
INNER JOIN production.brands b
ON b.brand_id = p.brand_id;


CREATE VIEW sales.product_info
AS
SELECT product_name, brand_name, list_price
FROM production.products p
INNER JOIN production.brands b
ON b.brand_id = p.brand_id;

SELECT * FROM sales.product_info;

SELECT *
FROM (
SELECT product_name, brand_name, list_price
FROM production.products p
INNER JOIN production.brands b
ON b.brand_id = p.brand_id ) product_info2;


CREATE VIEW sales.daily_sales
AS
SELECT order_date AS OrderDate, p.product_id AS ProductCode, quantity AS Quantity, i.list_price AS Price
FROM 
sales.orders as o
INNER JOIN sales.order_items as i
ON o.order_id = i.order_id
INNER JOIN production.products as p
ON p.product_id = i.product_id

SELECT OrderDate, ProductCode, Price
FROM sales.daily_sales
WHERE ProductCode = 20 ORDER BY OrderDate DESC; 

DROP VIEW sales.daily_sales;

EXEC sp_rename 'sales.daily_sales', 'sales'
