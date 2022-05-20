"""Class for Quest"""
# 1. Standard python libraries
from uuid import uuid4

# 2. Third party modules

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class Quest:
    """Quest is the chore."""
    def __init__(self, short_name='', description='', priority='essential', recurrance='daily', points=2):
        """Initialize the quest class."""
        self.uuid = uuid4()
        self.short_name = short_name
        self.description = description
        self.priority = priority
        self.recurrence = recurrance
        self.points = points

    def read_quest(self):
        pass

# uuid
# short name
# description
# essential, important, extra
# way of managing time specific items
# points