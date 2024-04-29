#!/usr/bin/python3
""" Show states from database """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def show_states():
    """ Main function to show states """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    # Retrieve states containing 'a' and order by ID
    states_with_a = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    if states_with_a:
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
    else:
        print("No record")

    session.close()


if __name__ == "__main__":
    show_states()
