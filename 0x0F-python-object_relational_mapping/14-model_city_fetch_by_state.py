#!/usr/bin/python3
""" a script that prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sys import argv


def main():
    """entry point of code
    """
    username, password, database = tuple(argv[1:])
    connection_string = f"mysql+mysqldb://{username}:{password}"
    connection_string += f"@localhost:3306/{database}"
    engine = create_engine(connection_string)

    with Session(engine) as session:
        table = session.query(State.name.label(
            "state_name"), City.name.label("city_name"), City.id).join(
                City).order_by(City.id)
        for row in table:
            print(f"{row.state_name}: ({row.id}) {row.city_name}")


if __name__ == "__main__":
    main()
