#!/usr/bin/python3


""" show table form  databaes named  """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states():
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=moteur)
    session = Session()

    fon = session.query(State).filter(State.name.like("%a%")).all()

    for i in fon:
        session.delete(i)
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_states()
