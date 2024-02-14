-- Task: Compute the average score of all records in the second_table.
-- The result column name should be average.
-- The database name is passed as an argument to the mysql command.
SELECT
    AVG(score) AS average
FROM
    second_table;
