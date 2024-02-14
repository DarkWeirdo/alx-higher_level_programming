-- Task: Remove all records with a score <=  5 from the second_table.
-- The database name is passed as an argument to the mysql command.
DELETE FROM second_table
WHERE
    score <= 5;
