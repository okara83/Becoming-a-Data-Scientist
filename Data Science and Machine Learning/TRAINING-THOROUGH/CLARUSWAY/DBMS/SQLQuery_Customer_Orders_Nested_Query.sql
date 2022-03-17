2017 yılında sipariş veren müşterileri listeleyiniz.

SELECT * FROM sales.customers -- 1445

Aşağıda yıllara göre GROUP BY yaptığımızda 2017 yılında 688 sipariş var.
4 Müşteri 2. sipariş verdiği için aslında 2017 yılında 684 müşteri sipariş vermiş.
684 müşteri bilgisi için aşağıda farklı sql queryler yazıldı.

--2016 --> 635 orders, 2017 --> 688 orders, 2018 --> 292 Total --> 1615 orders
SELECT YEAR(order_date), COUNT(*)
FROM sales.orders
GROUP BY YEAR(order_date)

SELECT customer_id FROM sales.orders --2, 4, 19, 47
WHERE YEAR(order_date) = 2017
GROUP BY customer_id
HAVING COUNT(*) > 1

Aşağıdaki EXISTS ile ilgili örneklerden customers ya da orders tablosunun kolonlarından
herhangi bir tanesi ya da NULL ya da 1 olduğunda doğru sonuçlar üretirken, 
count(*), count(1) olduğunda sipariş sayısını değil tüm müşterilerin sayısını getirdi.
Dolayısıyla burada EXISTS ile birlikte count kullanılması doğru değil(miş)!

1-
SELECT distinct c.customer_id, first_name, last_name, city -- 684
FROM sales.customers c INNER JOIN sales.orders o ON c.customer_id = o.customer_id
WHERE YEAR(order_date) = 2017
ORDER BY c.customer_id, first_name, last_name;

2-
SELECT customer_id, first_name, last_name, city -- 684
FROM sales.customers
WHERE customer_id IN ( SELECT customer_id FROM sales.orders WHERE YEAR(order_date) = 2017 )
ORDER BY customer_id, first_name, last_name;

3-
SELECT customer_id, first_name, last_name, city -- 684
FROM sales.customers c
WHERE
 EXISTS (
 SELECT customer_id
 FROM sales.orders o
 WHERE o.customer_id = c.customer_id AND YEAR (order_date) = 2017
 )
ORDER BY c.customer_id, first_name, last_name;

4-
SELECT customer_id, first_name, last_name, city -- 684
FROM sales.customers c
WHERE
 EXISTS (
 SELECT NULL
 FROM sales.orders o
 WHERE o.customer_id = c.customer_id AND YEAR (order_date) = 2017
 )
ORDER BY c.customer_id, first_name, last_name;

5-
SELECT customer_id, first_name, last_name, city -- 684
FROM sales.customers c
WHERE
 EXISTS (
 SELECT 1
 FROM sales.orders o
 WHERE o.customer_id = c.customer_id AND YEAR (order_date) = 2017
 )
ORDER BY c.customer_id, first_name, last_name;

6-
SELECT customer_id, first_name, last_name, city -- 1445
FROM sales.customers c
WHERE
 EXISTS (
 SELECT count(*)
 FROM sales.orders o
 WHERE o.customer_id = c.customer_id AND YEAR (order_date) = 2017
 )
ORDER BY c.customer_id, first_name, last_name;
