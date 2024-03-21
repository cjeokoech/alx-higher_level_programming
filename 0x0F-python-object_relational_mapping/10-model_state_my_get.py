#!/usr/bin/python3
"""script that prints the State object with the name"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    se = session()
    Base.metadata.create_all(engine)

    list_s = se.query(State).filter(State.name == argv[4]).first()

    if list_s:
        print("{}".format(list_s.id))
    else:
        print("Not found")
    se.close()
