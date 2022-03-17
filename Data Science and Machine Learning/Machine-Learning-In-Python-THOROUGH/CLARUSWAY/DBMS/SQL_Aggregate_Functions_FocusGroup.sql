															-- SQL Server Aggregate Functions --


-- An aggregate function performs a calculation on a set of values, and returns a single value.
-- Except for COUNT(*), aggregate functions ignore null values.
-- Aggregate functions are often used with the GROUP BY clause


--SQL Server Aggregate FunctionS

--1. AVG
--2. COUNT
--3. MAX
--4. MIN
--5. SUM
--6. STDEV

--------------------------------------

AVG()

	-- This function returns the average of the values in a group. It ignores null values.

	-- A) Syntax and Basic Examples

	AVG( [ ALL | DISTINCT ] expression)  -- All is default

	-- What are the average list_price?				-- SELECT * FROM production.products

	SELECT AVG(list_price) AS Avg_ListPrice
	FROM production.products;

	--	ALL

	SELECT AVG( ALL list_price) AS Avg_ListPrice_ALL
	FROM production.products

	--	DISTINCT

	SELECT AVG( DISTINCT list_price) AS Avg_ListPrice_DISTINCT
	FROM production.products


	--B) AVG() with GROUP BY example

	-- SELECT * FROM production.products
	-- SELECT * FROM production.categories

	-- What are the average list price by brand names?

	SELECT brand_name,
		   AVG(list_price) AS avg_product_price
    FROM production.products p
		INNER JOIN production.brands c
		ON p.brand_id = c.brand_id
	GROUP BY brand_name
    ORDER BY brand_name;


	--C) AVG() in HAVING clause example

	-- Which categories have average list price bigger than $500?

	SELECT brand_name,
		   AVG(list_price) AS avg_product_price
	FROM production.products p
		INNER JOIN production.brands c
		ON c.brand_id = p.brand_id
	GROUP BY brand_name
	HAVING AVG(list_price) > 500
	ORDER BY avg_product_price;

---------------------------------------

COUNT()

	-- This function returns the number of items found in a group.

	-- A) Syntax and Basic Examples

	COUNT( [ ALL | DISTINCT ] expression | * )
	COUNT(*)

	-- How many products in the products table?					-- SELECT * FROM production.products     

	SELECT COUNT(product_id) AS product_count     
	FROM production.products

		-- Second way
		SELECT COUNT(*) AS product_count     
		FROM production.products

	-- How many products have the model year 2016 and the list price greater than $999.99?

	SELECT COUNT(product_id) AS Total_Number								-- SELECT * FROM production.products
	FROM production.products
	WHERE model_year = 2016 AND 
		  list_price > 999.99

	-- B) COUNT(DISTINCT expression) example

	-- How many different brands are in the table?				--SELECT * FROM production.products

	SELECT COUNT(DISTINCT brand_id) AS Num_of_Brands
	FROM production.products


	--C) COUNT() with GROUP BY clause example

	-- How many products are in the table by categories?

	SELECT category_id,                                          --SELECT * FROM production.products
		   COUNT(product_id) AS product_count
	FROM production.products
	GROUP BY category_id
	ORDER BY product_count DESC

	-- If we want to find the name of the categories we need to make inner join.

	SELECT category_name,										--SELECT * FROM production.categories
		   COUNT(product_id) AS product_count
	FROM production.products p
		INNER JOIN production.categories c 
		ON p.category_id = c.category_id
	GROUP BY category_name
	ORDER BY product_count DESC

	-- D) COUNT() with HAVING clause example

	-- How many brands have more than 20 products?

	SELECT brand_id,
		   COUNT(DISTINCT product_id) AS product_count
	FROM production.products
	GROUP BY brand_id
	HAVING COUNT(*) > 20
	ORDER BY product_count DESC

	-- If we want to find the name of the brand we need to make inner join.

	SELECT brand_name,
		   COUNT(DISTINCT product_id) AS product_count
	FROM production.products p
		INNER JOIN production.brands c 
		ON p.brand_id = c.brand_id
	GROUP BY brand_name
	HAVING COUNT(*) > 20
	ORDER BY product_count DESC

------------------------------------------

