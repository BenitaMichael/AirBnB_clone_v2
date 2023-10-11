#!/usr/bin/python3
"""Module that creates a Review subclass"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for User review objects"""

    place_id = ""
    user_id = ""
    text = ""

