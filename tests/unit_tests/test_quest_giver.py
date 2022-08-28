"""Tests the quest_giver class."""
# 1. Standard python libraries
import pytest

# 2. Third party libraries
from family_quest_chart.quest_giver import QuestGiver

# 3. Local libraries

__copyright__ = "(C) Copyright Eric J. Jones 2020"
__license__ = "All rights reserved"


class TestQuestGiver():
    """Tests the quest_giver class."""

    def test_listing_present(self):
        quest_giver = QuestGiver()

        quest_giver.add_character()