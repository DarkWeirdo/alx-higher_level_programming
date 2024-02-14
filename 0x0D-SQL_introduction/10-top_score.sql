-- Task: List all records of the table second_table, displaying the score and name, ordered by score highest first.
-- The database name is passed as an argument to the mysql command.
SELECT
    score,
    name
FROM
    second_table
ORDER BY
    score DESC;
