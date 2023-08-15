-- A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- Import in hbtn_0c_0 database the temperatures table
SOURCE ./temperatures.sql;
-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS avg_tmp FROM temperatures GROUP BY city ORDER BY avg_tmp DESC;
