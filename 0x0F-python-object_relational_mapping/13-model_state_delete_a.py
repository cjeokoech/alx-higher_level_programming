#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter a"""
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

    delete = se.query(State).filter(State.name.like('%a%')).all()
    for dele in delete:
        se.delete(dele)
    se.commit()
    se.close()
