#!/usr/bin/python3
"""script that lists all State objects from the
database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import select
from sys import argv


def main():
    """entry point of code
    """
    username, password, database = tuple(argv[1:])
    connection_string = f"mysql+mysqldb://{username}:{password}"
    connection_string += f"@localhost:3306/{database}"
    engine = create_engine(connection_string)

    with Session(engine) as session:
        louisiana = State(name="Louisiana")
        session.add_all([louisiana])
        session.commit()
        states = session.query(State).order_by(State.id)
        for state in states:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
