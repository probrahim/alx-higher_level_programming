#!/usr/bin/python3
"""Prints the State"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def pls():
    moteur = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=moteur)
    session = Session()

    found = False
    pul = session.query(State)
    for i in pul:
        if i.name == argv[4]:
            print("{}".format(i.id))
            found = True
            break
    if found is False:
        print("Not found")
    session.close()


if __name__ == "__main__":
    pls()
