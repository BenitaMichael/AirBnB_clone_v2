#!/usr/bin/python3
"""Module creates a User subclass"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Subclass for User city objects
    Public class attributes:
    state_id: (string)
    name:(string)
    """

    state_id = ""
    name = ""
