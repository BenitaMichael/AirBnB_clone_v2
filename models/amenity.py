#!/usr/bin/python3
"""Module that create a Amenity subclass"""

from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from models import storage_type


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
