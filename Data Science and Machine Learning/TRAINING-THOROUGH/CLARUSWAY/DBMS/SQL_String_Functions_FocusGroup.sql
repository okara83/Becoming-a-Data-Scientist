							--SQL SERVER STRING FUNCTIONS--

-- String functions perform an operation on a string input value and return a string or numeric value.

-- 1. LEN()
-- 2. CHARINDEX()
-- 3. PATINDEX()
-- 4. LEFT()
-- 5. RIGHT()
-- 6. SUBSTRING()
-- 7. LOWER()
-- 8. UPPER()
-- 9. STRING_SPLIT()
-- 10. TRIM()
-- 11. LTRIM()
-- 12. RTRIM()
-- 13. REPLACE()
-- 14. STR()
-- 15. EXTRA EXAMPLES

------------------------------------------------------------------------------

LEN

	--	Returns the number of characters of the specified string expression, excluding trailing spaces.

	LEN ( string_expression )

	--A) Using LEN() function with a literal string

	SELECT LEN('SQL Server LEN') AS length,
		   LEN('SQL Server LEN   ') AS EXCLUDE_trailing_blanks,			
		   LEN('   SQL Server LEN    ') AS INCLUDE_leading_blanks,
		   -- EXTRA
		   DATALENGTH('   SQL Server LEN   ') AS  INCLUDE_both_blanks

	--B) Using LEN() function with a column

	-- Find the length of the products name.

	SELECT product_name, LEN(product_name) AS product_name_length
	FROM production.products
	
--	FOR YOUR INTEREST --> with ties

	SELECT TOP 5 product_name, LEN(product_name) AS product_name_length
	FROM production.products
	ORDER BY LEN(product_name) DESC

-------------------------------------------------------------------------------------------------------------

CHARINDEX

	-- This function searches for one character expression inside a second character expression, returning the starting position of the first expression if found.

	--A) Syntax and basic examples

	CHARINDEX ( expressionToFind , expressionToSearch [ , start_location ] )

	--WITHOUT START_LOCATION

	SELECT CHARINDEX('Server', 'SQL Server CHARINDEX') AS Position

	--WITH START_LOCATION

	SELECT CHARINDEX('Server', 'SQL Server CHARINDEX', 3) AS Position_#3
	SELECT CHARINDEX('Server', 'SQL Server CHARINDEX', 6) AS Position_#6

	--NULL Values

	SELECT CHARINDEX(NULL, 'SQL Server CHARINDEX') AS Position_#1
	SELECT CHARINDEX('Server', NULL) AS Position_#2

	--Returning the starting position of the first expression if found

	SELECT CHARINDEX('is', 'This is a string') AS Position
	SELECT CHARINDEX('is', 'This is a string', 4) AS Position


	--B) CHARINDEX() function to perform a case-insensitive and a case-sensitive search

	SELECT CHARINDEX('server', 'SQL Server CHARINDEX') AS Position

					-- EXTRA
					SELECT SERVERPROPERTY('Collation') AS Collation
					SELECT SERVERPROPERTY('ServerName') AS Server_Name

	--Then, How can I apply case sensitive search to strings ?

	SELECT CHARINDEX ('server', 'SQL Server CHARINDEX' COLLATE Turkish_CS_AS) AS Positions              -- Latin1_General_CS_AS
			

	--C) Using CHARINDEX() function with variables

	DECLARE @document AS varchar(64) 
	SET @document = 'Reflectors are vital safety components of your bicycle.'
	SELECT CHARINDEX('safety', @document) AS Positions 

---------------------------------------------------------------------------------------------------------

PATINDEX

	--The PATINDEX() function returns the position of the first occurrence of a pattern in a string.

	--A) Syntax and basic examples

	PATINDEX ( '%pattern%' , input_string )

	SELECT PATINDEX('%ern%', 'SQL Pattern Index') AS position

	--B) Using SQL Server PATINDEX() with multiple wildcards example

	SELECT PATINDEX('%f__ction%', 'SQL Server String Function') AS position

	SELECT PATINDEX('%f__ction%', 'SQL Server String Function' COLLATE Turkish_CI_AS) AS position

	--C) Using SQL Server PATINDEX() function with table column example

	-- Find the products that contain '2018' in their product name.

	SELECT product_name, 
		   PATINDEX('%2018%', product_name) AS position
	FROM production.products
  --WHERE product_name LIKE '%2018%'
	ORDER BY product_name;

------------------------------------------------------------------------------------

