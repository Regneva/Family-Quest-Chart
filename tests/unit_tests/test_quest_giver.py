# test_quest_giver.py

# 1. Standard python libraries
from datetime import datetime, timedelta
import os
import pytest

# 2. Third party libraries

# 3. Local libraries
from family_quest_chart.character import Character
from family_quest_chart.quest import Quest
from family_quest_chart.quest_giver import QuestGiver
from family_quest_chart.quest_scribe import QuestScribe

__copyright__ = "(C) Copyright Eric J. Jones 2020"
__license__ = "All rights reserved"


# Example of a test class
class TestQuestGiver:
  def setup_method(self):
      # Setup code that runs before each test method
    pass

  def teardown_method(self):
      # Teardown code that runs after each test method
    pass

  def test_initialization(self):
      # Test case for object initialization
    pass
  
  def create_all_characters(self, quest_giver):
    miles_kids = True
    jones_kids = True
    
    birthday = datetime.strptime('3/2/04', '%m/%d/%y')
    josh = Character('Josh', datetime.date(birthday), 'Josh', 'Miles', '')
    quest_giver.characters.append(josh)
      
    if miles_kids:
      birthday = datetime.strptime('5/6/06', '%m/%d/%y')
      kenna = Character('Kenna', datetime.date(birthday), 'Mckenna', 'Miles', '')
      quest_giver.characters.append(kenna)
      
    birthday = datetime.strptime('7/6/07', '%m/%d/%y')
    andrew = Character('Andy', datetime.date(birthday), 'Andrew', 'Miles', '')
    quest_giver.characters.append(andrew)
      
    if jones_kids:
      birthday = datetime.strptime('3/23/08', '%m/%d/%y')
      miriam = Character('Miriam', datetime.date(birthday), 'Miriam', 'Jones', '')
      quest_giver.characters.append(miriam)
      
    if miles_kids:
      birthday = datetime.strptime('4/28/09', '%m/%d/%y')
      jon = Character('Jon', datetime.date(birthday), 'Jonathan', 'Miles', '')
      quest_giver.characters.append(jon)
      
    if jones_kids:
      birthday = datetime.strptime('8/11/09', '%m/%d/%y')
      aaron = Character('Aaron', datetime.date(birthday), 'Aaron', 'Jones', '')
      quest_giver.characters.append(aaron)
      
      birthday = datetime.strptime('6/22/11', '%m/%d/%y')
      rachel = Character('Rachel', datetime.date(birthday), 'Rachel', 'Jones', '')
      quest_giver.characters.append(rachel)
    
    if miles_kids:
      birthday = datetime.strptime('3/17/12', '%m/%d/%y')
      abigail = Character('Abby', datetime.date(birthday), 'Abigail', 'Miles', '')
      quest_giver.characters.append(abigail)
    
    if jones_kids:
      birthday = datetime.strptime('11/22/12', '%m/%d/%y')
      ben = Character('Benj', datetime.date(birthday), 'Benjamin', 'Jones', '')
      quest_giver.characters.append(ben)
      
      birthday = datetime.strptime('5/10/14', '%m/%d/%y')
      melody = Character('Melody', datetime.date(birthday), 'Melody', 'Jones', '')
      quest_giver.characters.append(melody)

    if miles_kids:
      birthday = datetime.strptime('2/5/16', '%m/%d/%y')
      ann = Character('Ann', datetime.date(birthday), 'Annelise', 'Miles', '')
      quest_giver.characters.append(ann)
      
    birthday = datetime.strptime('2/18/21', '%m/%d/%y')
    ada = Character('Ada', datetime.date(birthday), 'Ada', 'Jones', '')
    # quest_giver.characters.append(ada)
    
  def create_all_quests(self, quest_giver):
    # Kitchen Chores
    wash_dishes = Quest('Wash Dishes', 'Wash all dishes and clean around the sink', 1, 4)
    quest_giver.quests.append(wash_dishes)
    clear_counters = Quest('Clear Counters', 'Put away all food, clean all counters and stovetop', 1, 3)
    quest_giver.quests.append(clear_counters)
    unload_dishwasher = Quest('Unload Dishwasher', 'Put away clean dishes near sink and in the dishwasher', 1, 3)
    quest_giver.quests.append(unload_dishwasher)
    # Pet Chores
    chickens = Quest('Chicken Tender', 'Take chicken bucket to chickens, ensure they have food & water, gather eggs', 1, 2)
    chickens.repeat = {day: ['morning'] for day in chickens.days}
    quest_giver.quests.append(chickens)
    cat_and_dog = Quest('Cat & Dog', 'Ensure they have food & water (dog at meals), take Dexter out 1st thing and at 8:20 pm', 1, 2)
    cat_and_dog.repeat = {day: ['morning'] for day in cat_and_dog.days}
    quest_giver.quests.append(cat_and_dog)
    # Cleaning Chores
    trash = Quest('Trash', 'Empty loft and kitchen garbages; on Monday, take garbages to curb', 1, 1)
    quest_giver.quests.append(trash)
    cat_and_dog.repeat = {day: ['morning'] for day in cat_and_dog.days}
    upstairs_bathroom = Quest('Upstairs Bathroom', 'Clean upstairs bathroom', 2, 3)
    upstairs_bathroom.repeat = {day: ['morning'] for day in upstairs_bathroom.days}
    quest_giver.quests.append(upstairs_bathroom)
    downstairs_bathroom = Quest('Downstairs Bathroom', 'Clean downstairs bathroom', 2, 3)
    downstairs_bathroom.repeat = {day: ['morning'] for day in downstairs_bathroom.days}
    quest_giver.quests.append(downstairs_bathroom)
    vacum = Quest('Vacum', 'Vacum one room', 2, 3)
    vacum.repeat = {day: ['evening'] for day in vacum.days}
    quest_giver.quests.append(vacum)
    outside = Quest('Outside', 'Take 10 minutes to work outside: Weeds, sweeping, snow-removal', 2, 3)
    outside.repeat = {day: ['evening'] for day in outside.days}
    quest_giver.quests.append(outside)
    outside2 = Quest('Outside', 'Take 10 minutes to work outside: Weeds, sweeping, snow-removal', 2, 3)
    outside2.repeat = {day: ['evening'] for day in outside2.days}
    quest_giver.quests.append(outside)

  def test_assign_quests_for_the_next_week(self):
      # Test case for a method of the class
    last_date = datetime.now().date() + timedelta(weeks=1)
  
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
    files_directory = os.path.join(parent_directory, 'files')

    quest_giver = QuestGiver(files_directory)
    
    self.create_all_characters(quest_giver)
    self.create_all_quests(quest_giver)
    
    quest_giver.assign_all_quests(last_date=last_date)
    
    quest_scribe = QuestScribe(quest_giver.directory)
    quest_scribe.create_word_document(quest_giver.fellowships_with_quests_by_date, quest_giver.remaing_quests)
    
