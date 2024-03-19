#!/usr/bin/python3
"""
This script connects to a MySQL database
and lists all states from the 'states' table
where the name matches the provided argument, sorted by ID in ascending order.
It requires the MySQLdb module
and takes four command-line arguments: MySQL username,
password, database name, and the state name to search for.
"""

import MySQLdb
import sys


def connect_to_database(user, password, db_name):
    """
    Connects to a MySQL database using the provided
    username, password, and database name.
    Returns a connection object.
    """
    return MySQLdb.connect(
        host="localhost", port=3306, user=user, passwd=password, db=db_name
    )


def list_states_matching_name(connection, state_name):
    """
    Executes a SQL query to list all states from the 'states' table
    where the name matches
    the provided state name, sorted by ID in ascending order.
    Prints the results in the specified format.
    """
    cursor = connection.cursor()
    query = ("SELECT id, name FROM states "
             "WHERE BINARY name = %s ORDER BY id ASC")
    cursor.execute(query, (state_name,))
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python3 script.py <username> <password> "
            "<database_name> <state_name>"
        )
        sys.exit(1)

    user, password, db_name, state_name = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
    )
    connection = connect_to_database(user, password, db_name)
    list_states_matching_name(connection, state_name)
    connection.close()
