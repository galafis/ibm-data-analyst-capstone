-- ETL Process for Data Analyst Platform

-- Step 1: Extract data from source tables
-- Create temporary tables to store extracted data
CREATE TEMPORARY TABLE temp_sales AS
SELECT * FROM source_schema.sales;

CREATE TEMPORARY TABLE temp_products AS
SELECT * FROM source_schema.products;

CREATE TEMPORARY TABLE temp_customers AS
SELECT * FROM source_schema.customers;

CREATE TEMPORARY TABLE temp_marketing AS
SELECT * FROM source_schema.marketing;

CREATE TEMPORARY TABLE temp_inventory AS
SELECT * FROM source_schema.inventory;

-- Step 2: Transform data
-- Clean and transform sales data
CREATE TEMPORARY TABLE transformed_sales AS
SELECT
    sale_id,
    date,
    product_id,
    customer_id,
    quantity,
    price,
    quantity * price AS total,  -- Calculate total
    UPPER(region) AS region,    -- Standardize region names
    INITCAP(channel) AS channel -- Standardize channel names
FROM
    temp_sales
WHERE
    quantity > 0                -- Filter out invalid quantities
    AND price > 0               -- Filter out invalid prices
    AND date IS NOT NULL;       -- Filter out records with missing dates

-- Clean and transform products data
CREATE TEMPORARY TABLE transformed_products AS
SELECT
    product_id,
    TRIM(name) AS name,         -- Trim whitespace
    INITCAP(category) AS category,       -- Standardize category names
    INITCAP(subcategory) AS subcategory, -- Standardize subcategory names
    cost,
    price,
    price - cost AS profit      -- Calculate profit
FROM
    temp_products
WHERE
    cost > 0                    -- Filter out invalid costs
    AND price > 0               -- Filter out invalid prices
    AND name IS NOT NULL;       -- Filter out records with missing names

-- Clean and transform customers data
CREATE TEMPORARY TABLE transformed_customers AS
SELECT
    customer_id,
    TRIM(name) AS name,         -- Trim whitespace
    LOWER(email) AS email,      -- Standardize email addresses
    phone,
    TRIM(address) AS address,   -- Trim whitespace
    INITCAP(city) AS city,      -- Standardize city names
    UPPER(state) AS state,      -- Standardize state names
    UPPER(country) AS country,  -- Standardize country names
    postal_code,
    INITCAP(segment) AS segment, -- Standardize segment names
    first_purchase_date
FROM
    temp_customers
WHERE
    name IS NOT NULL            -- Filter out records with missing names
    AND email IS NOT NULL;      -- Filter out records with missing emails

-- Clean and transform marketing data
CREATE TEMPORARY TABLE transformed_marketing AS
SELECT
    marketing_id,
    date,
    TRIM(campaign) AS campaign, -- Trim whitespace
    INITCAP(channel) AS channel, -- Standardize channel names
    cost,
    GREATEST(impressions, 0) AS impressions, -- Ensure non-negative values
    GREATEST(clicks, 0) AS clicks,           -- Ensure non-negative values
    GREATEST(conversions, 0) AS conversions  -- Ensure non-negative values
FROM
    temp_marketing
WHERE
    date IS NOT NULL            -- Filter out records with missing dates
    AND cost > 0;               -- Filter out invalid costs

-- Clean and transform inventory data
CREATE TEMPORARY TABLE transformed_inventory AS
SELECT
    inventory_id,
    date,
    product_id,
    GREATEST(quantity, 0) AS quantity, -- Ensure non-negative values
    UPPER(warehouse) AS warehouse      -- Standardize warehouse names
FROM
    temp_inventory
WHERE
    date IS NOT NULL            -- Filter out records with missing dates
    AND product_id IS NOT NULL; -- Filter out records with missing product IDs

-- Step 3: Load data into target tables
-- Load sales data
INSERT INTO data_analyst.sales (
    sale_id,
    date,
    product_id,
    customer_id,
    quantity,
    price,
    total,
    region,
    channel
)
SELECT
    sale_id,
    date,
    product_id,
    customer_id,
    quantity,
    price,
    total,
    region,
    channel
FROM
    transformed_sales;

-- Load products data
INSERT INTO data_analyst.products (
    product_id,
    name,
    category,
    subcategory,
    cost,
    price
)
SELECT
    product_id,
    name,
    category,
    subcategory,
    cost,
    price
FROM
    transformed_products;

-- Load customers data
INSERT INTO data_analyst.customers (
    customer_id,
    name,
    email,
    phone,
    address,
    city,
    state,
    country,
    postal_code,
    segment,
    first_purchase_date
)
SELECT
    customer_id,
    name,
    email,
    phone,
    address,
    city,
    state,
    country,
    postal_code,
    segment,
    first_purchase_date
FROM
    transformed_customers;

-- Load marketing data
INSERT INTO data_analyst.marketing (
    marketing_id,
    date,
    campaign,
    channel,
    cost,
    impressions,
    clicks,
    conversions
)
SELECT
    marketing_id,
    date,
    campaign,
    channel,
    cost,
    impressions,
    clicks,
    conversions
FROM
    transformed_marketing;

-- Load inventory data
INSERT INTO data_analyst.inventory (
    inventory_id,
    date,
    product_id,
    quantity,
    warehouse
)
SELECT
    inventory_id,
    date,
    product_id,
    quantity,
    warehouse
FROM
    transformed_inventory;

-- Step 4: Verify data load
SELECT COUNT(*) AS sales_count FROM data_analyst.sales;
SELECT COUNT(*) AS products_count FROM data_analyst.products;
SELECT COUNT(*) AS customers_count FROM data_analyst.customers;
SELECT COUNT(*) AS marketing_count FROM data_analyst.marketing;
SELECT COUNT(*) AS inventory_count FROM data_analyst.inventory;

-- Step 5: Clean up temporary tables
DROP TABLE temp_sales;
DROP TABLE temp_products;
DROP TABLE temp_customers;
DROP TABLE temp_marketing;
DROP TABLE temp_inventory;
DROP TABLE transformed_sales;
DROP TABLE transformed_products;
DROP TABLE transformed_customers;
DROP TABLE transformed_marketing;
DROP TABLE transformed_inventory;
