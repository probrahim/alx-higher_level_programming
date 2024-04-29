#!/usr/bin/python3
"""Prints the State"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def pol():
    moteur = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(moteur)
    Session = sessionmaker(bind=moteur)
    session = Session()
    pug = session.query(State).filter(State.id == 2).all()

    if pug:
        pug[0].name = "New Mexico"
    session.commit()
    session.close()


if __name__ == "__main__":
    pol()
