#!/usr/bin/python3
"""Module that create a Amenity subclass"""

from models.base_model import BaseModel
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import storageDB


class Amenity(BaseModel):
    '''amenity class'''
    __tablename__ = 'amenities'
    if storageDB == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
