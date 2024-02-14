-- This script prints the full description of the table first_table.
-- Task: Print the full description of the table first_table.
SELECT
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE,
    IS_NULLABLE,
    COLUMN_DEFAULT,
    COLUMN_TYPE,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE  
    TABLE_SCHEMA = 'your_database_name'
    AND
    TABLE_NAME = 'your_table_name';