LEFT

	-- Returns the left part of a character string with the specified number of characters.

	-- A) Syntax and Basic Examples

	LEFT ( character_expression , integer_expression ) 

	SELECT LEFT('SQL Server',1) Result_string_1            -- negative --> error    Large value --> itself.
	SELECT LEFT('SQL Server',5) Result_string_5
	SELECT LEFT('SQL Server',100) Result_string_100
	SELECT LEFT('SQL Server',0) Result_string_0
	SELECT LEFT('SQL Server',-4) Result_string_negative

	--B) Using the LEFT() function with a table column

	-- Find the first 7 letters of product names.

	SELECT product_name,
		   LEFT(product_name, 7) AS first_7_characters
	FROM production.products
	ORDER BY product_name;


	--C) Using LEFT() function with GROUP BY clause

	-- Count the initial numbers of the product names.

	--	STEPS
		(
			SELECT * FROM production.products

			SELECT product_name, LEFT(product_name, 1) AS initial
			FROM production.products

			SELECT LEFT(product_name, 1) AS initial
			FROM production.products
			GROUP BY left(product_name, 1)
		)

	-- FINAL SOLUTION

	SELECT
		LEFT(product_name, 1) initial,
		COUNT(product_name) AS product_count
	FROM production.products
	GROUP BY left(product_name, 1)
	
---------------------------------------------------------------------------

RIGHT

	-- Returns the right part of a character string with the specified number of characters.

	-- A) Syntax and Basic Examples

	RIGHT ( input_string , number_of_characters ) 

	SELECT RIGHT('SQL Server',8) Result_string

	-- Find the last 4 characters of product name.

	SELECT product_name,                                       -- SELECT product_name FROM production.products
		   RIGHT(product_name, 4) AS last_4_characters
	FROM production.products
	ORDER BY product_name;

	-- B) RIGHT() with GROUP BY clause example

    -- Find the total number by product's last 4 characters.

	SELECT RIGHT(product_name, 4) AS last_4_characters,
		   COUNT(product_name) AS tot_num
	FROM production.products
	GROUP BY RIGHT(product_name, 4)

-------------------------------------------------------------

SUBSTRING

	--	Returns part of a character, binary, text, or image expression in SQL Server.

	-- A) Syntax and Basic Examples

	SUBSTRING ( expression ,start , length )

	SELECT SUBSTRING('SQL Server SUBSTRING', 5, 6) result;

	SELECT store_name,
	       phone,
		   SUBSTRING(phone, 7 , 8) AS Substring_of_phone
	FROM sales.stores

-----------------------------------------------------------------------

LOWER

	--	Returns a character expression after converting uppercase character data to lowercase.

	-- A) Syntax and Basic Examples

	LOWER ( character_expression )

	SELECT LOWER('TEST') result;

	--B) Using the LOWER() function with table column

	SELECT [state],
	       LOWER([state]) AS Lower_State
	FROM sales.stores																		-- SELECT * FROM sales.stores

------------------------------------------------------------------------------------------------

UPPER

	--	Returns a character expression with lowercase character data converted to uppercase.

	-- A) Syntax and Basic Examples

	UPPER ( character_expression )

	SELECT UPPER('sql') result;

	--B) Using the UPPER() function with table column

	SELECT product_name, 
		   UPPER(product_name) AS product_name_upper
	FROM production.products
	ORDER BY product_name

-----------------------------------------------------------------------------------------------------------

STRING_SPLIT

	--	A table-valued function that splits a string into rows of substrings, based on a specified separator character.

	-- A) Syntax and Basic Examples

	STRING_SPLIT ( input_string , separator )  

	--B) Using the STRING_SPLIT() function to split comma-separated value string

	-- STRING_SPLIT outputs a single-column table whose rows contain the substrings. The name of the output column is value.

	SELECT [value] 
	FROM STRING_SPLIT('red,green,blue', ',')

------------------------------------------------------

TRIM

	--The TRIM() function removes spaces or specified characters from both ends of a string.

	-- A) Syntax and Basic Examples

	TRIM([removed_characters FROM] input_string)

	-- Remove leading and trailing spaces from a string

	SELECT TRIM('  Test string    ')

	--B) Using TRIM() function to remove specified characters from both sides of a string

	SELECT TRIM('.$' FROM '$$$Hello..') AS result


	--C) Using TRIM() function to clean up leading and trailing spaces in a column of a table

	UPDATE sales.customers
	SET  street = TRIM(street)

-------------------------------------------------------------------------------------

LTRIM

	-- Returns a character expression after it removes leading blanks.

	-- A) Syntax and Basic Examples

	LTRIM ( character_expression )

	SELECT ('      SQL Server LTRIM Function') result;

	SELECT LTRIM('      SQL Server LTRIM Function') ltrim_result


	--B) Using LTRIM() function to clean up spaces
	
	SELECT (value) part 
	FROM STRING_SPLIT('Doe, John', ',')
	                
	SELECT LTRIM(value) part
	FROM STRING_SPLIT('Doe, John', ',')  

