-- This script prints the full description of the table first_table.
-- Task: Print the full description of the table first_table.

SELECT CONCAT('CREATE TABLE `', TABLE_NAME, '` (\\n', GROUP_CONCAT(COLUMN_TYPE), '\\n) ENGINE=', ENGINE, ' DEFAULT CHARSET=', TABLE_COLLATION, ';') AS Create_Table
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';

