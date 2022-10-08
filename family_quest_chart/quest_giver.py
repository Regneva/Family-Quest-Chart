"""Class for QuestGiver"""
# 1. Standard python libraries
from uuid import uuid4

# 2. Third party modules
import h5py

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class QuestGiver:
    """Quest giver assigns to quests to characters."""
    def __init__(self, directory):
        """Initialize the quest class."""
        self.characters = []
        self.quests = []
        self.directory = directory

        self.roles = []

    def read_all_quests(self, f):
        pass

    def write_all_quests(self, f):
        grp = f.create_group("Quests")
        for quest in self.quests:
            quest.write_quest(grp)

    def read_all_characters(self, f):
        pass
    
    def write_all_characters(self, f):
        pass
    
    def read_file(self, filename='quest_giver.hdf5'):
        with h5py.File(filename, 'r') as f:
            self.read_all_quests(f)
            self.read_all_characters(f)
    
    def write_file(self, filename='quest_giver.hdf5'):
        with h5py.File(filename, 'w') as f:
            self.write_all_quests(f)
            self.write_all_characters(f)

    def assign_all_quests(self):
        # Assign mentors by birthdate
        # Determine quests to assign based on priority
        # Assign the quests
        pass

    def compute_data(self):
        self.read_all_quests()
        self.read_all_characters()
        self.assign_all_quests()
