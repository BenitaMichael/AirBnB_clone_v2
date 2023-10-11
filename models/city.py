#!/usr/bin/python3
"""Module creates a User subclass"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for User city objects"""

    state_id = ""
    name = ""
