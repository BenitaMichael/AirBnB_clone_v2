#!/usr/bin/python3
"""Module that creates a Review subclass"""

import os
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models import storageDB


class Review(BaseModel):
    __tablename__ = 'reviews'
    if storageDB == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""