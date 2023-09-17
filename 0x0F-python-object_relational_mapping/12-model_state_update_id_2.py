#!/usr/bin/python3
"""script that changes name of a State
object from database hbtn_0e_6_usa"""

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
    newct = session.query(State).filter_by(id=2).first()
    newct.name = 'New Mexico'
    session.commit()
