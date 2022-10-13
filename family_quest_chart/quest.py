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
    def __init__(self, short_name='', description='', priority='essential', recurrance='daily', points=2):
        """Initialize the quest class."""
        self.uuid = uuid4()
        self.short_name = short_name
        self.description = description
        self.priority = priority
        self.recurrence = recurrance
        self.points = points

    def read_quest(self, h5group, uuid):
        # self.short_name = np.array(h5group.get(uuid))[0]
        self.short_name = h5group[uuid].attrs['short_name']
        self.description = h5group[uuid].attrs['description']
        self.priority = h5group[uuid].attrs['priority']
        self.recurrence = h5group[uuid].attrs['recurrence']
        self.points = h5group[uuid].attrs['points']
        return self

    def write_quest(self, h5group):
        dt = h5py.string_dtype(encoding='utf-8')
        data = h5group.create_dataset(str(self.uuid), data=self.short_name, dtype=dt)
        data.attrs['short_name'] = self.short_name
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