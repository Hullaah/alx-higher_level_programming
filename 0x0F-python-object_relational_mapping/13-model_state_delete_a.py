#!.venv/bin/python
#!/usr/bin/python3
""" a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
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
        states = session.query(State).filter(State.name.like("%a%"))
        for state in states:
            session.delete(state)
            session.commit()

if __name__ == "__main__":
    main()
