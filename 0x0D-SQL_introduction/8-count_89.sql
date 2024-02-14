-- Task: Display the number of records with id =  89 in the table first_table
-- This script counts the number of records in the first_table where the id equals  89.
-- The database name is passed as an argument to the mysql command.

SELECT COUNT(*)
FROM first_table
WHERE ID =  89;
