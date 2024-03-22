#!/usr/bin/python3
"""
This script connects to a MySQL database
and adds a new State object named "Louisiana"
to the 'states' table.
It requires the SQLAlchemy module and imports State and Base from the
model_state module.
The script prints the new states.id after creation.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def connect_to_database(user, password, db_name):
    """
    Connects to a MySQL database using
    the provided username, password, and database name.
    Returns a session object.
    """
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def add_state(session, state_name):
    """
    Creates a new State object with the specified name,
    adds it to the database, and prints the new states.id.
    """
    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py "
              "<username> <password> <database_name>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    session = connect_to_database(user, password, db_name)
    add_state(session, "Louisiana")
    session.close()
