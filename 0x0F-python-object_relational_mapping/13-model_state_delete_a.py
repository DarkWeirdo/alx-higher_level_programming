#!/usr/bin/python3
"""
This script connects to a MySQL database and deletes all State objects
from the 'states' table where the name contains the letter 'a'.
It requires the SQLAlchemy module and imports State and Base
from the model_state module.
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


def delete_states_with_a(session):
    """
    Finds all State objects where the name contains the letter 'a',
    deletes them, and commits the changes.
    """
    states_to_delete = (session
                        .query(State)
                        .filter(State.name.contains("a"))
                        .all())
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    print("States with 'a' in their name have been deleted.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py "
              "<username> <password> <database_name>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    session = connect_to_database(user, password, db_name)
    delete_states_with_a(session)
    session.close()
