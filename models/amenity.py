#!/usr/bin/python3
"""Module that create a Amenity subclass"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Subclass for User amenity objects
    Public class attribute:
    name: (string)
    """

    name = ""

