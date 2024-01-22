"""Class for Quest"""
# 1. Standard python libraries
from uuid import uuid4

# 2. Third party modules
import h5py

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class Quest:
    """Quest is the chore."""
    # def __init__(self, short_name='', description='', priority='essential', recurrance='daily', 
    #              points=2, assign_by_day=False):
    def __init__(self, short_name='', description='', priority=1, 
                 points=2, assign_by_day=False):
        """Initialize the quest class."""
        self.uuid = uuid4()
        self.short_name = short_name
        self.description = description
        self.priority = priority  # 1 (must assign), 2 (assign), 3 (may assign)
        # The days this task occurs
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  
        self.repeat = {day: ['morning', 'evening'] for day in self.days}
        self.repeat['Saturday'].append('noon')
        self.repeat['Sunday'].append('noon')
        self.points = points
        
        self.assign_by_day = assign_by_day  # characters are assigned to this task by certain days
        self.mentor_assignment_by_day = {}
        self.mentee_assignment_by_day = {}
        
        self.last_assigned_to_character = None
        
    def get_mentor_and_mentee_for_day(self, day):
        mentor = None
        mentee = None
        if day in self.mentor_assignment_by_day:
            mentor = self.mentor_assignment_by_day[day]
        if day in self.mentee_assignment_by_day:
            mentee = self.mentee_assignment_by_day[day]
        return mentor, mentee

    def read_quest(self, h5file):
        pass

    def write_quest(self, h5group):
        dt = h5py.string_dtype(encoding='utf-8')
        data = h5group.create_dataset(self.uuid, data=self.short_name, dtype=dt)
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