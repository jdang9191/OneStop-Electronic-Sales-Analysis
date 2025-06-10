SELECT * FROM public.entire_sales_data_cleaned LIMIT 5;
SELECT "USER_ID" FROM public.entire_sales_data_cleaned;
SELECT * FROM geo_lookup;


CREATE TABLE customers
	AS SELECT DISTINCT "USER_ID", "MARKETING_CHANNEL",
	"ACCOUNT_CREATION_METHOD", "COUNTRY_CODE", "REGION",
	"LOYALTY_PROGRAM", "CREATED_ON"
FROM entire_sales_data_cleaned;

CREATE TABLE order_status
	AS SELECT "USER_ID", "ORDER_ID", "PURCHASE_TS", 
	"SHIP_TS", "DELIVERY_TS", "REFUND_TS", "TIME_TO_SHIP",
	"TIME_TO_DELIVER", "TIME_TO_REFUND"
FROM entire_sales_data_cleaned;

CREATE TABLE product
	AS SELECT DISTINCT "PRODUCT_NAME", "PRODUCT_ID", "USD_PRICE"
FROM entire_sales_data_cleaned;ß

CREATE TABLE orders 
	AS SELECT "USER_ID", "ORDER_ID", "PURCHASE_TS",
	"PRODUCT_NAME", "PRODUCT_ID", "USD_PRICE", "CURRENCY", 
	"LOCAL_PRICE", "PURCHASE_PLATFORM", "MONTH_OF_SALE", "YEAR_OF_SALE"
FROM entire_sales_data_cleaned;


-- calculating sales metrics (AOV, total revenue, number of orders)
SELECT
  CAST(SUM("USD_PRICE") as INT) AS total_revenue, -- converting to integer
  CAST(AVG("USD_PRICE") as INT) AS aov, -- converting to integer
  COUNT(DISTINCT "ORDER_ID") AS order_count
FROM entire_sales_data_cleaned;

--calculating yearly sales metrics
SELECT 
	"YEAR_OF_SALE" as year,
	CAST(SUM("USD_PRICE") as INT) AS total_revenue, -- converting to integer
    CAST(AVG("USD_PRICE") as INT) AS aov, -- converting to integer
    COUNT(DISTINCT "ORDER_ID") AS order_count
	FROM entire_sales_data_cleaned
GROUP BY "YEAR_OF_SALE";

--calculating quarterly sales metrics
SELECT
	EXTRACT(quarter FROM "PURCHASE_TS") as quarter,
	CAST(SUM("USD_PRICE") as INT) as total_revenue,
	CAST(AVG("USD_PRICE") as INT) as aov,
	COUNT(DISTINCT "ORDER_ID") as order_count
	FROM entire_sales_data_cleaned
GROUP BY quarter;
--calculating monthly sales metrics
SELECT 
	"MONTH_OF_SALE" AS month,
	CAST(SUM("USD_PRICE") as INT) as total_revenue,
	CAST(AVG("USD_PRICE") as INT) as aov,
	COUNT(DISTINCT "ORDER_ID") as order_count
	FROM entire_sales_data_cleaned
GROUP BY month
ORDER BY aov DESC, total_revenue DESC;
	

SELECT * FROM entire_sales_data_cleaned LIMIT 5;

SELECT COUNT(*) AS null_year_count
FROM entire_sales_data_cleaned
WHERE "YEAR_OF_SALE" IS NULL;

--calculating refund rate

--calculate




