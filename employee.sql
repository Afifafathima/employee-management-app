CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ssn VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    salary int
);