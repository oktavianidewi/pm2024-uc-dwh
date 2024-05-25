-- DDL queries to create schema and tables in redshift

CREATE SCHEMA db_pizzamura;

CREATE TABLE db_pizzamura.users 
(
    id INTEGER,
    first_name	VARCHAR(512),
    last_name	VARCHAR(512),
    email	VARCHAR(512),
    residence	VARCHAR(512),
    lat	DOUBLE PRECISION,
    lon	DOUBLE PRECISION,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE db_pizzamura.products 
(
    product_id  INTEGER,
    name	    VARCHAR(512),
    description VARCHAR(512),
    price	    DOUBLE PRECISION,
    category	VARCHAR(512),
    image	    VARCHAR(512),
    created_at  TIMESTAMP,
    updated_at  TIMESTAMP
);

CREATE TABLE db_pizzamura.orders 
(
    order_id    INTEGER,
    ordered_at  TIMESTAMP,
    user_id	    INTEGER,
    total	    DOUBLE PRECISION,
    created_at  TIMESTAMP,
    updated_at  TIMESTAMP
);

CREATE TABLE db_pizzamura.order_detail 
(
    order_detail_id INTEGER,
    order_id    INTEGER,
    product_id	INTEGER,
    quantity	INTEGER,
    price       DOUBLE PRECISION,
    sub_total   DOUBLE PRECISION,
    created_at  TIMESTAMP,
    updated_at  TIMESTAMP
);


