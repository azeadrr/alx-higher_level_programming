#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    for cities in session.query(State).order_by(State.id):
        print(cities.id, cities.name, net=": ")
