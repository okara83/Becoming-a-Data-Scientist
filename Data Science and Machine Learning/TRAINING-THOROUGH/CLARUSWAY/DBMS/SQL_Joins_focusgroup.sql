--JOIN

--TOPICS:

--INNER JOIN
--LEFT JOIN
--RIGHT JOIN
--FULL OUTER JOIN
--SELF JOIN
--CROSS JOIN
---------------------------------------------------------------------------------------------

-- 1) INNER JOIN:


-- 1.1. Write a statement that retrieves the product information from the products table:

SELECT *
FROM
    production.products
ORDER BY
    product_name DESC;


-- 1.2. Add the category names in the result set:

SELECT
    product_name,
    category_name,
	c.category_id,
    list_price
FROM
	production.products p
		INNER JOIN production.categories c ON c.category_id = p.category_id
ORDER BY 
	product_name DESC;


-- 1.3. Add the brand names in the result set:

SELECT
    product_name,
    category_name,
    brand_name,
    list_price
FROM
    production.products p
		INNER JOIN production.categories c ON c.category_id = p.category_id
		INNER JOIN production.brands b ON b.brand_id = p.brand_id
ORDER BY
    product_name DESC;
------------------------------------------------------------------------------


-- 2) LEFT JOIN:

-- 2.1. Write a statement that retrieves all the product information from the products table,
-- and add the "order_id" in the result set: 


SELECT
    product_name,
    order_id
FROM
    production.products p
		LEFT JOIN sales.order_items o ON o.product_id = p.product_id
ORDER BY
    order_id;


-- 2.2. Write a statement that returns the products that do not appear in any sales order:
-- (in other words: it returns the products which have not been sold to any customer yet:)

SELECT
    product_name,
    order_id
FROM
    production.products p
		LEFT JOIN sales.order_items o ON o.product_id = p.product_id
WHERE 
	order_id IS NULL
ORDER BY
    order_id;


--	2.3. Write a statement that retrieves all the product information from the products table,
-- and add the "order_id" and "order_date" in the result set:

SELECT
    p.product_name,
    o.order_id,
    i.item_id,
    o.order_date
FROM
    production.products p
		LEFT JOIN sales.order_items i ON i.product_id = p.product_id
		LEFT JOIN sales.orders o ON o.order_id = i.order_id
ORDER BY
    order_id;


-- 2.4. Write a query that finds the products that belong to the order id 100:

SELECT
    product_name,
    i.order_id,
	item_id,
	o.order_date
FROM
    production.products p
		LEFT JOIN sales.order_items i ON i.product_id = p.product_id
		LEFT JOIN sales.orders o ON o.order_id = i.order_id
WHERE 
	i.order_id = 100
ORDER BY
    o.order_id;
---------------------------------------------------------------------------------------------


-- 3) RIGHT JOIN:

-- 3.1. Write a statement that retrieves all the product information from the products table,
-- and add the "order_id" in the result set:

SELECT
    product_name,
    order_id
FROM
    sales.order_items o
		RIGHT JOIN production.products p ON o.product_id = p.product_id
ORDER BY
    order_id;


-- 3.2. Write a statement that returns the products that do not appear in any sales order:
-- (in other words: it returns the products which have not been sold to any customer yet:)

SELECT
    product_name,
    order_id
FROM
    sales.order_items o
		RIGHT JOIN production.products p ON o.product_id = p.product_id
WHERE
    order_id IS NULL
ORDER BY
    product_name;
---------------------------------------------------------------------------------------------


-- 4) FULL OUTER JOIN:

-- 4.1. Write a statement that retrieves all the product information,
-- and all the item information from the related tables: 

SELECT
    product_name,
    order_id
FROM
    production.products p
		FULL OUTER JOIN sales.order_items o ON o.product_id = p.product_id
ORDER BY
    order_id;
---------------------------------------------------------------------------------------------


-- 5) SELF JOIN: (It is not actually a join, uses the inner join or left join clause)


-- 5.1.(to query hierarchical data) Write a statement that gives who reports to whom from the staff:

SELECT
    e.first_name + ' ' + e.last_name as employee,
    m.first_name + ' ' + m.last_name as manager
FROM
    sales.staffs e
		INNER JOIN sales.staffs m ON m.staff_id = e.manager_id
ORDER BY
    manager;


-- 5.2. Write a statement that gives who reports to whom from the staff including all member:

SELECT
    e.first_name + ' ' + e.last_name as employee,
    m.first_name + ' ' + m.last_name as manager
FROM
    sales.staffs e
		LEFT JOIN sales.staffs m ON m.staff_id = e.manager_id
ORDER BY
    manager;


-- 5.3. (to compare rows within a table) Write a statement in order to 
-- find the customers who locate in the same city.

SELECT
    c1.city,
    c1.first_name + ' ' + c1.last_name as customer_1,
    c2.first_name + ' ' + c2.last_name as customer_2
FROM
    sales.customers c1
		INNER JOIN sales.customers c2 ON c1.customer_id > c2.customer_id
		AND c1.city = c2.city
ORDER BY
    city,
    customer_1,
    customer_2;


-- 5.4. What is the difference between > and <> in the ON clause?

SELECT
    c1.city,
    c1.first_name + ' ' + c1.last_name as customer_1,
    c2.first_name + ' ' + c2.last_name as customer_2
FROM
    sales.customers c1
		INNER JOIN sales.customers c2 ON c1.customer_id <> c2.customer_id
		AND c1.city = c2.city
ORDER BY
    city,
    customer_1,
    customer_2;
---------------------------------------------------------------------------------------------


-- 6) CROSS JOIN: (to join two or more unrelated tables.)

-- 6.1. Find the combinations of all products and stores:
-- Note: The result set can be used for stocktaking procedure
--		 during the month-end and year-end closings

SELECT
    product_id,
    product_name,
    store_id
FROM
    production.products
		CROSS JOIN sales.stores
ORDER BY
    product_name,
    store_id;


-- 6.2. Write a statement that finds the products that have no sales across the stores:

SELECT
    s.store_id,
    p.product_id
    sales,
	ISNULL(sales, 0) as zero_sales 
FROM
    sales.stores s
		CROSS JOIN production.products p
		LEFT JOIN (
			SELECT
				s.store_id,
				p.product_id,
				SUM (quantity * i.list_price) as sales
			FROM
				sales.orders o
					INNER JOIN sales.order_items i ON i.order_id = o.order_id
					INNER JOIN sales.stores s ON s.store_id = o.store_id
					INNER JOIN production.products p ON p.product_id = i.product_id
			GROUP BY
				s.store_id,
				p.product_id
		) c ON c.store_id = s.store_id
		AND c.product_id = p.product_id
WHERE
    sales IS NULL
ORDER BY
    store_id,
	product_id;