-- remove duplicate

{{ config(
    schema='l1',
    materialized='table'
) }}

with raw_users as (

    

    WITH ranked_users AS (
        SELECT
            *, 
            ROW_NUMBER() OVER (
                PARTITION BY id
                ORDER BY created_at DESC
            ) AS row_num
        FROM
            {{ source('raw', 'users') }}
    )
    -- Select only the rows where row_num is 1, indicating the top-ranked (first occurrence) of each duplicate
    SELECT
        id
        , first_name
        , last_name
        , email
        , residence
        , lat
        , lon
        , created_at
        , updated_at
    FROM
        ranked_users
    WHERE
        row_num = 1
)

SELECT
    {{ dbt_utils.generate_surrogate_key(['id', 'updated_at']) }} as user_key
    , id
    , first_name
    , last_name
    , email
    , residence
    , lat
    , lon
    , created_at
    , updated_at
FROM raw_users

