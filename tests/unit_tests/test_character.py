"""Tests the Quest class."""
# 1. Standard python libraries
import os
import pytest

# 2. Third party libraries
import h5py
from family_quest_chart.character import Character

# 3. Local libraries

__copyright__ = "(C) Copyright Eric J. Jones 2020"
__license__ = "All rights reserved"


class TestCharacter:
    """Tests the Quest class."""

    def test_creating_character(self):
        new_character = Character('Studiosfir3917', first_name='Aaron', last_name='Jones',
                                  email='studiosfir3917@gmail.com', points=0, inventory=[])
        return new_character

    def test_writing_character(self):
        new_character = self.test_creating_character()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        basename = 'test_writing_character.hdf5'
        file = os.path.join(dir_path, '..', 'files', 'test_writing_character', 'out', basename)
        with h5py.File(file, 'w') as character_file:
            grp = character_file.create_group("Character")
            new_character.write_character(grp)

    def test_read_character(self):
        new_character = self.test_creating_character()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        basename = 'test_read_character.hdf5'
        file = os.path.join(dir_path, '..', 'files', 'test_read_character', 'base', basename)
        with h5py.File(file, 'r') as character_file:
            grp = character_file["Character"]
            character_uuids = grp.keys()