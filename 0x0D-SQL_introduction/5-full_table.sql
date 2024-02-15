-- This script prints the full description of the table first_table.
-- Task: Print the full description of the table first_table.
SELECT
    table_name,
    column_name,
    data_type,
    is_nullable,
    column_default,
    column_type,
    extra
FROM
    first_table
