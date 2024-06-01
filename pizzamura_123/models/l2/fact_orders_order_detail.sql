-- remove duplicate

{{ config(
    schema='l2',
    materialized='table'
) }}

with stg_orders_order_detail as (

    SELECT 
        o.order_key
        , o.order_id
        , o.ordered_at
        , o.user_id
        , o.total
        , o.created_at AS order_created_at
        , o.updated_at AS order_updated_at
        , od.order_detail_key
        , od.order_detail_id
        , od.product_id
        , od.quantity
        , od.price
        , od.sub_total
        , od.created_at AS order_detail_created_at
        , od.updated_at AS order_detail_updated_at
    FROM {{ source('stg', 'stg_orders') }} AS o
    LEFT JOIN {{ source('stg', 'stg_order_detail') }} AS od ON o.order_id = od.order_id
    
)

SELECT
    order_key
    , order_id
    , ordered_at
    , user_id
    , total
    , order_created_at
    , order_updated_at
    , order_detail_key
    , order_detail_id
    , product_id
    , quantity
    , price
    , sub_total
    , order_detail_created_at
    , order_detail_updated_at
FROM stg_orders_order_detail

