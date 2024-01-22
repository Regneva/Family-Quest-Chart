"""Class for Character"""
# 1. Standard python libraries
from uuid import uuid4

# 2. Third party modules

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class QuestFellowshipAssignment:
    """Assignment of the Fellowship of the quest."""
    def __init__(self, mentor, mentee, quest = None):
        """Initialize the character class"""
        self.mentor = mentor
        self.mentee = mentee
        self.mentor_daily_quest = quest
        self.mentee_daily_quest = quest
        
        self.mentor_quest_schedule = {}
        self.mentee_quest_schedule = {}

    def read_fellowship(self):
      pass
      
    def write_fellowship(self):
      pass
