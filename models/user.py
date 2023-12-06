#!/usr/bin/python3
"""Module to create a User class"""
from models import storageDB
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class User(BaseModel):
    """Subclass for user objects"""
    __tablename__ = 'users'
    if storageDB == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')

    email = ""
    password = ""
    first_name = ""
    last_name = ""
