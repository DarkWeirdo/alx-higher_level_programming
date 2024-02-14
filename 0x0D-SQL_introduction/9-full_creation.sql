-- Task: Create the table second_table if it does not exist and insert multiple records
-- This script checks for the existence of the second_table and creates it if it doesn't exist.
-- It then inserts four records into the second_table.
-- The database name is passed as an argument to the mysql command.
CREATE TABLE
    IF NOT EXISTS SECOND_TABLE (ID INT, NAME VARCHAR(256), SCORE INT);

INSERT INTO
    SECOND_TABLE (ID, NAME, SCORE)
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
