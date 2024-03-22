#!/usr/bin/python3
"""
This script connects to a MySQL database and lists
all State objects from the 'states' table
that contain the letter 'a' in their name,
sorted by 'states.id' in ascending order.
It requires the SQLAlchemy module
and imports State and Base from the model_state module.
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


def list_states_with_a(session):
    """
    Queries the 'states' table and lists all State objects
    that contain the letter 'a' in their name,
    sorted by 'states.id' in ascending order.
    """
    states = (
        session.query(State)
        .filter(State.name.contains('a'))
        .order_by(State.id)
        .all()
    )
    if not states:
        print("No records found.")
    else:
        for state in states:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database_name>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    session = connect_to_database(user, password, db_name)
    list_states_with_a(session)
    session.close()
