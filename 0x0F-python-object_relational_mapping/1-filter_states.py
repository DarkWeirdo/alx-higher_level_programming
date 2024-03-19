#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states from the 'states' table
where the name starts with 'N' (upper N), sorted by ID in ascending order.
It requires the MySQLdb module and takes three command-line arguments: MySQL username,
password, and database name.
"""

import MySQLdb
import sys

def connect_to_database(user, password, db_name):
    """
    Connects to a MySQL database using the provided username, password, and database name.
    Returns a connection object.
    """
    return MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name)

def list_states_starting_with_n(connection):
    """
    Executes a SQL query to list all states from the 'states' table where the name starts with 'N',
    sorted by ID in ascending order. Prints the results in the specified format.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database_name>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    connection = connect_to_database(user, password, db_name)
    list_states_starting_with_n(connection)
    connection.close()
