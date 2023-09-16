#!/usr/bin/python3
"""script that lists all State objects from the
database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


def main():
    """entry point of code
    """
    username, password, database = tuple(argv[1:])
    connection_string = f"mysql+mysqldb://{username}:{password}"
    connection_string += f"@localhost:3306/{database}"
    engine = create_engine(connection_string)

    with Session(engine) as session:
        state_to_be_updated = session.query(
            State).filter(State.id == 2).first()
        state_to_be_updated.name = "New Mexico"
        session.add(state_to_be_updated)
        session.commit()


if __name__ == "__main__":
    main()
