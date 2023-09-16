#!/usr/bin/python3
"""a python file that contains the class definition of
a State and an instance Base = declarative_base()
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """links to the mysql table states
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
