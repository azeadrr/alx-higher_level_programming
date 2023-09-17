#!/usr/bin/python3
"""script that deletes all State objects with a name
containing letter a from database hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for cities in session.query(State).filter(State.name.like('%a%')):
        session.delete(cities)
    session.commit()
