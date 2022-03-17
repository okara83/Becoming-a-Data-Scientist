-- DATE FUNCTIONS:

-- TOPICS:

-- DATENAME()
-- DATEPART()
-- DAY()
-- MONTH()
-- YEAR()
-- GETDATE()
-- ISDATE()
-- DATEDIFF()
-- DATEADD()
-- EOMONTH()


-- 1) DATENAME() and DATEPART() functions:

-- DATENAME(date_part,input_date)
-- Returns a date part of a date as a character string
-- DATEPART(date_part,input_date)
-- Returns a date part of a date as an integer number


SELECT
    DATEPART(year, '2018-05-10') [datepart], 
    DATENAME(year, '2018-05-10') [datename];


SELECT
    DATEPART(year, '2018-05-10') + '1' [datepart], 
    DATENAME(year, '2018-05-10') + '1' [datename];


DECLARE @d DATETIME = '2019-01-01 14:30:14';  -- degisken tanimliyoruz 
SELECT 
   DATEPART(year, @d) as 'year', -- alias yazim türleri degisebilir
   DATEPART(quarter, @d) quarter, 
   DATEPART(month, @d) month, 
   DATEPART(day, @d) day, 
   DATEPART(hour, @d) hour, 
   DATEPART(minute, @d) minute, 
   DATEPART(second, @d) second;


DECLARE @dt DATETIME2 = '2020-11-04T00:08:57.5618443+01:00'-- Messages dan alindi
SELECT 
   DATEPART(year, @dt) as 'year',
   DATEPART(quarter, @dt) quarter, 
   DATEPART(month, @dt) month, 
   DATEPART(day, @dt) day, 
   DATEPART(hour, @dt) hour, 
   DATEPART(minute, @dt) minute, 
   DATEPART(second, @dt) second,
   DATEPART(millisecond, @dt) millisecond,
   DATEPART(microsecond, @dt) microsecond,
   DATEPART(nanosecond, @dt) nanosecond;


-- Write a statement from the Bikestores that retrieves the gross sales by year,
-- quarter, month and day.

SELECT DATEPART(year, shipped_date) [year], 
       DATEPART(quarter, shipped_date) [quarter], 
       DATEPART(month, shipped_date) [month], 
       DATEPART(day, shipped_date) [day] 
       --SUM(quantity * list_price) gross_sales
FROM sales.orders o
     INNER JOIN sales.order_items i ON i.order_id = o.order_id
WHERE shipped_date IS NOT NULL
GROUP BY DATEPART(year, shipped_date), 
         DATEPART(quarter, shipped_date), 
         DATEPART(month, shipped_date), 
         DATEPART(day, shipped_date)
ORDER BY [year] DESC;


--2) DAY(), MONTH(), YEAR() functions:

-- DAY(input_date) : Returns the day of a specified date as an integer
-- MONTH(input_date) : Returns the month of a specified date as an integer
-- YEAR(input_date) : Returns the year of the date as an integer.

SELECT
    DAY('2018-05-10') [day], 
    MONTH('2018-05-10') [month],
	YEAR('2018-05-10') [year];


-- Write a statement from the Bikestores that retrieves the gross sales by month in 2017

SELECT MONTH(shipped_date) [month], 
	   SUM(list_price * quantity) gross_sales
FROM sales.orders o
    INNER JOIN sales.order_items i ON i.order_id = o.order_id
WHERE shipped_date IS NOT NULL
	  AND YEAR(shipped_date) = 2017
GROUP BY MONTH(shipped_date)
ORDER BY [month];


-- Write a statement from the Bikestores that retrieves the gross sales by day in February 2017

SELECT
    DAY(shipped_date) [day], 
    SUM(list_price * quantity) gross_sales
FROM
    sales.orders o
    INNER JOIN sales.order_items i ON i.order_id = o.order_id
WHERE
    shipped_date IS NOT NULL
    AND YEAR(shipped_date) = 2017
    AND MONTH(shipped_date) = 2
GROUP BY
    DAY(shipped_date)
ORDER BY [day];


-- 3) GETDATE():

-- Returns the current system date and time of the operating system
-- on which the SQL Server is running.

SELECT 
    GETDATE() current_date_time;  --taking the current time


