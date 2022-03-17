
﻿

------ SELECT ------

-- Mağazaları listeleyin
SELECT	*
FROM	sales.stores;

-- Mağazaların isimlerini listeleyin
SELECT	store_name
FROM	sales.stores;


------ ORDER BY ------
-- Çalışanları isimlerine göre A'dan Z'ye sıralayın
SELECT	*
FROM	sales.staffs
ORDER BY first_name;

-- Aynı mağazada çalışanlar alt alta gelecek şekilde çalışanları isimlerine göre Z'dan A'ya sıralayın
SELECT	*
FROM	sales.staffs
ORDER BY store_id ASC, first_name DESC;

-- Çalışanları manager_id sine göre küçükten büyüğe doğru sıralayın. NULL olan değerin nerede olduğuna dikkat edin.
SELECT	*
FROM	sales.staffs
ORDER BY manager_id ASC;

-- Çalışanları manager_id sine göre büyükten küçüğe doğru sıralayın. NULL olan değerin nerede olduğuna dikkat edin.
SELECT	*
FROM	sales.staffs
ORDER BY manager_id DESC;



------ DISTINCT ------
-- Hangi eyaletlerden müşteri olduğunu listeleyin. Sadece eyalet bilgileri isteniyor.
SELECT	DISTINCT state
FROM	sales.customers;

-- Hangi şehirlerden müşteri olduğunu listeyelin. Sadece eyalet ve şehir bilgisi isteniyor.
SELECT	DISTINCT state, city
FROM	sales.customers;


------ TOP -----
-- Liste fiyatına göre en pahalı ürünü listeleyin
SELECT	TOP 1 *
FROM	production.products
ORDER BY list_price DESC;

-- Liste fiyatına göre en ucuz ilk 5 ürünü listeleyin
SELECT	TOP 5 *
FROM	production.products
ORDER BY list_price ASC;


------ OFFSET / FETCH -----
-- Liste fiyatına göre en pahalı ürün hariç diğer tüm ürünleri listeleyin
SELECT	*
FROM	production.products
ORDER BY list_price DESC
OFFSET	1 ROWS;

-- Liste fiyatına göre en pahalı 2. ürünü listeleyin
SELECT	*
FROM	production.products
ORDER BY list_price DESC
OFFSET	1 ROWS
FETCH NEXT 1 ROWS ONLY;


------ WHERE -----
-- 2 nolu mağazada çalışan personelleri listeleyin
SELECT	*
FROM	sales.staffs
WHERE	store_id = 2;

-- Adı Venita olan çalışan(lar)ın adı, soyadı ve telefon numaralarını listeleyin
SELECT	first_name, last_name, phone
FROM	sales.staffs
WHERE	first_name = 'Venita';

-- 2017 yılından sonraki tüm siparişleri sipariş tarihi yeniden eskiye doğru listeleyin
-- Aynı soruyu farklı COMPARISION OPERATOR kullanarak çözmeye çalışın
-- Coparision Operators: =, <>, >, >=, <, <=
SELECT	*
FROM	sales.orders
WHERE	order_date > '2017-12-31'
ORDER BY order_date DESC;

-- Sipariş tarihi ile temin tarihi aynı olan siparişleri listeleyin
SELECT	*
FROM	sales.orders
WHERE	order_date = required_date;

-- Sipariş verildiği yıldan bir sonraki yılda kargoya verilen siparişleri listeleyin
-- Örneğin 2016 yılında verilen bir sipariş 2017 yılında kargoya verilmiş gibi
SELECT	*
FROM	sales.orders
WHERE	DATEPART(yyyy, order_date) = DATEPART(yyyy, shipped_date) - 1;


------ LOGICAL OPERATORS -----
-- AND -- 3 numaralı mağazadan 2018 yılı Nisan ayında verilmiş siparişleri listeleyin
SELECT	*
FROM	sales.orders
WHERE	YEAR(order_date) = 2018
		AND MONTH(order_date) = 4
		AND store_id = 3;

-- OR -- 1, 11 ve 111 id numaralı müşterilerin siparişlerini customer_id ye göre küçükten büyüğe doğru listeleyin
SELECT	*
FROM	sales.orders
WHERE	customer_id = 1
		OR customer_id = 11
		OR customer_id = 111
ORDER BY customer_id;

-- BETWEEN -- 20.01.2018 ile 25.01.2018 tarihleri arasındaki siparişleri listeleyin
SELECT	*
FROM	sales.orders
WHERE	order_date BETWEEN '2018-01-20' AND '2018-01-25'
ORDER BY order_date;

-- IN -- Los Angeles, San Diego ve Yuba City şehirlerinde ikamet eden müşterileri listeleyin
SELECT	*
FROM	sales.customers
WHERE	city IN ('Los Angeles', 'San Diego', 'Yuba City')
ORDER BY city;

-- LIKE -- mail adresi hotmail olup Oakland ya da Santa Clara şehirlerinden birinde ikamet eden müşterileri listeleyin
SELECT	*
FROM	sales.customers
WHERE	email LIKE '%@hotmail.%'
		AND city IN ('Oakland', 'Santa Clara');

