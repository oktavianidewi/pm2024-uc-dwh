-- remove duplicate

{{ config(
    schema='l1',
    materialized='table'
) }}

with raw_order_detail as (

    WITH ranked_order_detail AS (
        SELECT
            *, 
            ROW_NUMBER() OVER (
                PARTITION BY order_detail_id
                ORDER BY created_at DESC
            ) AS row_num
        FROM
            {{ source('raw', 'order_detail') }}
    )
    -- Select only the rows where row_num is 1, indicating the top-ranked (first occurrence) of each duplicate
    SELECT
        order_detail_id
        , order_id
        , product_id
        , quantity
        , price
        , sub_total
        , created_at
        , updated_at
    FROM
        ranked_order_detail
    WHERE
        row_num = 1
)

SELECT
    {{ dbt_utils.generate_surrogate_key(['order_detail_id', 'updated_at']) }} as order_detail_key
    , order_detail_id
    , order_id
    , product_id
    , quantity
    , price
    , sub_total
    , created_at
    , updated_at
FROM raw_order_detail