SELECT 
    CONVERT(DATE, GETDATE()) [Current Date]; --taking only date


SELECT 
    CONVERT(TIME, GETDATE()) [Current Date]; --taking only time


--4) ISDATE():

-- Checks if a value is a valid DATE, TIME or DATETIME.
-- ISDATE(expression)

SELECT 
    ISDATE('2020-06-15') is_date  -- TRUE


SELECT 
    ISDATE('2020-15-06') is_date  -- FALSE


SELECT 
    ISDATE('2020-12-05 11:20:30') is_date --TRUE


-- 5) DATEDIFF():

-- Returns a difference in date part between two dates.
-- DATEDIFF(date_part , start_date , end_date)

-- Compare the difference between two dates in various date parts:

DECLARE 
    @start_dt DATETIME2 = '2019-12-31 23:59:59.9999999', 
    @end_dt DATETIME2 = '2020-01-01 00:00:00.0000000';

SELECT 
    DATEDIFF(year, @start_dt, @end_dt) diff_in_year, 
    DATEDIFF(quarter, @start_dt, @end_dt) diff_in_quarter, 
    DATEDIFF(month, @start_dt, @end_dt) diff_in_month, 
    DATEDIFF(dayofyear, @start_dt, @end_dt) diff_in_dayofyear, 
    DATEDIFF(day, @start_dt, @end_dt) diff_in_day, 
    DATEDIFF(week, @start_dt, @end_dt) diff_in_week, 
    DATEDIFF(hour, @start_dt, @end_dt) diff_in_hour, 
    DATEDIFF(minute, @start_dt, @end_dt) diff_in_minute, 
    DATEDIFF(second, @start_dt, @end_dt) diff_in_second, 
    DATEDIFF(millisecond, @start_dt, @end_dt) diff_in_millisecond;


-- Write a query in order to compare the requested delivery date with the ship date
-- in days and return if the order is ON-TIME, EARLY or LATE:

SELECT *
FROM 
    sales.orders


SELECT
    order_id, 
    required_date, 
    shipped_date,
    CASE
        WHEN DATEDIFF(day, required_date, shipped_date) > 0 THEN 'Late'
		WHEN DATEDIFF(day, required_date, shipped_date) < 0 THEN 'Early'
        ELSE 'OnTime'
    END shipment
FROM 
    sales.orders
WHERE 
    shipped_date IS NOT NULL
ORDER BY 
    required_date;


-- 6) DATEADD():

-- Adds a value to a date part of a date and return the new date value.
-- DATEADD (date_part , value , input_date )


-- Add 1 second to 2018-12-31 23:59:59:

SELECT 
    DATEADD(second, 1, '2018-12-31 23:59:59') result;


-- Adding 1 day to 2018-12-31 00:00:00:

SELECT 
    DATEADD(day, 1, '2018-12-31 23:59:59') result;


-- Handling month examples

SELECT 
    DATEADD(month, 4, '2019-05-31') AS result;
SELECT 
    DATEADD(month, 4, '2019-05-30') AS result;


-- Write a query in order to calculate the estimated shipped date based on the ordered date

SELECT *
FROM 
    sales.orders


SELECT 
    order_id, 
    customer_id, 
    order_date,
	shipped_date,
    DATEADD(day, 2, order_date) estimated_shipped_date
FROM 
    sales.orders
WHERE 
    shipped_date IS NULL
ORDER BY 
    estimated_shipped_date DESC;


-- 7) EOMONTH()

-- Returns the last day of the month containing the specified date,
-- with an optional offset.

-- If the addition of offset and start_date results in an invalid date,
-- the EOMONTH() function will raise an error.

-- EOMONTH(start_date [, offset]);

SELECT 
    EOMONTH('2019-02-15') end_of_month_feb2019;

SELECT
    EOMONTH('2020-02-09') end_of_month_feb2020;  -- a date of a leap year

SELECT 
    DAY(EOMONTH('2020-02-09')) days; -- returns the number of days in related Month

SELECT 
    DAY(EOMONTH(GETDATE())); -- to get the number of days in the current month,


-- Offset example; (integer and number of months)

SELECT 
    EOMONTH('2019-02-15', 2) eomonth_next_2_months;

