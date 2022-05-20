"""Class for Character"""
# Standard imports
from uuid import uuid4

# Third party imports

# Local imports

# Copyright Aaron Jones 2022


class Character:
    """Character are the player."""
    def __init__(self):
        """Initialize the character class"""
        self.uuid = uuid4()
        self.username = ''
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        # self.birthday = ''
        self.points = 0
        self.inventory = []

# username
# first name
# last name
# email
# birthdate
# count of points
# inventory
# uuid