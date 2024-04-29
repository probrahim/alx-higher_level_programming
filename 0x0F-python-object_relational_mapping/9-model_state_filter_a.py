#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def plutot():

    """debut de moteur creation"""

    moteur = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=moteur)

    session = Session()
    Base.metadata.create_all(moteur)

    kumul = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for i in kumul:
        print("{}: {}".format(i.id, i.name))
    session.close()


if __name__ == "__main__":
    plutot()
