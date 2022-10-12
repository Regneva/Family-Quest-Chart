"""Tests the Quest class."""
# 1. Standard python libraries
import os
import unittest

# 2. Third party libraries
from family_quest_chart.quest import Quest
import h5py

# 3. Local libraries

__copyright__ = "(C) Copyright Eric J. Jones 2020"
__license__ = "All rights reserved"


class TestQuest(unittest.TestCase):
    """Tests the Quest class."""

    def test_creating_quest(self):
        new_chore = Quest('sweep floor', 'Sweep the entire kitchen floor, edge to edge.', points=3)
        return new_chore

    def test_writing_quest(self):
        new_chore = self.test_creating_quest()
        basename = 'test_writing_quest.hdf5'
        file = os.path.join('files', 'test_writing_quest', 'out', basename)
        with h5py.File(file, 'w') as quest_file:
            grp = quest_file.create_group("Quests")
            new_chore.write_quest(grp)