-- EXISTS -- Id numarası 3 olan mağazanın stoğunda olmayan ürünleri listeleyin (stok sayısı = 0)
-- Bu sorgu IN ve EXISTS operatörleri ile ayrı ayrı yazılmıştır
SELECT	*
FROM	production.products
WHERE	product_id IN	(
						SELECT	product_id
						FROM	production.stocks
						WHERE	store_id = 3
								AND quantity = 0
						);

SELECT	*
FROM	production.products A
WHERE	EXISTS	(
				SELECT	*
				FROM	production.stocks B
				WHERE	B.quantity = 0
						AND B.store_id = 3
						AND A.product_id = B.product_id
				);

-- NULL -- Herhangi bir manager a bağlı olmayan çalışanları listeleyin
-- Aynı sorguyu NULL operatörü kullanmadan yazabilir miyiz?
SELECT	*
FROM	sales.staffs
WHERE	manager_id IS NULL;

SELECT	*
FROM	sales.staffs
WHERE	manager_id < 1; -- Bu sorguda hiç kayıt gelmiyor neden?

-- NOT -- Email adresi gmail olmayan ve aynı zamanda telefon numarası alanı da dolu olan müşterileri listeleyin
SELECT	*
FROM	sales.customers
WHERE	email NOT LIKE '%@gmail.%'
		AND phone IS NOT NULL;

-- Hiç sipariş verilmeyen bisikletleri liste fiyatı büyükten küçüğe doğru sıralayın (NOT EXISTS)
SELECT	*
FROM	production.products A
WHERE	NOT EXISTS	(
					SELECT	1
					FROM	sales.order_items B
					WHERE	A.product_id = B.product_id
					)
ORDER BY A.list_price DESC;


------ ALIAS ------
-- COLUMN & TABLE aliasa örnek olacak bir sorgu yazın (EXISTS örneğindeki sorguyu kullanabilirsiniz)
SELECT	A.product_name AS 'Bisikletin Adı', A.model_year AS Model_Yılı, A.list_price 'Fiyatı ($)'
FROM	production.products A
WHERE	EXISTS	(
				SELECT	*
				FROM	production.stocks AS B
				WHERE	B.quantity = 0
						AND B.store_id = 3
						AND A.product_id = B.product_id
				);



------ SUBQUERY -----
-- Model yılı 2018 olan ve 2017 model yılındaki tüm bisikletlerden pahalı olan bisikletleri listeleyin
SELECT	*
FROM	production.products
WHERE	model_year = 2018
		AND list_price > ALL	(
								SELECT	list_price
								FROM	production.products
								WHERE	model_year = 2017
								);

-- FROM bloğunda subquery kullanarak bir sorgu yazın
SELECT	A.*
FROM	(
		SELECT	store_name AS magaza, phone AS telefon
		FROM	sales.stores
		) A
WHERE	A.magaza = 'Baldwin Bikes';

-- NOT: Subquery için EXISTS bölümündeki sorguları da inceleyebilirsiniz


------ UNION / UNION ALL -----
-- Fairport şehrindeki müşteriler ile East Meadow şehrindeki müşterilerin soyisimlerini listeleyin
SELECT	last_name
FROM	sales.customers
WHERE	city = 'Fairport'
UNION ALL
SELECT	last_name
FROM	sales.customers
WHERE	city = 'East Meadow';

SELECT	last_name
FROM	sales.customers
WHERE	city = 'Fairport'
UNION
SELECT	last_name
FROM	sales.customers
WHERE	city = 'East Meadow';

-- Aşağıdaki sorguları inceleyin ve tartışın
SELECT	store_name
FROM	sales.stores
UNION
SELECT	state
FROM	sales.customers;

SELECT	store_name, state
FROM	sales.stores
UNION ALL
SELECT	store_name
FROM	sales.stores;

SELECT	*
FROM	production.brands
UNION
SELECT	*
FROM	production.categories;


------ CASE -----
-- Simple Case Expression
-- Sipariş günü kargoya verilen siparişler 'hızlı',
-- ertesi gün kargoya verilenler 'normal'
-- siparişten 2 gün sonra kargoya verilenler 'yavaş' ve
-- siparişten 3 gün sonra kargoya verilenler 'çok yavaş' olacak şekilde yeni bir attribute oluşturun.
SELECT	*,	CASE DATEDIFF(DAY, order_date, shipped_date)
				WHEN 0 THEN 'hızlı'
				WHEN 1 THEN 'normal'
				WHEN 2 THEN 'yavaş'
				WHEN 3 THEN 'çok yavaş'
			END AS shipping_speed
FROM	sales.orders
ORDER BY shipped_date DESC;

