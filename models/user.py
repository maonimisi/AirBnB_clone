#!/usr/bin/python3
"""Module contains the user class object"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines user class model
        Attributes: email, password, first_name, last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
