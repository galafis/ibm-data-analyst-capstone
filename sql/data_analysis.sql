-- Sales Analysis
-- Total sales by product category
SELECT
    p.category,
    SUM(s.total) AS total_sales,
    COUNT(s.sale_id) AS total_orders,
    SUM(s.quantity) AS total_quantity,
    SUM(s.total) / SUM(s.quantity) AS average_price
FROM
    data_analyst.sales s
    JOIN data_analyst.products p ON s.product_id = p.product_id
GROUP BY
    p.category
ORDER BY
    total_sales DESC;

-- Total sales by region
SELECT
    region,
    SUM(total) AS total_sales,
    COUNT(sale_id) AS total_orders,
    SUM(quantity) AS total_quantity,
    SUM(total) / COUNT(DISTINCT customer_id) AS sales_per_customer
FROM
    data_analyst.sales
GROUP BY
    region
ORDER BY
    total_sales DESC;

-- Total sales by channel
SELECT
    channel,
    SUM(total) AS total_sales,
    COUNT(sale_id) AS total_orders,
    SUM(quantity) AS total_quantity,
    SUM(total) / COUNT(DISTINCT customer_id) AS sales_per_customer
FROM
    data_analyst.sales
GROUP BY
    channel
ORDER BY
    total_sales DESC;

-- Sales trend by month
SELECT
    TO_CHAR(DATE_TRUNC('month', date), 'YYYY-MM') AS month,
    SUM(total) AS total_sales,
    COUNT(sale_id) AS total_orders,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT customer_id) AS total_customers,
    SUM(total) / COUNT(DISTINCT customer_id) AS sales_per_customer
FROM
    data_analyst.sales
GROUP BY
    DATE_TRUNC('month', date)
ORDER BY
    DATE_TRUNC('month', date);

-- Customer Analysis
-- Top customers by total sales
SELECT
    c.customer_id,
    c.name,
    c.segment,
    c.city,
    c.state,
    c.country,
    COUNT(s.sale_id) AS total_orders,
    SUM(s.total) AS total_sales,
    SUM(s.total) / COUNT(s.sale_id) AS average_order_value
FROM
    data_analyst.sales s
    JOIN data_analyst.customers c ON s.customer_id = c.customer_id
GROUP BY
    c.customer_id,
    c.name,
    c.segment,
    c.city,
    c.state,
    c.country
ORDER BY
    total_sales DESC
LIMIT 10;

-- Customer segmentation by total sales
SELECT
    c.segment,
    COUNT(DISTINCT c.customer_id) AS total_customers,
    SUM(s.total) AS total_sales,
    SUM(s.total) / COUNT(DISTINCT c.customer_id) AS sales_per_customer,
    COUNT(s.sale_id) AS total_orders,
    COUNT(s.sale_id) / COUNT(DISTINCT c.customer_id) AS orders_per_customer,
    SUM(s.total) / COUNT(s.sale_id) AS average_order_value
FROM
    data_analyst.sales s
    JOIN data_analyst.customers c ON s.customer_id = c.customer_id
GROUP BY
    c.segment
ORDER BY
    total_sales DESC;

-- Customer acquisition by month
SELECT
    TO_CHAR(DATE_TRUNC('month', first_purchase_date), 'YYYY-MM') AS month,
    COUNT(*) AS new_customers
FROM
    data_analyst.customers
WHERE
    first_purchase_date IS NOT NULL
GROUP BY
    DATE_TRUNC('month', first_purchase_date)
ORDER BY
    DATE_TRUNC('month', first_purchase_date);

-- Product Analysis
-- Top products by total sales
SELECT
    p.product_id,
    p.name,
    p.category,
    p.subcategory,
    SUM(s.quantity) AS total_quantity,
    SUM(s.total) AS total_sales,
    SUM(s.total) / SUM(s.quantity) AS average_price,
    COUNT(DISTINCT s.customer_id) AS total_customers
FROM
    data_analyst.sales s
    JOIN data_analyst.products p ON s.product_id = p.product_id
GROUP BY
    p.product_id,
    p.name,
    p.category,
    p.subcategory
ORDER BY
    total_sales DESC
LIMIT 10;

-- Product profitability
SELECT
    p.product_id,
    p.name,
    p.category,
    p.subcategory,
    SUM(s.quantity) AS total_quantity,
    SUM(s.total) AS total_sales,
    SUM(s.quantity * p.cost) AS total_cost,
    SUM(s.total) - SUM(s.quantity * p.cost) AS total_profit,
    (SUM(s.total) - SUM(s.quantity * p.cost)) / SUM(s.total) * 100 AS profit_margin
FROM
    data_analyst.sales s
    JOIN data_analyst.products p ON s.product_id = p.product_id
GROUP BY
    p.product_id,
    p.name,
    p.category,
    p.subcategory
ORDER BY
    total_profit DESC;

-- Marketing Analysis
-- Marketing performance by campaign
SELECT
    campaign,
    SUM(cost) AS total_cost,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    CASE
        WHEN SUM(impressions) > 0 THEN SUM(clicks)::FLOAT / SUM(impressions)
        ELSE 0
    END AS ctr,
    CASE
        WHEN SUM(clicks) > 0 THEN SUM(conversions)::FLOAT / SUM(clicks)
        ELSE 0
    END AS conversion_rate,
    CASE
        WHEN SUM(conversions) > 0 THEN SUM(cost) / SUM(conversions)
        ELSE 0
    END AS cost_per_conversion
