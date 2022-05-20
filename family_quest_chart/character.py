"""Class for Character"""
# 1. Standard python libraries
from uuid import uuid4

# 2. Third party modules

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


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