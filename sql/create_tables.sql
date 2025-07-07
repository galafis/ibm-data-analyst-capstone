-- Create schema
CREATE SCHEMA IF NOT EXISTS data_analyst;

-- Create tables
CREATE TABLE IF NOT EXISTS data_analyst.sales (
    sale_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    product_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    region VARCHAR(50) NOT NULL,
    channel VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS data_analyst.products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(50) NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS data_analyst.customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(200),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    segment VARCHAR(50) NOT NULL,
    first_purchase_date DATE
);

CREATE TABLE IF NOT EXISTS data_analyst.marketing (
    marketing_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    campaign VARCHAR(100) NOT NULL,
    channel VARCHAR(50) NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    impressions INTEGER,
    clicks INTEGER,
    conversions INTEGER
);

CREATE TABLE IF NOT EXISTS data_analyst.inventory (
    inventory_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    warehouse VARCHAR(50) NOT NULL
);

-- Create views
CREATE OR REPLACE VIEW data_analyst.sales_by_product AS
SELECT
    p.product_id,
    p.name,
    p.category,
    p.subcategory,
    SUM(s.quantity) AS total_quantity,
    SUM(s.total) AS total_sales,
    SUM(s.total) / SUM(s.quantity) AS average_price
FROM
    data_analyst.sales s
    JOIN data_analyst.products p ON s.product_id = p.product_id
GROUP BY
    p.product_id,
    p.name,
    p.category,
    p.subcategory;

CREATE OR REPLACE VIEW data_analyst.sales_by_customer AS
SELECT
    c.customer_id,
    c.name,
    c.segment,
    c.city,
    c.state,
    c.country,
    COUNT(s.sale_id) AS total_orders,
    SUM(s.total) AS total_sales
FROM
    data_analyst.sales s
    JOIN data_analyst.customers c ON s.customer_id = c.customer_id
GROUP BY
    c.customer_id,
    c.name,
    c.segment,
    c.city,
    c.state,
    c.country;

CREATE OR REPLACE VIEW data_analyst.sales_by_date AS
SELECT
    DATE_TRUNC('day', s.date) AS day,
    DATE_TRUNC('month', s.date) AS month,
    DATE_TRUNC('quarter', s.date) AS quarter,
    DATE_TRUNC('year', s.date) AS year,
    SUM(s.total) AS total_sales,
    COUNT(DISTINCT s.customer_id) AS total_customers,
    SUM(s.total) / COUNT(DISTINCT s.customer_id) AS sales_per_customer
FROM
    data_analyst.sales s
GROUP BY
    DATE_TRUNC('day', s.date),
    DATE_TRUNC('month', s.date),
    DATE_TRUNC('quarter', s.date),
    DATE_TRUNC('year', s.date);

CREATE OR REPLACE VIEW data_analyst.marketing_performance AS
SELECT
    DATE_TRUNC('day', m.date) AS day,
    DATE_TRUNC('month', m.date) AS month,
    DATE_TRUNC('quarter', m.date) AS quarter,
    DATE_TRUNC('year', m.date) AS year,
    m.campaign,
    m.channel,
    SUM(m.cost) AS total_cost,
    SUM(m.impressions) AS total_impressions,
    SUM(m.clicks) AS total_clicks,
    SUM(m.conversions) AS total_conversions,
    CASE
        WHEN SUM(m.impressions) > 0 THEN SUM(m.clicks)::FLOAT / SUM(m.impressions)
        ELSE 0
    END AS ctr,
    CASE
        WHEN SUM(m.clicks) > 0 THEN SUM(m.conversions)::FLOAT / SUM(m.clicks)
        ELSE 0
    END AS conversion_rate,
    CASE
        WHEN SUM(m.conversions) > 0 THEN SUM(m.cost) / SUM(m.conversions)
        ELSE 0
    END AS cost_per_conversion
FROM
    data_analyst.marketing m
GROUP BY
    DATE_TRUNC('day', m.date),
    DATE_TRUNC('month', m.date),
    DATE_TRUNC('quarter', m.date),
    DATE_TRUNC('year', m.date),
    m.campaign,
    m.channel;

CREATE OR REPLACE VIEW data_analyst.inventory_status AS
SELECT
    i.date,
    p.product_id,
    p.name,
    p.category,
    p.subcategory,
    i.warehouse,
    i.quantity,
    p.cost * i.quantity AS inventory_value
FROM
    data_analyst.inventory i
    JOIN data_analyst.products p ON i.product_id = p.product_id;

