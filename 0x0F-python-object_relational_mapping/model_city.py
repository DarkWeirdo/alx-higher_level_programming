#!/usr/bin/python3
"""
This module defines the City class, which represents a city in the database.
It is used to model the 'cities' table in the 'hbtn_0e_14_usa' database,
including its attributes and relationships.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents a city in the database, modeling the 'cities' table.
    Each city is associated with a state through the 'state_id' foreign key.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
