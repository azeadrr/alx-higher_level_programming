#!/usr/bin/python3
"""
Python file contains
class definition of a City
"""

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """Class city"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey("states.id"), Integer, nullable=False)
