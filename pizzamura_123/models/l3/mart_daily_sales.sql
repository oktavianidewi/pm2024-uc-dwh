{{ config(
    schema='l3',
    materialized='table'
) }}

WITH daily_sales AS (
    SELECT
        DATE(ordered_at) AS sales_date,
        SUM(sub_total) AS daily_sales
    FROM
        {{ ref('fact_orders_order_detail') }}
    GROUP BY
        DATE(ordered_at)
    ORDER BY
        sales_date
)

SELECT *
FROM daily_sales