MAX()

	-- Returns the maximum value in the expression.

	-- A) Syntax and Basic Examples

	MAX([ ALL | DISTINCT ] expression)  -- All is default

	-- what is the highest list price?										--SELECT * FROM production.products
	
	SELECT MAX(list_price) AS max_list_price
	FROM production.products

	-- What are the other deatails of the product which has the max price list?

	SELECT *
	FROM production.products
	WHERE list_price = (
						 SELECT MAX(list_price)
						 FROM production.products
					   )

	--B) MAX() with GROUP BY clause example

	-- What are the max list price by brand names?

	SELECT brand_id,
           MAX(list_price) AS max_list_price
	FROM production.products
	GROUP BY brand_id
	ORDER BY brand_id

	-- If we want to find the name of the categories we need to make inner join.

	SELECT brand_name,
           MAX(list_price) AS max_list_price
	FROM production.products p
		INNER JOIN production.brands b
        ON p.brand_id = b.brand_id 
	GROUP BY brand_name
	ORDER BY brand_name


	--C) MAX() with HAVING clause example

	-- Which brands's max price list are bigger than $1000?

	SELECT brand_name,
		   MAX(list_price) AS max_list_price
	FROM production.products p
		INNER JOIN production.brands b
        ON p.brand_id = b.brand_id 
	GROUP BY brand_name
	HAVING MAX(list_price) > 1000
	ORDER BY max_list_price DESC

--------------------------------------------------------

MIN

	-- Returns the minimum value in the expression.

	-- A) Syntax and Basic Examples

	MIN([ ALL | DISTINCT ] expression)  -- All is default

	-- What is the highest list price?							-- SELECT * FROM production.products

	SELECT MIN(list_price) AS min_list_price
	FROM production.products

	-- What are the other id, name and list_price of the product which has the min price list?

	SELECT product_id,
		   product_name,
           list_price
	FROM production.products
	WHERE list_price = (
						 SELECT MIN(list_price )
						 FROM production.products
					   )

	--B) MIN() function with GROUP BY clause example

	-- What are the min list price by categories?

	SELECT category_name,
           MIN(list_price) AS min_list_price
	FROM production.products p
		INNER JOIN production.categories c
		ON p.category_id = c.category_id 
	GROUP BY category_name
	ORDER BY category_name

	--C) MIN() with HAVING clause example

	--  Which categories have min list_price are bigger than $500?

	SELECT category_name,
		   MIN(list_price) AS min_list_price
	FROM production.products p
		INNER JOIN production.categories c 
        ON p.category_id = c.category_id 
	GROUP BY category_name
	HAVING MIN(list_price) < 1000
	ORDER BY category_name

------------------------------------------

SUM

	-- Returns the sum of all the values, or only the DISTINCT values, in the expression. SUM can be used with numeric columns only. Null values are ignored.

	-- A) Syntax and Basic Examples

	SUM([ ALL | DISTINCT ] expression)  -- All is default

	-- Total number of products in the all stores.								-- SELECT * FROM production.stocks

	SELECT SUM(quantity) AS total_stocks
	FROM production.stocks


	--B) SQL Server SUM() function with GROUP BY example

	-- How many products are in stocks by store_id?

	SELECT store_id,														 -- SELECT COUNT(DISTINCT store_id) FROM production.stocks
		   SUM(quantity) AS store_stocks
	FROM production.stocks
	GROUP BY store_id

	-- How many products are in stocks by store_name?

	SELECT store_name,
		   SUM(quantity) AS store_stocks
	FROM production.stocks a
		INNER JOIN sales.stores b
        ON a.store_id = b.store_id
	GROUP BY store_name

	--C) SUM() function with HAVING clause example

	-- How many products are in stocks by product_name?
																						-- SELECT * FROM production.products
	SELECT product_name,																-- SELECT * FROM production.stocks
		   SUM(quantity) AS total_stocks
	FROM production.stocks s
		INNER JOIN production.products p
        ON s.product_id = p.product_id
	GROUP BY product_name
	HAVING SUM(quantity) > 100
	ORDER BY total_stocks DESC;

	--D) SQL Server SUM() function with expression example

	-- What are the net values of the orders by order_id?

	SELECT order_id,																	-- SELECT * FROM sales.orders
		   SUM( quantity * list_price * (1 - discount)) AS net_value					-- SELECT * FROM sales.order_items
	FROM sales.order_items
	GROUP BY order_id
	ORDER BY net_value DESC;

------------------------------------------

STDEV

	-- Returns the statistical standard deviation of all values in the specified expression.

	-- A) Syntax and Basic Examples

	STDEV([ ALL | DISTINCT ] expression)  -- All is default

	SELECT STDEV(list_price) AS list_price,
		   STDEV(ALL list_price) AS ALL_list_price,
		   STDEV(DISTINCT list_price) AS DISTINCT_list_price
	FROM production.products   









