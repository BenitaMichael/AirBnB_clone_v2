#!/usr/bin/python3
"""Module to create a User subclass"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Subclass for User state objects
        Public class attribute:
        name: (string)
    """

    name = ""
