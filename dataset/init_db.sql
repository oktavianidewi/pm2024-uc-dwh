CREATE DATABASE db;
CREATE USER 'dewi'@'%' IDENTIFIED WITH 'dewi';
GRANT ALL ON db.* TO 'dewi'@'%';

/* Make sure the privileges are installed */
FLUSH PRIVILEGES;

USE db;