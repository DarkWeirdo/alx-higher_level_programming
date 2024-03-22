#!/usr/bin/python3
"""
This script connects to a MySQL database
and updates the name of the State object
with id = 2 to "New Mexico" in the 'states' table.
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


def update_state_name(session, state_id, new_name):
    """
    Finds the State object with the
    specified id, updates its name, and commits the changes.
    """
    state = session.query(State).filter(State.id == state_id).first()
    if state is not None:
        state.name = new_name
        session.commit()
        print(f"State with id {state_id} updated to {new_name}")
    else:
        print(f"No state found with id {state_id}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py "
              "<username> <password> <database_name>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    session = connect_to_database(user, password, db_name)
    update_state_name(session, 2, "New Mexico")
    session.close()
