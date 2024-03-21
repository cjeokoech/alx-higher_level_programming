#!/usr/bin/python3
"""script that lists all State objects that contain the letter a"""
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    se = session()
    Base.metadata.create_all(engine)

    list_s = se.query(State).filter(State.name.like('%a%'))\
                            .order_by(State.id).all()

    for state in list_s:
        print("{}:{}".format(state.id, state.name))

    se.close()
