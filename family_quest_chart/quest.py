"""Class for Quest"""
# Standard imports
from uuid import uuid4

# Third party imports

# Local imports

# Copyright Aaron Jones 2022


class Quest:
    """Quest is the chore."""
    def __init__(self):
        """Initialize the quest class."""
        self.uuid = uuid4()
        self.short_name = ''
        self.description = ''
        self.priority = 'essential'
        self.recurrence = 'daily'
        self.points = 0

# uuid
# short name
# description
# essential, important, extra
# way of managing time specific items
# points