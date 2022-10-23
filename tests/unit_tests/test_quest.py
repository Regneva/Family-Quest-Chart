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
        dir_path = os.path.dirname(os.path.realpath(__file__))
        basename = 'test_writing_quest.hdf5'
        file = os.path.join(dir_path, '..', 'files', 'test_writing_quest', 'out', basename)
        with h5py.File(file, 'w') as quest_file:
            grp = quest_file.create_group("Quests")
            new_chore.write_quest(grp)

    def test_reading_quest(self):
        new_chore = self.test_creating_quest()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        basename = 'test_reading_quest.hdf5'
        file = os.path.join(dir_path, '..', 'files', 'test_reading_quest', 'base', basename)
        with h5py.File(file, 'r') as quest_file:
            grp = quest_file["Quests"]
            quests_uuids = grp.keys()

            quests = []
            for uuid in quests_uuids:
                read_quest = Quest().read_quest(grp, uuid)
                quests.append(read_quest)

        if len(quests) != 1:
            self.assertTrue(False, "Number of quests read was wrong!")
            return False

        read_quest = quests[0]

        if read_quest.short_name == new_chore.short_name:
            if read_quest.description == new_chore.description:
                if read_quest.points == new_chore.points:
                    return True

            self.assertTrue(False, "quest that was read does not match created quest!")
            return False