-- Create functions
CREATE OR REPLACE FUNCTION data_analyst.calculate_revenue_growth(
    start_date DATE,
    end_date DATE,
    interval_type VARCHAR(10)
)
RETURNS TABLE (
    period VARCHAR(20),
    revenue DECIMAL(10, 2),
    previous_revenue DECIMAL(10, 2),
    growth_amount DECIMAL(10, 2),
    growth_percentage DECIMAL(5, 2)
)
AS $$
BEGIN
    RETURN QUERY
    WITH periods AS (
        SELECT
            CASE
                WHEN interval_type = 'day' THEN TO_CHAR(date, 'YYYY-MM-DD')
                WHEN interval_type = 'week' THEN TO_CHAR(date_trunc('week', date), 'YYYY-MM-DD')
                WHEN interval_type = 'month' THEN TO_CHAR(date_trunc('month', date), 'YYYY-MM')
                WHEN interval_type = 'quarter' THEN TO_CHAR(date_trunc('quarter', date), 'YYYY-Q') || TO_CHAR(date_trunc('quarter', date), 'Q')
                WHEN interval_type = 'year' THEN TO_CHAR(date_trunc('year', date), 'YYYY')
                ELSE TO_CHAR(date, 'YYYY-MM-DD')
            END AS period,
            SUM(total) AS revenue
        FROM
            data_analyst.sales
        WHERE
            date BETWEEN start_date AND end_date
        GROUP BY
            period
        ORDER BY
            period
    ),
    periods_with_previous AS (
        SELECT
            period,
            revenue,
            LAG(revenue) OVER (ORDER BY period) AS previous_revenue
        FROM
            periods
    )
    SELECT
        period,
        revenue,
        previous_revenue,
        revenue - COALESCE(previous_revenue, 0) AS growth_amount,
        CASE
            WHEN COALESCE(previous_revenue, 0) = 0 THEN NULL
            ELSE ((revenue - previous_revenue) / previous_revenue) * 100
        END AS growth_percentage
    FROM
        periods_with_previous;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION data_analyst.calculate_customer_acquisition_cost(
    start_date DATE,
    end_date DATE,
    interval_type VARCHAR(10)
)
RETURNS TABLE (
    period VARCHAR(20),
    marketing_cost DECIMAL(10, 2),
    new_customers INTEGER,
    cac DECIMAL(10, 2)
)
AS $$
BEGIN
    RETURN QUERY
    WITH marketing_costs AS (
        SELECT
            CASE
                WHEN interval_type = 'day' THEN TO_CHAR(date, 'YYYY-MM-DD')
                WHEN interval_type = 'week' THEN TO_CHAR(date_trunc('week', date), 'YYYY-MM-DD')
                WHEN interval_type = 'month' THEN TO_CHAR(date_trunc('month', date), 'YYYY-MM')
                WHEN interval_type = 'quarter' THEN TO_CHAR(date_trunc('quarter', date), 'YYYY-Q') || TO_CHAR(date_trunc('quarter', date), 'Q')
                WHEN interval_type = 'year' THEN TO_CHAR(date_trunc('year', date), 'YYYY')
                ELSE TO_CHAR(date, 'YYYY-MM-DD')
            END AS period,
            SUM(cost) AS marketing_cost
        FROM
            data_analyst.marketing
        WHERE
            date BETWEEN start_date AND end_date
        GROUP BY
            period
    ),
    new_customers AS (
        SELECT
            CASE
                WHEN interval_type = 'day' THEN TO_CHAR(first_purchase_date, 'YYYY-MM-DD')
                WHEN interval_type = 'week' THEN TO_CHAR(date_trunc('week', first_purchase_date), 'YYYY-MM-DD')
                WHEN interval_type = 'month' THEN TO_CHAR(date_trunc('month', first_purchase_date), 'YYYY-MM')
                WHEN interval_type = 'quarter' THEN TO_CHAR(date_trunc('quarter', first_purchase_date), 'YYYY-Q') || TO_CHAR(date_trunc('quarter', first_purchase_date), 'Q')
                WHEN interval_type = 'year' THEN TO_CHAR(date_trunc('year', first_purchase_date), 'YYYY')
                ELSE TO_CHAR(first_purchase_date, 'YYYY-MM-DD')
            END AS period,
            COUNT(*) AS new_customers
        FROM
            data_analyst.customers
        WHERE
            first_purchase_date BETWEEN start_date AND end_date
        GROUP BY
            period
    )
    SELECT
        COALESCE(mc.period, nc.period) AS period,
        COALESCE(mc.marketing_cost, 0) AS marketing_cost,
        COALESCE(nc.new_customers, 0) AS new_customers,
        CASE
            WHEN COALESCE(nc.new_customers, 0) = 0 THEN NULL
            ELSE COALESCE(mc.marketing_cost, 0) / nc.new_customers
        END AS cac
    FROM
        marketing_costs mc
        FULL OUTER JOIN new_customers nc ON mc.period = nc.period
    ORDER BY
        period;
END;
$$ LANGUAGE plpgsql;

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_sales_date ON data_analyst.sales(date);
CREATE INDEX IF NOT EXISTS idx_sales_product_id ON data_analyst.sales(product_id);
CREATE INDEX IF NOT EXISTS idx_sales_customer_id ON data_analyst.sales(customer_id);
CREATE INDEX IF NOT EXISTS idx_marketing_date ON data_analyst.marketing(date);
CREATE INDEX IF NOT EXISTS idx_inventory_date ON data_analyst.inventory(date);
CREATE INDEX IF NOT EXISTS idx_inventory_product_id ON data_analyst.inventory(product_id);
