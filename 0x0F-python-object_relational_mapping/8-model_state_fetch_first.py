#!/usr/bin/python3
"""
This script connects to a MySQL database
and prints the first State object from the 'states' table,
based on the 'states.id'.
It requires the SQLAlchemy module and imports State and Base from the
model_state module.
The script is designed to handle cases where the 'states' table might be empty.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def connect_to_database(user, password, db_name):
    """
    Connects to a MySQL database using the provided
    username, password, and database name.
    Returns a session object.
    """
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def print_first_state(session):
    """
    Queries the 'states' table and
    prints the first State object based on 'states.id'.
    If the table is empty, prints "Nothing" followed by a new line.
    """
    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database_name>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    session = connect_to_database(user, password, db_name)
    print_first_state(session)
    session.close()
