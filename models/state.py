#!/usr/bin/python3
"""Module to create a User subclass"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class for User state objects"""

    name = ""
