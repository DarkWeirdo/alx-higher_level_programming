0x0D-SQL_introduction
task 0:
 The SHOW DATABASES; command in  0-list_databases.sql file is correct for listing all databases. When we run this script through the command line using cat and pipe (|) it to the mysql client, it executes the SQL command against the MySQL server specified by -hlocalhost, -uroot, and prompts for the root password due to -p.

Here's what happens step by step when we execute the command:

cat 0-list_databases.sql reads the content of the 0-list_databases.sql file and outputs it to the standard output.
| pipes the output of the cat command to the next command.
mysql -hlocalhost -uroot -p connects to the MySQL server running on localhost with the username root and prompts for the password.
Once connected, the SHOW DATABASES; command is executed, and the list of databases is displayed in the terminal.

task 1:
To create a database named hbtn_0c_0 in our MySQL server without using SELECT or SHOW statements, and to ensure that the script does not fail if the database already exists, we can use the CREATE DATABASE IF NOT EXISTS statement. This statement checks if the database exists and creates it only if it doesn't exist.

task 2:
 you can use the DROP DATABASE IF EXISTS statement. This statement checks if the database exists and drops it only if it exists. Since the DROP DATABASE IF EXISTS statement is idempotent, it won't cause an error if the database does not exist, and it will drop the database if it does.

task 3:
To list all the tables of a specific database in your MySQL server, you can use the SHOW TABLES; command within the context of the desired database. Since the database name will be passed as an argument to the mysql command, you don't need to hardcode the database name in the SQL script itself. Instead, you can use the USE statement to switch to the specified database before executing SHOW TABLES;.

task 3:
To create a table called `first_table` with columns `id` and `name` in the current database on your MySQL server, without using `SELECT` or `SHOW` statements, and to ensure that the script does not fail if the table already exists, you can use the `CREATE TABLE IF NOT EXISTS` statement. This statement checks if the table exists and creates it only if it doesn't exist.
