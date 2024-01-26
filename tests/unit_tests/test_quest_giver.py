# test_quest_giver.py

# 1. Standard python libraries
from datetime import datetime, timedelta
import os
import pytest

# 2. Third party libraries
from docx.enum.text import WD_COLOR
from docx.shared import RGBColor

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
    josh.highlight_color = WD_COLOR.BRIGHT_GREEN
    quest_giver.characters.append(josh)
      
    if miles_kids:
      birthday = datetime.strptime('5/6/06', '%m/%d/%y')
      kenna = Character('Kenna', datetime.date(birthday), 'Mckenna', 'Miles', '')
      kenna.highlight_color = WD_COLOR.TEAL
      kenna.font_color = RGBColor(255, 255, 255)
      quest_giver.characters.append(kenna)
      
    birthday = datetime.strptime('7/6/07', '%m/%d/%y')
    andrew = Character('Andy', datetime.date(birthday), 'Andrew', 'Miles', '')
    andrew.highlight_color = WD_COLOR.DARK_RED
    andrew.font_color = RGBColor(255, 255, 255)
    quest_giver.characters.append(andrew)
      
    if jones_kids:
      birthday = datetime.strptime('3/23/08', '%m/%d/%y')
      miriam = Character('Miriam', datetime.date(birthday), 'Miriam', 'Jones', '')
      miriam.highlight_color = WD_COLOR.RED
      miriam.font_color = RGBColor(255, 255, 255)
      quest_giver.characters.append(miriam)
      
    if miles_kids:
      birthday = datetime.strptime('4/28/09', '%m/%d/%y')
      jon = Character('Jon', datetime.date(birthday), 'Jonathan', 'Miles', '')
      jon.highlight_color = WD_COLOR.DARK_YELLOW
      jon.font_color = RGBColor(255, 255, 255)
      quest_giver.characters.append(jon)
      
    if jones_kids:
      birthday = datetime.strptime('8/11/09', '%m/%d/%y')
      aaron = Character('Aaron', datetime.date(birthday), 'Aaron', 'Jones', '')
      aaron.highlight_color = WD_COLOR.GREEN
      aaron.font_color = RGBColor(255, 255, 255)
      quest_giver.characters.append(aaron)
      
      birthday = datetime.strptime('6/22/11', '%m/%d/%y')
      rachel = Character('Rachel', datetime.date(birthday), 'Rachel', 'Jones', '')
      rachel.highlight_color = WD_COLOR.VIOLET
      rachel.font_color = RGBColor(255, 255, 255)
      quest_giver.characters.append(rachel)
    
    if miles_kids:
      birthday = datetime.strptime('3/17/12', '%m/%d/%y')
      abigail = Character('Abby', datetime.date(birthday), 'Abigail', 'Miles', '')
      abigail.highlight_color = WD_COLOR.TURQUOISE
      quest_giver.characters.append(abigail)
    
    if jones_kids:
      birthday = datetime.strptime('11/22/12', '%m/%d/%y')
      ben = Character('Benj', datetime.date(birthday), 'Benjamin', 'Jones', '')
      ben.highlight_color = WD_COLOR.BLUE
      ben.font_color = RGBColor(255, 255, 255)
      quest_giver.characters.append(ben)
      
      birthday = datetime.strptime('5/10/14', '%m/%d/%y')
      melody = Character('Melody', datetime.date(birthday), 'Melody', 'Jones', '')
      melody.highlight_color = WD_COLOR.PINK
      quest_giver.characters.append(melody)

    if miles_kids:
      birthday = datetime.strptime('2/5/16', '%m/%d/%y')
      ann = Character('Ann', datetime.date(birthday), 'Annelise', 'Miles', '')
      ann.highlight_color = WD_COLOR.YELLOW
      quest_giver.characters.append(ann)
      
    birthday = datetime.strptime('2/18/21', '%m/%d/%y')
    ada = Character('Ada', datetime.date(birthday), 'Ada', 'Jones', '')
    # quest_giver.characters.append(ada)
    
  def create_all_quests(self, quest_giver):
    # Kitchen Chores
    kitchen_font_color = RGBColor(211, 76, 76)
    wash_dishes = Quest('Wash Dishes', 'Wash all dishes and clean around the sink', 1, 4, kitchen_font_color)
    quest_giver.quests.append(wash_dishes)
    clear_counters = Quest('Clear Counters', 'Put away all food, clean all counters and stovetop', 1, 3, kitchen_font_color)
    quest_giver.quests.append(clear_counters)
    unload_dishwasher = Quest('Unload Dishwasher', 'Put away clean dishes near sink and in the dishwasher', 1, 3, kitchen_font_color)
    quest_giver.quests.append(unload_dishwasher)
    floors = Quest('Floors', 'Sweep and mop the kitchen floor', 1, 3, kitchen_font_color)
    quest_giver.quests.append(floors)
    # Pet Chores
    animal_font_color = RGBColor(112, 48, 160)
    chickens = Quest('Chicken Tender', 'Take chicken bucket to chickens, ensure they have food & water, gather eggs', 1, 2, animal_font_color)
    chickens.repeat = {day: ['Morning'] for day in chickens.days}
    quest_giver.quests.append(chickens)
    cat_and_dog = Quest('Cat & Dog', 'Ensure they have food & water (dog at meals), take Dexter out 1st thing and at 8:20 pm', 1, 2, animal_font_color)
    cat_and_dog.repeat = {day: ['Morning'] for day in cat_and_dog.days}
    quest_giver.quests.append(cat_and_dog)
    # Cleaning Chores
    cleaning_font_color = RGBColor(237, 125, 49)
    trash = Quest('Trash', "Empty loft and kitchen garbages; Monday: take to curb (& Hamilton's) and return", 1, 1, cleaning_font_color)
    trash.repeat = {day: ['Morning'] for day in trash.days}
    quest_giver.quests.append(trash)
    upstairs_bathroom = Quest('Clean Upstairs Bathroom', 'Follow list above light-switch', 2, 3, cleaning_font_color)
    upstairs_bathroom.repeat = {day: ['Morning'] for day in upstairs_bathroom.days}
    quest_giver.quests.append(upstairs_bathroom)
    main_bathroom = Quest('Clean Main Bathroom', 'Follow list above light-switch', 2, 3, cleaning_font_color)
    main_bathroom.repeat = {day: ['Morning'] for day in main_bathroom.days}
    quest_giver.quests.append(main_bathroom)
    downstairs_bathroom = Quest('Clean Downstairs Bathroom', 'Follow list above light-switch', 2, 3, cleaning_font_color)
    downstairs_bathroom.repeat = {day: ['Morning'] for day in downstairs_bathroom.days}
    quest_giver.quests.append(downstairs_bathroom)
    vacuum = Quest('Vacuum', 'Vacuum stairs and hallway going up or down and your room.', 2, 3, cleaning_font_color)
    vacuum.repeat = {day: ['Evening'] for day in vacuum.days}
    quest_giver.quests.append(vacuum)
    # Dust, Tidy, & Outside 
    dust_font_color = RGBColor(22, 136, 65)
    loft = Quest('Dust & Tidy Loft', 'Dust, tidy your desk (no loose papers), maintain vacuum', 2, 3, dust_font_color)
    loft.repeat = {day: ['Evening'] for day in loft.days}
    quest_giver.quests.append(loft)
    library = Quest('Dust & Tidy Library', 'Dust & tidy Library, sweep & vacuum Library and main hall', 2, 3, dust_font_color)
    library.repeat = {day: ['Evening'] for day in library.days}
    quest_giver.quests.append(library)
    family_room = Quest('Dust & Tidy Family Room', 'Dust & tidy Family Room & main hall, sweep & vacuum Family Room', 2, 3, dust_font_color)
    family_room.repeat = {day: ['Evening'] for day in family_room.days}
    quest_giver.quests.append(family_room)
    outside = Quest('Outside', 'Take 10 minutes to work outside: Weeds, sweeping, snow-removal', 2, 3, dust_font_color)
    outside.repeat = {day: ['Evening'] for day in outside.days}
    quest_giver.quests.append(outside)
    outside2 = Quest('Outside', 'Take 10 minutes to work outside: Weeds, sweeping, snow-removal', 2, 3, dust_font_color)
    outside2.repeat = {day: ['Evening'] for day in outside2.days}
    quest_giver.quests.append(outside)
    # Laundry
    laundry_font_color = RGBColor(0, 0, 0)
    laundry = Quest('Laundry', 'Sort, wash, dry, fold, and put away clothes.', 1, 3, laundry_font_color, True)
    laundry.mentor_assignment_by_day = {
      'Monday': quest_giver.find_character_by_first_name('Abigail').uuid,
      'Tuesday': quest_giver.find_character_by_first_name('Mckenna').uuid,
      'Wednesday': quest_giver.find_character_by_first_name('Andrew').uuid,
      'Thursday': quest_giver.find_character_by_first_name('Rachel').uuid,
      'Friday': quest_giver.find_character_by_first_name('Aaron').uuid,
      'Saturday': None,
      'Sunday': quest_giver.find_character_by_first_name('Josh').uuid
    }
    laundry.mentee_assignment_by_day = {
      'Monday': quest_giver.find_character_by_first_name('Annelise').uuid,
      'Tuesday': quest_giver.find_character_by_first_name('Miriam').uuid,
      'Wednesday': quest_giver.find_character_by_first_name('Jonathan').uuid,
      'Thursday': quest_giver.find_character_by_first_name('Melody').uuid,
      'Friday': quest_giver.find_character_by_first_name('Benjamin').uuid,
      'Saturday': None,
      'Sunday': None
    }
    quest_giver.quests.append(laundry)
    
  def test_assign_quests_for_the_next_week(self):
      # Test case for a method of the class
    start_day = 1
    num_days = 7
    start_date = datetime.now().date() + timedelta(days=start_day)
    last_date = start_date + timedelta(days=num_days)
  
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
    files_directory = os.path.join(parent_directory, 'files')

    quest_giver = QuestGiver(files_directory)
    
    self.create_all_characters(quest_giver)
    self.create_all_quests(quest_giver)
    
    quest_giver.assign_all_quests(start_date, last_date=last_date)
    
    quest_scribe = QuestScribe(quest_giver.directory)
    quest_scribe.create_word_document(quest_giver.fellowships_with_quests_by_date, quest_giver.remaing_quests)
    
