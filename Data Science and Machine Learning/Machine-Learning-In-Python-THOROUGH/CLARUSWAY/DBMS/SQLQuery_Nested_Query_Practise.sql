SQL Scripts

=, !=, <, <= , >, >=
IN, NOT IN
BETWEEN, NOT BETWEEN
ANY, ALL

SELECT * FROM sales.customers
SELECT * FROM sales.staffs
SELECT * FROM sales.orders
SELECT * FROM sales.order_items

SELECT * FROM production.products
SELECT * FROM production.brands
SELECT * FROM production.categories

1-

SELECT order_id, order_date, customer_id
FROM sales.orders
WHERE customer_id IN ( SELECT customer_id FROM sales.customers WHERE city = 'New York' )
ORDER BY order_date DESC;

2-

SELECT product_name, list_price
FROM production.products
WHERE list_price > ( SELECT AVG(list_price)
					 FROM production.products
					 WHERE brand_id IN 
					  ( SELECT brand_id
						FROM production.brands
						WHERE brand_name = 'Strider' OR brand_name = 'Trek' )
				   )
ORDER BY list_price;

3-

SELECT order_id, order_date,
 (
 SELECT MAX(list_price) FROM sales.order_items i WHERE i.order_id = o.order_id
 ) AS max_list_price
FROM sales.orders o
ORDER BY order_date DESC;

4-

SELECT product_id, product_name
FROM production.products
WHERE category_id IN (
			SELECT category_id
			FROM production.categories
			WHERE category_name = 'Mountain Bikes' OR category_name = 'Road Bikes' );

5-

SELECT product_name, list_price
FROM production.products
WHERE
 list_price >= ANY (
 SELECT AVG(list_price) FROM production.products GROUP BY brand_id );

6-

SELECT product_name, list_price
FROM production.products
WHERE
 list_price >= ALL (
 SELECT AVG(list_price) FROM production.products GROUP BY brand_id );

7-

SELECT customer_id, first_name, last_name, city
FROM sales.customers c
WHERE
 EXISTS (
 SELECT customer_id
 FROM sales.orders o
 WHERE o.customer_id = c.customer_id AND YEAR (order_date) = 2017
 )
ORDER BY first_name, last_name;

8-

SELECT AVG(order_count) average_order_count_by_staff
FROM
	(SELECT staff_id, COUNT(order_id) order_count
	 FROM sales.orders GROUP BY staff_id) t;

9-

SELECT product_name, list_price, category_id
FROM production.products p1
WHERE
 list_price IN (
 SELECT MAX (p2.list_price)
 FROM production.products p2
 WHERE p2.category_id = p1.category_id
 GROUP BY p2.category_id
 )
ORDER BY category_id, product_name;

10-

SELECT customer_id, first_name, last_name
FROM sales.customers
WHERE
 EXISTS (SELECT NULL)
ORDER BY first_name, last_name;

11-

SELECT customer_id, first_name, last_name
FROM sales.customers c
WHERE
 EXISTS (
 SELECT COUNT (*)
 FROM sales.orders o
 WHERE o.customer_id = c.customer_id
 GROUP BY o.customer_id
 HAVING COUNT (*) > 2
 )
ORDER BY first_name, last_name;

12-

WITH cte_sales_amounts (staff, sales, year) AS (
 SELECT first_name + ' ' + last_name, SUM(quantity * list_price * (1 - discount)),
YEAR(order_date)
 FROM sales.orders o
 INNER JOIN sales.order_items i ON i.order_id = o.order_id
 INNER JOIN sales.staffs s ON s.staff_id = o.staff_id
 GROUP BY first_name + ' ' + last_name, year(order_date)
)
SELECT staff, sales
FROM cte_sales_amounts
WHERE year = 2018;

13-

WITH cte_sales AS (
 SELECT staff_id, COUNT(*) order_count
 FROM sales.orders
 WHERE YEAR(order_date) = 2018
 GROUP BY staff_id
)
SELECT AVG(order_count) average_orders_by_staff
FROM cte_sales;

14-

SELECT *
FROM
(
	SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS row_number  
    FROM sales.orders
) t
WHERE row_number = 1

15-

WITH orders_with_row_numbers AS
(
	SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS row_number  
    FROM sales.orders
)
SELECT *
FROM orders_with_row_numbers
WHERE row_number = 1
