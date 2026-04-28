CREATE DATABASE IF NOT EXISTS covid_project;
USE covid_project;

USE covid_project;
SELECT COUNT(*) FROM covid_data;

-- 1. total cases 
SELECT SUM(new_cases)AS
total_cases
FROM covid_data;

-- 2. total deaths 
SELECT SUM(new_deaths)AS
total_deaths
FROM covid_data;

-- 3. which month has the highest cases
SELECT MONTH(date)AS months, 
SUM(new_cases)AS total_cases
FROM covid_data
GROUP BY MONTH(date)
ORDER BY total_cases DESC;

-- 4. which month has the highest death rate
SELECT MONTH(date)AS months, 
SUM(new_deaths)AS total_deaths
FROM covid_data
GROUP BY MONTH(date)
ORDER BY total_deaths DESC;

-- 5. avreage number of death 
SELECT AVG(new_deaths)
FROM covid_data;
