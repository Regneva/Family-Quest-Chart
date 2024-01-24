"""Class for Quest"""
# 1. Standard python libraries
from uuid import uuid4

# 2. Third party modules
import h5py
import numpy as np

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class Quest:
    """Quest is the chore."""
    # def __init__(self, short_name='', description='', priority='essential', recurrance='Daily', 
    #              points=2, assign_by_day=False):
    def __init__(self, name='', description='', priority=1, 
                 points=2, assign_by_day=False):
    # def __init__(self, name='', description='', check_off_instructions='', priority='essential', frequency='Daily', points=2):
        """Initialize the quest class."""
        self.uuid = uuid4()
        self.name = name
        self.description = description
        self.priority = priority  # 1 (must assign), 2 (assign), 3 (may assign)
        # The days this task occurs
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  
        self.repeat = {day: ['Morning', 'Evening'] for day in self.days}
        self.repeat['Saturday'].append('Noon')
        self.repeat['Sunday'].append('Noon')
        # self.check_off_instructions = check_off_instructions
        # self.age_limit = 0
        # self.last_completed = None
        # self.priority = priority
        # self.frequency = frequency
        self.points = points
        
        self.assign_by_day = assign_by_day  # characters are assigned to this task by certain days
        self.mentor_assignment_by_day = {}
        self.mentee_assignment_by_day = {}
        
        self.last_assigned_to_character = None
        
    def get_mentor_and_mentee_for_day(self, day):
        mentor_uuid = None
        mentee_uuid = None
        if day in self.mentor_assignment_by_day:
            mentor_uuid = self.mentor_assignment_by_day[day]
        if day in self.mentee_assignment_by_day:
            mentee_uuid = self.mentee_assignment_by_day[day]
        return mentor_uuid, mentee_uuid

    def read_quest(self, h5group, uuid):
        # self.short_name = np.array(h5group.get(uuid))[0]
        self.name = h5group[uuid].attrs['name']
        self.description = h5group[uuid].attrs['description']
        self.priority = h5group[uuid].attrs['priority']
        self.recurrence = h5group[uuid].attrs['recurrence']
        self.points = h5group[uuid].attrs['points']
        return self

    def write_quest(self, h5group):
        dt = h5py.string_dtype(encoding='utf-8')
        data = h5group.create_dataset(str(self.uuid), data=self.name, dtype=dt)
        data.attrs['name'] = self.name
        data.attrs['description'] = self.description
        data.attrs['priority'] = self.priority
        data.attrs['recurrence'] = self.recurrence
        data.attrs['points'] = self.points

# uuid
# short name
# description
# essential, important, extra
# way of managing time specific items
# points