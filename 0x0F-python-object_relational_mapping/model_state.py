#!/usr/bin/python3
"""file that contains class definition of State
and instance Base = declarative_base()
"""

from sqlalchemy import Column, String, MetaData, Integer
from sqlalchemy.ext.declarative import declarative_base

mtdata = MetaData()
Base = declarative_base(metadata=mtdata)


class State(Base):
    """
    Class State
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
