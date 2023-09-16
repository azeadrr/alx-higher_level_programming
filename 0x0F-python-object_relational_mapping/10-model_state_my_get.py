#!/usr/bin/python3
"""script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine) 
    session = sessionmaker(bind=engine)
    cities = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(cities[0].id)
    except IndexError:
        print("Not found")
