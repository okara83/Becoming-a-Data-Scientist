

-- 1. ANALYTIC AGGREGATE FUNCTIONS --

	/*
MIN() - MAX() - AVG() - SUM() - COUNT()
Products tablosunda herbir ürünün yanına sırasıyla şu değerleri yazdırınız:
1. Tüm bisikletler arasında en ucuz bisikletin fiyatı
2. Herbir kategorideki en ucuz bisikletin fiyatı
3. Toplam kaç faklı bisikletin bulunduğu
4. Herbir kategoride toplam kaç farklı bisikletin bulunduğu
	Soru: WF ile bu sorgu içinde herbir kategoride kaç farklı marka olduğunu hesaplayabilir miyiz?
5. Herbir kategorideki herbir markada kaç farklı bisikletin bulunduğu
	*/


SELECT	*,
		MIN(list_price) OVER() mp_all,
		MIN(list_price) OVER(PARTITION BY category_id) mp_cat,
		COUNT(*) OVER() pc_all,
		COUNT(*) OVER(PARTITION BY category_id) pc_cat,
		COUNT(*) OVER(PARTITION BY category_id, brand_id) pct_cat_bra
FROM	production.products
ORDER BY category_id, brand_id, list_price;


-- 2. ANALYTIC NAVIGATION FUNCTIONS --

	/*
LAG() - LEAD()
Orders tablosunda herbir siparişin yanına sırasıyla şu değerleri yazdırınız:
1. Herbir personelin bir önceki satışının sipariş tarihini yazdırınız (LAG fonksiyonunu kullanınız)
2. Herbir personelin bir sonraki satışının sipariş tarihini yazdırınız (LEAD fonksiyonunu kullanınız)
Not: OVER bloğu içinde satırlar arasındaki sıralamayı iyi belirtmek lazım.
	Eğer order_date e göre sıralama yapılmış olsaydı aynı güne ait siparişler arasındaki sıralama kontrolümüzde olmayacaktı.
	Bundan dolayı order_id ye göre sıralama yapılmıştır.
	*/

SELECT	*,
		LAG(order_date, 1) OVER(PARTITION BY staff_id ORDER BY order_id) od_LAG1,
		LEAD(order_date, 1) OVER(PARTITION BY staff_id ORDER BY order_id) od_LEAD1
FROM	sales.orders
ORDER BY staff_id, order_id;



-- SUNUM - Window Frame --

-- Windows frame i anlamak için birkaç örnek:
-- Herbir satırda işlem yapılacak olan frame in büyüklüğünü (satır sayısını) tespit edip window frame in nasıl oluştuğunu aşağıdaki sorgu sonucuna göre konuşalım.
-- 

SELECT	category_id, product_id,
		COUNT(*) OVER() NOTHING,
		COUNT(*) OVER(PARTITION BY category_id) P,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id) P_O,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) P_O_UPCR,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) P_O_CRUF,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) P_O_CRUF,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) P_O_1P1F,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) P_O_2P3F
FROM	production.products
ORDER BY category_id, product_id;


	/*
FIRST_VALUE() - LAST_VALUE()
Products tablosunda herbir ürünün yanına sırasıyla şu değerleri yazdırınız:
1. Tüm bisikletler arasında en ucuz bisikletin adı (FIRST_VALUE fonksiyonunu kullanınız)
2. Herbir kategorideki en ucuz bisikletin adı (FIRST_VALUE fonksiyonunu kullanınız)
3. 1. maddeyi LAST_VALUE fonksiyonu kullanarak yapınız
4. 2. maddeyi LAST_VALUE fonksiyonu kullanarak yapınız
	Not: 2. ve 4. maddenin sonuçlarını karşılaştırınız. Farklılık varsa nedenini bulmaya çalışınız?
	İstediğiniz satır berlirlediğiniz kurala göre FIRST_VALUE da ilk sırada, LAST_VALUE da sonra sırada gelmelidir.
	Eğer veri içinde aynı fiyatlı bisikletler varsa ORDER BY sıralamasına ekstra dikkat etmek lazım.
	OVER bloğunda belirlediğiniz ORDER BY kuralına göre tabloyu başka bir sorguda sorgulayıp istediğiniz satır istediğiniz yerder (FIRST veya LAST) gelmiş mi diye kontrol edebilirsiniz.
Not: OVER bloğu içinde ORDER BY dan sonra Window Frame tanımlarken ROWS ya da RANGE kullanılabilir.
	ROWS BETWEEN ile RANGE BETWEEN arasında çok fark yok.
	RANGE ile sadece UNBOUNDEN PRECEDING, CURRENT ROW veya UNBOUNDED FOLLOWING değerlerini kullanabiliyorsunuz.
	ROWS ile ek olarak n PRECEDING ya da m FOLLOWING değerlerini de kullanabiliyoruz.
	Dolayısıyla RANGE i bilin fakat ROWS kullanmaya alışmanızı tavsiye ederim.
	*/

SELECT	*,
		FIRST_VALUE(product_name) OVER(ORDER BY list_price ASC) cheapest_product,
		FIRST_VALUE(product_name) OVER(PARTITION BY category_id ORDER BY list_price ASC) cheapest_product_category,
		LAST_VALUE(product_name) OVER(ORDER BY list_price DESC, product_id DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) cheapest_product2,
		LAST_VALUE(product_name) OVER(PARTITION BY category_id ORDER BY list_price DESC, product_id DESC RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) cheapest_product_category2
