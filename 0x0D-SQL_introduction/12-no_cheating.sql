-- Task: Update the score of the record with the name 'Bob' to  10 in the second_table.
-- The database name is passed as an argument to the mysql command.
UPDATE second_table
SET
    score = 10
WHERE
    name = 'Bob';
