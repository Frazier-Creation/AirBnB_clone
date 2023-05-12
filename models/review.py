#!/usr/bin/python3
"""Review class module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Representing a Review."""
    place_id = ""
    user_id = ""
    text = ""
