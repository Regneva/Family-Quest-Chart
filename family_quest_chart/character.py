"""Class for Character"""
# 1. Standard python libraries
from uuid import uuid4
import h5py

# 2. Third party modules

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class Character:
    """Character are the player."""
    def __init__(self, username, birthday, first_name='', last_name='', email='', points='0', inventory=''):
        """Initialize the character class"""
        self.uuid = uuid4()
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = birthday
        self.points = points
        self.inventory = inventory
        self.quests = []
        self.completed_quests = [[]]
        self.uncompleted_quests = []
        self.fellowship_dict = {}
        self.quest_last_assigned = {}
        

    def assign_quest(self, quest, new_day):
        if new_day:
            if len(self.quests):
                self.uncompleted_quests = self.quests
            self.quests = []
        self.quests.append(quest)


    def read_character(self):
        pass

    def write_character(self, h5group):
        dt = h5py.string_dtype(encoding='utf-8')
        data = h5group.create_dataset(str(self.uuid), data=self.username, dtype=dt)
        data.attrs['username'] = self.username
        data.attrs['inventory'] = self.inventory
        data.attrs['email'] = self.email
        data.attrs['completed_quests'] = self.completed_quests
        data.attrs['points'] = self.points

# username
# first name
# last name
# email
# birthdate
# count of points
# inventory
# uuid