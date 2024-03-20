#!/usr/bin/python3
"""
This script defines a State class
that represents the 'states' table in the MySQL database.
It uses SQLAlchemy for ORM (Object-Relational Mapping)
to map the State class to the 'states' table.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents the 'states' table in the MySQL database.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


"""
Ensure all classes that inherit from Base are imported
before calling Base.metadata.create_all(engine)
"""
