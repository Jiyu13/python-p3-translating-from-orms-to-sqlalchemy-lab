#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    '''contains model "Dog" with name and breed attributes.'''

    # create class attributes
    __tablename__ = "dogs"
    __table_args__ = (PrimaryKeyConstraint("id"), )
    
    # create columns
    id = Column(Integer())
    name = Column(String())
    breed = Column(String())