---------------------------------------------------------------

RTRIM

	-- Returns a character string after truncating all trailing spaces.

	-- A) Syntax and Basic Examples

	RTRIM ( character_expression )

	SELECT RTRIM('SQL Server RTRIM Function   ') AS result

	SELECT RTRIM(first_name) AS Rtrimmed_Name
	FROM sales.customers 

---------------------------------------------------------------------

REPLACE
	
	-- Replaces all occurrences of a specified string value with another string value.

	-- A) Syntax and Basic Examples

	REPLACE ( string_expression , string_pattern , string_replacement )

	SELECT REPLACE( 'Success is how high you bounce when you hit bottom. George S. Patton' 
					,'S.'
                    ,'Smith'
				   ) AS result

---------------------------------------------------------------------------

STR

	--The STR() function converts a numeric value to a character value.

	-- A) Syntax and Basic Examples

	STR ( float_expression [ , length [ , decimal ] ] )  
	-- length : Is the total length. This includes decimal point, sign, digits, and spaces. The default is 10.
	-- The number is rounded to an integer by default or if the decimal parameter is 0

	SELECT STR(123.456) AS result

	SELECT STR(123.456, 6, 2) AS result

	SELECT STR(987.65, 2, 2) AS result




--*********************************************************************************************************************
--*********************************************************************************************************************
--*********************************************************************************************************************




-- ||||||||||  EXTRA EXAMPLES  |||||||||||||--





-- 1. Find the first part of the category name

	SELECT category_name, LEFT(category_name, CHARINDEX(' ', category_name)-1) AS Left_Part
	FROM production.categories 

-- 2. 
	-- A. find domains

	SELECT                                         
		email, 
		SUBSTRING( email,   CHARINDEX('@', email)+1,  LEN(email)-CHARINDEX('@', email)) AS domain
	--			||-STRING-||----------START---------||------------LENGHT-------------||
	FROM 
		sales.customers

	-- B. count the domains

	SELECT domain, COUNT(email) domain_count
	FROM  
	     (
	      SELECT email,
		  SUBSTRING(
					email,
					CHARINDEX('@', email)+1,
					LEN(email)-CHARINDEX('@', email)
					)AS domain
		   
			FROM 
			sales.customers
		  ) a
	GROUP BY domain


	
--3. Concat the first name and last name with space.

		SELECT												-- SELECT first_name, last_name FROM sales.customers
		first_name, 
		last_name, 
		CONCAT_WS(' ',   LOWER(first_name),  LOWER(last_name)) AS full_name_lowercase			--CONCAT_WS ( separator, argument1, argument2 [, argumentN]... )
--				 sprtr     argument1           argument2								
	FROM 
		sales.customers
	ORDER BY 
		first_name, 
		last_name

-- 4. Divide phone numbers in two parts then cross apply to phone numbers

	--SELECT staff_id, phone FROM sales.staffs

	SELECT staff_id, phone, value FROM sales.staffs
		CROSS APPLY STRING_SPLIT(phone, '-')


-- 5. --B) Using REPLACE() function with table columns

	SELECT                                                             -- SELECT first_name, last_name, phone FROM sales.customers WHERE phone IS NOT NULL
		first_name, 
		last_name, 
		phone, 
		REPLACE(REPLACE(phone, '(', ''), ')', '') AS replace_formatte,        -- SELECT first_name, last_name, REPLACE(phone, '(', '') phone FROM sales.customers WHERE phone IS NOT NULL
	FROM															   																	
		sales.customers												   
	WHERE phone IS NOT NULL
	ORDER BY 
		first_name, 
		last_name


	--C) Using REPLACE() function to correct data in tables

	UPDATE
		sales.customers
	SET
		phone = REPLACE(phone,'(916)','(917)')
	WHERE
		phone IS NOT NULL

	--C) Using TRANSLATE() function to correct data in tables

	--	TRANSLATE ( inputString, characters, translations)

	SELECT TRANSLATE('35*{4-1}/[5+4]', '[]{}', '()()')
	SELECT TRANSLATE('1/2*3-4+5-6/7', '-/+', 'QWE')

	-- SELECT TOP (3) first_name, last_name, phone FROM sales.customers WHERE phone IS NOT NULL

	SELECT first_name, 
		   last_name, 
		   phone, 
		   TRANSLATE(phone, '()-', '  /') phone_formatted      
	FROM sales.customers												   
	WHERE phone IS NOT NULL
    ORDER BY first_name, last_name

