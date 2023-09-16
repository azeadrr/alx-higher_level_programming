#!/usr/bin/python3
""" class definition of State"""

from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """state class"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(256), nullable=True)
    cities = relationship("City", backref="state", cascade="all, delete")
