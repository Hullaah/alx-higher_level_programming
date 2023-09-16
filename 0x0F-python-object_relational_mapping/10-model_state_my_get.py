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
    username, password, database, state = tuple(argv[1:])
    connection_string = f"mysql+mysqldb://{username}:{password}"
    connection_string += f"@localhost:3306/{database}"
    engine = create_engine(connection_string)

    with Session(engine) as session:
        state_id = session.query(State).filter(
            State.name == state).first()
        if state_id:
            print(state_id.id)
        else:
            print("Not found")


if __name__ == "__main__":
    main()
