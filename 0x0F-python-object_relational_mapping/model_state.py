#!/usr/bin/python3
""""""

from sqlalchemy.ext.declarative import declarative _base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Class state that inheritss from Base"""
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True, primary_key=True,
                nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
