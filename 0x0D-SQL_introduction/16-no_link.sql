-- Task: List all records from the second_table with a non-null name value, displaying score and name, sorted by score descending.
-- The database name is passed as an argument to the mysql command.
SELECT
    score,
    name
FROM
    second_table
WHERE
    name IS NOT NULL
ORDER BY
    score desc;
