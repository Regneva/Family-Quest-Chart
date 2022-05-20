"""Tests the Quest class."""
# 1. Standard python libraries
import unittest

# 2. Third party libraries
from family_quest_chart.quest import Quest

# 3. Local libraries

__copyright__ = "(C) Copyright Eric J. Jones 2020"
__license__ = "All rights reserved"


class TestQuest(unittest.TestCase):
    """Tests the Quest class."""

    def test_creating_quest(self):
        new_chore = Quest('sweep floor', 'Sweep the entire kitchen floor, edge to edge.', points=3)

