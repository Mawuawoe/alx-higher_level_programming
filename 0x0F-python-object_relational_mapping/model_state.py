#!/usr/bin/python3
"""
This script defines only the State class and
the Base class.
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class State(Base):
    """
    create Table
    """
    __tablename__ = "states"

    id = Column(Integer, autoincrement=True,
                    primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)