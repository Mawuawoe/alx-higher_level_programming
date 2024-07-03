#!/usr/bin/python3
"""
This script defines only the State class and
the Base class.
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Create Table
    """
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
