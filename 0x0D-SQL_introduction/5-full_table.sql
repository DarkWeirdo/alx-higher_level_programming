-- This script prints the full description of the table first_table.
-- Task: Print the full description of the table first_table.
SELECT CONCAT('CREATE TABLE `', TABLE_NAME, '` (\\n', GROUP_CONCAT(CONCAT('  `', COLUMN_NAME, '` ', COLUMN_TYPE)), '\\n) ENGINE=', ENGINE, ' DEFAULT CHARSET=', TABLE_COLLATION, ' COLLATE=', TABLE_COLLATION, ';') AS Create_Table
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';

