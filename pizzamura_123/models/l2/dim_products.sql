-- remove duplicate

{{ config(
    schema='l2',
    materialized='table'
) }}

with stg_products as (
    SELECT
        * 
    FROM
        {{ source('stg', 'stg_products') }}
)

SELECT
    product_key
    , product_id
    , name
    , description
    , price
    , category
    , image
    , created_at
    , updated_at
FROM stg_products

