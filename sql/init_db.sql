CREATE DATABASE test;
CREATE USER 'test_user'@'%' IDENTIFIED WITH mysql_native_password BY '123';
GRANT ALL ON test.* TO 'test_user'@'%';

/* Make sure the privileges are installed */
FLUSH PRIVILEGES;

USE test;

CREATE TABLE test_table (
  name VARCHAR(30)
);