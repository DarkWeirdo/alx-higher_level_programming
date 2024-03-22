#!/usr/bin/python3
"""
This script connects to a MySQL database and prints the State object
with the specified name from the 'states' table.
It requires the SQLAlchemy module and imports State and Base from the
model_state module.
The script is designed to handle cases where the specified state name
might not exist in the database.
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


def print_state_by_name(session, state_name):
    """
    Queries the 'states' table and prints the State object
    with the specified name.
    If no state has the specified name, prints "Not found".
    """
    state = session.query(State).filter(State.name == state_name).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python3 script.py <username> "
            "<password> <database_name> <state_name>"
        )
        sys.exit(1)

    user, password, db_name, state_name = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
    )
    session = connect_to_database(user, password, db_name)
    print_state_by_name(session, state_name)
    session.close()
