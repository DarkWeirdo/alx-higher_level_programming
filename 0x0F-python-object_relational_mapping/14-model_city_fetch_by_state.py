#!/usr/bin/python3
"""
This script connects to a MySQL database
and prints all City objects from the 'cities' table,
sorted by 'cities.id' in ascending order.
It requires the SQLAlchemy module and imports State and Base
from the model_state module.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def connect_to_database(user, password, db_name):
    """
    Connects to a MySQL database
    using the provided username, password, and database name.
    Returns a session object.
    """
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def print_cities_by_state(session):
    """
    Queries the 'cities' table and prints all City objects,
    sorted by 'cities.id' in ascending order,
    in the format: <state name>: (<city id>) <city name>.
    """
    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py "
              "<username> <password> <database_name>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    session = connect_to_database(user, password, db_name)
    print_cities_by_state(session)
    session.close()
