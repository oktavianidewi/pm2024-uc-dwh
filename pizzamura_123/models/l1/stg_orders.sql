-- remove duplicate

{{ config(
    schema='l1',
    materialized='table'
) }}

with raw_orders as (

    WITH ranked_orders AS (
        SELECT
            *, 
            ROW_NUMBER() OVER (
                PARTITION BY order_id
                ORDER BY created_at DESC
            ) AS row_num
        FROM
            {{ source('raw', 'orders') }}
    )
    -- Select only the rows where row_num is 1, indicating the top-ranked (first occurrence) of each duplicate
    SELECT
        order_id
        , ordered_at
        , user_id
        , total
        , created_at
        , updated_at
    FROM
        ranked_orders
    WHERE
        row_num = 1
)

SELECT
    {{ dbt_utils.generate_surrogate_key(['order_id', 'updated_at']) }} as order_key
    , order_id
    , ordered_at
    , user_id
    , total
    , created_at
    , updated_at
FROM raw_orders

