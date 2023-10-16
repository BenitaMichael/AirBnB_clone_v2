#!/usr/bin/python3
"""Module that creates a Review subclass"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Subclass for User review objects
    place_id:(string)
    user_id: (string)
    text:    (string)
    """

    place_id = ""
    user_id = ""
    text = ""
