-- This script creates the table first_table if it does not already exist.
-- Task: Create a table named first_table with columns id and name if it does not exist.

CREATE TABLE
IF NOT EXISTS first_table
(
    id INT,
    name VARCHAR
(256)
);
