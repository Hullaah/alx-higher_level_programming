-- A script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
-- Creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Inserts Johnn into the record
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
-- Inserts Alex into the record
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
-- Inserts Bob into the record
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
-- Inserts George into the record
INSERT INTO second_table (id, name , score) VALUES (4, "George", 8);
