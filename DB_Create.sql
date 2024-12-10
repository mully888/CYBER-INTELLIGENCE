CREATE DATABASE database1;
CREATE DATABASE database2;
CREATE DATABASE database3;

USE database1;

-- Creazione tabella email
CREATE TABLE IF NOT EXISTS email (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL
);


USE database2;
CREATE TABLE IF NOT EXISTS email (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL
);


USE database3;
CREATE TABLE IF NOT EXISTS email (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE USER 'check_user'@'localhost' IDENTIFIED BY '';
GRANT SELECT ON database1.email TO 'check_user'@'localhost';

GRANT SELECT ON database2.email TO 'check_user'@'localhost';

GRANT SELECT ON database3.email TO 'check_user'@'localhost';