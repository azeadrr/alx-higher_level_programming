#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    meta = Base.metadata
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True, pool_recycle=False
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    ct_st = session.query(City, State).\
        join(State, City.state_id == State.id).order_by(City.id).all()
    for city, state in ct_st:
        print("{}: {} -> {}".format(city.id, city.name, state.name))
