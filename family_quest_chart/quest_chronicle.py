"""Class for Character"""
# 1. Standard python libraries
from uuid import uuid4

# 2. Third party modules

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class QuestChronicle:
    """Chronicle of fellowships and their quests for a day."""
    def __init__(self):
        """Initialize the character class"""
        self.fellowships = []
        
    def add_fellowship(self, fellowship):
      self.fellowships.append(fellowship)
      return len(self.fellowships)-1

    
    def read_chronicle(self):
      pass
      
    def write_chronicle(self):
      pass
