#!/usr/bin/python3
"""a python file that contains the class
   definition of a State
"""

from sqlalchemy.ext.declarative import declarative_base
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
