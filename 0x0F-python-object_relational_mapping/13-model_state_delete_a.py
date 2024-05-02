#!/usr/bin/python3


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states():
    moteur = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format("root", "root", "hbtn_0e_6_usa"),
                           pool_pre_ping=True)
    Base.metadata.create_all(moteur)

    Session = sessionmaker(bind=moteur)
    session = Session()

    fon = session.query(State).filter(State.name.like("%a%")).all()

    for i in fon:
        session.delete(i)
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_states()
