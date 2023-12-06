#!/usr/bin/python3
"""Module that creates a Review subclass"""

import os
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel):
    __tablename__ = 'states'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )
    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            city_list = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
