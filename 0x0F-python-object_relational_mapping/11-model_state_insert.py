#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    newst = State(name='Louisiana')
    session.add(newst)
    newct = session.query(State).filter_by(name='Louisiana').first()
    print(newct.id)
    session.commit()
