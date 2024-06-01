-- remove duplicate

{{ config(
    schema='l1',
    materialized='table'
) }}

with raw_products as (

    

    WITH ranked_products AS (
        SELECT
            *, 
            ROW_NUMBER() OVER (
                PARTITION BY product_id
                ORDER BY created_at DESC
            ) AS row_num
        FROM
            {{ source('raw', 'products') }}
    )
    -- Select only the rows where row_num is 1, indicating the top-ranked (first occurrence) of each duplicate
    SELECT
        product_id
        , name
        , description
        , price
        , category
        , image
        , created_at
        , updated_at
    FROM
        ranked_products
    WHERE
        row_num = 1
)

SELECT
    {{ dbt_utils.generate_surrogate_key(['product_id', 'updated_at']) }} as product_key
    , product_id
    , name
    , description
    , price
    , category
    , image
    , created_at
    , updated_at
FROM raw_products

