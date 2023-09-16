#!/usr/bin/python3
""" script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine) 
    session = sessionmaker(bind=engine)
    cities = session.query(State).first()
    if cities is None:
        print("Nothing")
    else:
        print(cities.id, cities.name, net=": ")
