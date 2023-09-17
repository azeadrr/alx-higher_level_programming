#!/usr/bin/python3
"""
file that contains class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, MetaData, Integer, String
from sqlalchemy.ext.declarative import declarative_base

mdt = MetaData()
Base = declarative_base(metadata=mdt)

class State(Base):
    """
    Class State
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
