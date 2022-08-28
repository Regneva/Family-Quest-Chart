"""Tests the Quest class."""
# 1. Standard python libraries
import pytest

# 2. Third party libraries
from family_quest_chart.character import Character

# 3. Local libraries

__copyright__ = "(C) Copyright Eric J. Jones 2020"
__license__ = "All rights reserved"


class TestCharacter:
    """Tests the Quest class."""

    def test_creating_quest(self):
        new_character = Character('Studiosfir3917', first_name='Aaron', last_name='Jones',
                                  email='studiosfir3917@gmail.com', points=0, inventory=[])

