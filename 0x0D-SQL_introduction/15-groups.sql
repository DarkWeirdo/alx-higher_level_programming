-- Task: List the number of records with the same score in the second_table, displaying score and number of records for each score, sorted by the number of records descending.
-- The database name is passed as an argument to the mysql command.
SELECT
    score,
    COUNT(*) AS number
FROM
    second_table
GROUP BY
    score
ORDER BY
    number desc;
