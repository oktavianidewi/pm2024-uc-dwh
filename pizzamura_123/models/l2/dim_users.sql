-- remove duplicate

{{ config(
    schema='l2',
    materialized='table'
) }}

with stg_users as (

    SELECT
        *
    FROM
        {{ source('stg', 'stg_users') }}
    
)

SELECT
    user_key
    , id
    , first_name
    , last_name
    , email
    , residence
    , lat
    , lon
    , created_at
    , updated_at
FROM stg_users