FROM
    data_analyst.marketing
GROUP BY
    campaign
ORDER BY
    total_conversions DESC;

-- Marketing performance by channel
SELECT
    channel,
    SUM(cost) AS total_cost,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    CASE
        WHEN SUM(impressions) > 0 THEN SUM(clicks)::FLOAT / SUM(impressions)
        ELSE 0
    END AS ctr,
    CASE
        WHEN SUM(clicks) > 0 THEN SUM(conversions)::FLOAT / SUM(clicks)
        ELSE 0
    END AS conversion_rate,
    CASE
        WHEN SUM(conversions) > 0 THEN SUM(cost) / SUM(conversions)
        ELSE 0
    END AS cost_per_conversion
FROM
    data_analyst.marketing
GROUP BY
    channel
ORDER BY
    total_conversions DESC;

-- Marketing performance by month
SELECT
    TO_CHAR(DATE_TRUNC('month', date), 'YYYY-MM') AS month,
    SUM(cost) AS total_cost,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    CASE
        WHEN SUM(impressions) > 0 THEN SUM(clicks)::FLOAT / SUM(impressions)
        ELSE 0
    END AS ctr,
    CASE
        WHEN SUM(clicks) > 0 THEN SUM(conversions)::FLOAT / SUM(clicks)
        ELSE 0
    END AS conversion_rate,
    CASE
        WHEN SUM(conversions) > 0 THEN SUM(cost) / SUM(conversions)
        ELSE 0
    END AS cost_per_conversion
FROM
    data_analyst.marketing
GROUP BY
    DATE_TRUNC('month', date)
ORDER BY
    DATE_TRUNC('month', date);

-- Inventory Analysis
-- Current inventory status
SELECT
    p.product_id,
    p.name,
    p.category,
    p.subcategory,
    SUM(i.quantity) AS total_quantity,
    SUM(i.quantity * p.cost) AS total_value
FROM
    data_analyst.inventory i
    JOIN data_analyst.products p ON i.product_id = p.product_id
WHERE
    i.date = (SELECT MAX(date) FROM data_analyst.inventory)
GROUP BY
    p.product_id,
    p.name,
    p.category,
    p.subcategory
ORDER BY
    total_value DESC;

-- Inventory trend by month
SELECT
    TO_CHAR(DATE_TRUNC('month', i.date), 'YYYY-MM') AS month,
    p.category,
    SUM(i.quantity) AS total_quantity,
    SUM(i.quantity * p.cost) AS total_value
FROM
    data_analyst.inventory i
    JOIN data_analyst.products p ON i.product_id = p.product_id
GROUP BY
    DATE_TRUNC('month', i.date),
    p.category
ORDER BY
    DATE_TRUNC('month', i.date),
    p.category;

-- Combined Analysis
-- Sales and marketing correlation by month
SELECT
    TO_CHAR(DATE_TRUNC('month', s.date), 'YYYY-MM') AS month,
    SUM(s.total) AS total_sales,
    SUM(m.cost) AS total_marketing_cost,
    SUM(m.conversions) AS total_conversions,
    CASE
        WHEN SUM(m.cost) > 0 THEN SUM(s.total) / SUM(m.cost)
        ELSE 0
    END AS roas
FROM
    data_analyst.sales s
    JOIN data_analyst.marketing m ON DATE_TRUNC('month', s.date) = DATE_TRUNC('month', m.date)
GROUP BY
    DATE_TRUNC('month', s.date)
ORDER BY
    DATE_TRUNC('month', s.date);

-- Sales, inventory, and marketing by product category
SELECT
    p.category,
    SUM(s.total) AS total_sales,
    SUM(s.quantity) AS total_quantity_sold,
    SUM(i.quantity) AS total_inventory,
    SUM(i.quantity * p.cost) AS total_inventory_value,
    SUM(s.total) / NULLIF(SUM(i.quantity * p.cost), 0) AS inventory_turnover
FROM
    data_analyst.products p
    LEFT JOIN data_analyst.sales s ON p.product_id = s.product_id
    LEFT JOIN data_analyst.inventory i ON p.product_id = i.product_id AND i.date = (SELECT MAX(date) FROM data_analyst.inventory)
GROUP BY
    p.category
ORDER BY
    total_sales DESC;

-- Customer lifetime value
WITH customer_orders AS (
    SELECT
        s.customer_id,
        MIN(s.date) AS first_order_date,
        MAX(s.date) AS last_order_date,
        COUNT(s.sale_id) AS total_orders,
        SUM(s.total) AS total_sales
    FROM
        data_analyst.sales s
    GROUP BY
        s.customer_id
)
SELECT
    c.customer_id,
    c.name,
    c.segment,
    co.first_order_date,
    co.last_order_date,
    EXTRACT(DAY FROM co.last_order_date - co.first_order_date) AS customer_lifespan_days,
    co.total_orders,
    co.total_sales,
    co.total_sales / NULLIF(EXTRACT(DAY FROM co.last_order_date - co.first_order_date), 0) * 365 AS annual_value,
    co.total_sales / co.total_orders AS average_order_value
FROM
    data_analyst.customers c
    JOIN customer_orders co ON c.customer_id = co.customer_id
ORDER BY
    annual_value DESC
LIMIT 10;
