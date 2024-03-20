#!/usr/bin/python3
"""
This script connects to a MySQL database
and lists all cities from the 'cities' table,
including the state name for each city,
sorted by ID in ascending order.
It requires the MySQLdb module and takes three command-line arguments:
MySQL username, password, and database name.
"""

import MySQLdb
import sys


def connect_to_database(user, password, db_name):
    """
    Connects to a MySQL database
    using the provided username, password, and database name.
    Returns a connection object.
    """
    return MySQLdb.connect(
        host="localhost", port=3306, user=user, passwd=password, db=db_name
    )


def list_cities_with_state(connection):
    """
    Executes a SQL query to list all cities from the 'cities' table,
    including the state name for each city,
    sorted by ID in ascending order.
    Prints the results in the specified format.
    """
    cursor = connection.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database_name>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    connection = connect_to_database(user, password, db_name)
    list_cities_with_state(connection)
    connection.close()