-- Search Case Expression
-- Yukarıdaki sorguda herbir durumu ayrı ayrı fonksiyonlarda tanımlayın
SELECT	*,	CASE
				WHEN DATEDIFF(DAY, order_date, shipped_date) = 0 THEN 'hızlı'
				WHEN DATEDIFF(DAY, order_date, shipped_date) = 1 THEN 'normal'
				WHEN DATEDIFF(DAY, order_date, shipped_date) = 2 THEN 'yavaş'
				WHEN DATEDIFF(DAY, order_date, shipped_date) = 3 THEN 'çok yavaş'
			END AS shipping_speed
FROM	sales.orders
ORDER BY shipped_date DESC;

-- Müşterilerin email servis sağlayıcılarını yeni bir alanda CASE ile yazdırın
SELECT	*, CASE
				WHEN email LIKE '%@gmail.%' THEN 'GMAIL'
				WHEN email LIKE '%@hotmail.%' THEN 'HOTMAIL'
				WHEN email LIKE '%@yahoo.%' THEN 'YAHOO'
				WHEN email IS NOT NULL THEN 'DİĞER'
			ELSE NULL END email_servis
FROM	sales.customers;


------ CALCULATION -----
-- Siparişlerde herbir item için farklı indirim oranları uygulanmıştır.
-- Herbir item için toplam tutarı (adet sayısı ve discount raito kullanılacak) hesaplayınız
SELECT	*, (list_price * (1 - discount) * quantity) AS tutar
FROM	sales.order_items;


------ CAST / CONVERT -----
-- CALCULATION kısmında hesapladığınız tutar değişkenini tam sayı olacak şekilde listeleyelim
SELECT	*, (list_price * (1 - discount) * quantity) AS tutar,
		CAST((list_price * (1 - discount) * quantity) AS INT) tutar_INT,
		CAST((list_price * (1 - discount) * quantity) AS NUMERIC) tutar_NUMERIC
FROM	sales.order_items;

-- Aynı sorguyu CONVERT ile yazınız
SELECT	*, (list_price * (1 - discount) * quantity) AS tutar,
		CONVERT(INT, (list_price * (1 - discount) * quantity)) tutar_INT,
		CONVERT(NUMERIC, (list_price * (1 - discount) * quantity)) tutar_NUMERIC
FROM	sales.order_items;


------ CONCAT -----
-- Müşterinin adres bilgilerini birleştirip tek bir sütunda listeleyin
SELECT	*, CONCAT(street, ' ', city, ' ', state, ' ', zip_code) adres
FROM	sales.customers;

-- Müşterilerin email ve telefon numarası bilgilerini birleştirip bir sütunda listeleyin
SELECT	*, CONCAT('e-mail: ', email, ' telefon: ', phone) iletisim
FROM	sales.customers;

-- Email ya da telefon numarası boş ise yeni sütunda yer almasını istemiyoruz. Bunu nasıl bir kontrol ederiz?
-- email boş ise sadece telefonu, telefon boş ise sadece telefonu ve hiçbiri boş değilse her ikisini CONCAT yaparız.
SELECT	*, CASE
				WHEN phone IS NULL AND email IS NOT NULL THEN CONCAT('e-mail: ', email)
				WHEN phone IS NOT NULL AND email IS NULL THEN CONCAT('telefon: ', phone)
				WHEN phone IS NOT NULL AND email IS NOT NULL THEN CONCAT('e-mail: ', email, ' telefon: ', phone)
			END iletisim
FROM	sales.customers;


------ COALESCE / ISNULL -----
-- Kargo tarihi boş olan siparişlerin sipariş tarihinden 5 gün sonra kargoya verildiği biliniyor.
-- Fakat teknik bir hatadan dolayi sipariş tarihi değerleri tabloya girilmemiş.
-- Sipariş tarihlerinin son halini yeni bir alanda SELECT bloğunda oluşturunuz
SELECT	*, COALESCE(shipped_date, DATEADD(d, 5, order_date)) AS shipped_date2
FROM	sales.orders;

-- Yukarıdaki sorguyu ISNULL ile yazınız
SELECT	*, ISNULL(shipped_date, DATEADD(d, 5, order_date)) AS shipped_date2
FROM	sales.orders;

-- Aşağıdaki örnekleri inceleyebilirsiniz
SELECT	COALESCE(NULL, NULL, 1, 2, 3, NULL) ornek;
SELECT	ISNULL(NULL, 2) ornek2;


------ ISNUMERIC -----
-- Müşterilerin telefon numaralarının ve Posta kodu bilgilerinin numerik olup olmadığını inceleyin
SELECT	TOP 10 *,
		ISNUMERIC(phone) phone_NUMERIC,
		ISNUMERIC(zip_code) zip_code_NUMERIC
FROM	sales.customers;


------ NULLIF -----
-- İki değer birbirine eşit ise NULL, eşit değilse ilk değeri yazdırır
-- Aşağıdaki sorgu sonucu üzerinden sözlü olarak anlatılacaktır
SELECT	*, NULLIF(order_date, required_date) result_NULLIF
FROM	sales.orders;
SQL Basics - Focus Group - v2.sql
Displaying SQL Basics - Focus Group - v2.sql.