-- Task: List all records with a score >=  10 from the second_table, displaying score and name, ordered by score highest first.
-- The database name is passed as an argument to the mysql command.
SELECT
    score,
    name
FROM
    second_table
WHERE
    score >= 10
ORDER BY
    score desc;