FROM	production.products
ORDER BY category_id, list_price;



-- 3. ANALYTIC NUMBERING FUNCTIONS --

	/*
ROW_NUMBER() - RANK() - DENSE_RANK() - CUME_DIST() - PERCENT_RANK() - NTILE()
Products tablosunda herbir ürünün yanına sırasıyla şu değerleri yazdırınız:
1. Herbir kategori içinde bisikletlerin fiyat sıralamasını yapınız (artan fiyata göre 1'den başlayıp birer birer artacak)
2. Aynı soruyu aynı fiyatlı bisikletler aynı sıra numarasını alacak şekilde yapınız (RANK fonksiyonunu kullanınız)
Not: RANK fonksiyonunda aynı fiyatlı ürünlerin numarası o ürünlerin ROW_NUMBER larından en küçüğü oluyor.
	Aynı fiyatlı ürünlerde RANK fonksiyonu o ürünlerin ROW_NUMBER değerinin en büyüğünü döndürmüyor diye biliyorum.
	Bu ihtiyaç için aşağıda yer alan ikinci sorguyu inceleyebilirsiniz.
	Bu sorguda en sağdaki alan (R2 yani RANK2 diyebilirsiniz) bu ihtiyacı karşılamaktadır.
3. Aynı soruyu aynı fiyatlı bisikletler aynı sıra numarasını alacak şekilde yapınız (DENSE_RANK fonksiyonunu kullanınız)
	Not: 2. ve 3. maddenin sonuçlarını karşılaştırınız. Farklılık varsa nedenini anlamaya çalışınız?
	Farkı daha iyi görebilmek için aynı kategori içinde sıralamaların nasıl değiştiğine dikkat ediniz.
4. Herbir kategori içinde bisikletierin fiyatlarına göre bulundukları yüzdelik dilimleri yazdırınız. (CUME_DIST fonksiyonunu kullanınız)
	Not: Hesaplanan değeri virgülden sonra 2 hane olacak şekilde yazdırınız ve bu değeri yorumlayınız?
5. Bir bisiklet diğer bisikletlerin yüzde kaçından daha pahalıdır? Bu yüzdeyi hesaplayınız. (PERCENT_RANK fonksiyonunu kullanınız)
	Not: Hesaplanan değeri virgülden sonra 2 hane olacak şekilde yazdırınız ve bu değeri yorumlayınız?
	4. ve 5. maddelerde hesaplanan değerleri karşılaştırınız. Formüllerine göz atınız.
Not: CUME_DIST fonksiyonu bir ürünün belirlediğimiz sıraya yüzde kaçlık dilimde olduğunu gösterir (Sınavlardaki yüzdelik dilimler gibi)
	PERCENT_RANK fonksiyou ise bir ürünün belirttiğimiz partition içindeki diğer ürünlerin yüzde kaçından daha pahalı/ucuz olduğunu ifade eder.
6. Herbir kategorideki bisikletleri artan fiyata göre 4 gruba ayırın. Mümkünse her grupta aynı sayıda bisiklet olacak. (NTILE fonksiyonunu kullanınız)
	Not: En düşük fiyatlı bisikletler 1. grupta, diğer bisikletler içinde en düşük fiyatlı bisikletler 2. grupta ... olacak şekilde.
Not: NTILE ile kümeler oluşturulurken aynı fiyatlı ürünler farklı gruplara denk gelebilir.
	NTLIE bu durumu kontrol etmemektedir. Buna herhangi bir çözüm bulamadım. Bulursam paylaşırım.
	*/

SELECT	*,
		ROW_NUMBER() OVER(PARTITION BY category_id ORDER BY list_price) RN,
		RANK() OVER(PARTITION BY category_id ORDER BY list_price) R,
		DENSE_RANK() OVER(PARTITION BY category_id ORDER BY list_price) DR,
		ROUND(CUME_DIST() OVER(PARTITION BY category_id ORDER BY list_price), 02) CD,
		ROUND(PERCENT_RANK() OVER(PARTITION BY category_id ORDER BY list_price), 2) PR,
		NTILE(4) OVER(PARTITION BY category_id ORDER BY list_price) NT
FROM	production.products;


-- RANK2
SELECT	A.*,
		MAX(RN) OVER(PARTITION BY A.category_id, A.R) R2
FROM	(
		SELECT	*,
				ROW_NUMBER() OVER(PARTITION BY category_id ORDER BY list_price) RN,
				RANK() OVER(PARTITION BY category_id ORDER BY list_price) R,
				DENSE_RANK() OVER(PARTITION BY category_id ORDER BY list_price) DR,
				ROUND(CUME_DIST() OVER(PARTITION BY category_id ORDER BY list_price), 02) CD,
				ROUND(PERCENT_RANK() OVER(PARTITION BY category_id ORDER BY list_price), 2) PR,
				NTILE(4) OVER(PARTITION BY category_id ORDER BY list_price) NT
		FROM	production.products
		) A
ORDER BY A.category_id, A.list_price;

