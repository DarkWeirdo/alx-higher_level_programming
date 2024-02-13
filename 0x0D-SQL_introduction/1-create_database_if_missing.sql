-- This script creates the database hbtn_0c_0 if it does not already exist.
-- Task: Create a database named hbtn_0c_0 if it does not exist.

IF NOT EXISTS (SELECT 1
FROM sys.databases
WHERE name = 'hbtn_0c_0')
    CREATE DATABASE hbtn_0c_0;
