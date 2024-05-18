CREATE TABLE users 
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name	VARCHAR(512),
    last_name	VARCHAR(512),
    email	VARCHAR(512),
    residence	VARCHAR(512),
    lat	DOUBLE,
    lon	DOUBLE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE products 
(
    product_id  INT AUTO_INCREMENT PRIMARY KEY,
    name	    VARCHAR(512),
    description VARCHAR(512),
    price	    DOUBLE,
    category	VARCHAR(512),
    image	    VARCHAR(512),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE orders 
(
    order_id    INT,
    user_id	    INT,
    total	    DOUBLE,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE order_detail 
(
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id    INT,
    product_id	INT,
    quantity	INT,
    price       DOUBLE,
    sub_total   DOUBLE,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
