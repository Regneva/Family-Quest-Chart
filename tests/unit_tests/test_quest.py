"""Tests the Quest class."""
# 1. Standard python libraries
import pytest

# 2. Third party libraries
from family_quest_chart.quest import Quest

# 3. Local libraries

__copyright__ = "(C) Copyright Eric J. Jones 2020"
__license__ = "All rights reserved"


class TestQuest:
    """Tests the Quest class."""

    def test_creating_quest(self):
        new_chore = Quest('sweep floor', 'Sweep the entire kitchen floor', 'edge to edge', 'essential', points=3)

        assert new_chore.name == 'sweep floor', 'Name not properly set'
        assert new_chore.description == 'Sweep the entire kitchen floor', 'description not properly set'
        assert new_chore.check_off_instructions == 'edge to edge', 'check off instructions not properly set'
        assert new_chore.priority == 'essential', 'priority not properly set'
        assert new_chore.points == 3, 'points not properly assigned'

