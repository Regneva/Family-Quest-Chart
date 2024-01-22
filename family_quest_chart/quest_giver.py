"""Class for QuestGiver"""
# 1. Standard python libraries
import copy
from datetime import datetime, timedelta
from uuid import uuid4

# 2. Third party modules
import h5py

# 3. Family modules

# 4. Local modules
from family_quest_chart.quest_fellowship import QuestFellowshipAssignment

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class QuestGiver:
    """Quest giver assigns to quests to characters."""
    def __init__(self, directory):
        """Initialize the quest class."""
        self.characters = []
        self.quests = []
        self.directory = directory
        
        self.characters_to_assign = []
        self.characters_to_be_assigned = []
        self.assigned_fellowships = []

        self.quests_to_assign = []
        self.quests_prioritized = {}
        
        # Final product
        self.fellowships_with_quests_by_date = {}
        self.remaing_quests = {}

        self.roles = []

    def read_all_quests(self, f):
        pass

    def write_all_quests(self, f):
        grp = f.create_group("Quests")
        for quest in self.quests:
            quest.write_quest(grp)

    def read_all_characters(self, f):
        pass
    
    def write_all_characters(self, f):
        pass
    
    def read_file(self, filename='quest_giver.hdf5'):
        with h5py.File(filename, 'r') as f:
            self.read_all_quests(f)
            self.read_all_characters(f)
    
    def write_file(self, filename='quest_giver.hdf5'):
        with h5py.File(filename, 'w') as f:
            self.write_all_quests(f)
            self.write_all_characters(f)

    def sort_people_by_birthday(self, characters):
        return sorted(characters, key=lambda character: datetime.strptime(str(character.birthday), "%Y-%m-%d"))
    
    def assign_all_fellowships(self, date):
        """Assigns all the characters into a fellowship."""
        # Calculate the midpoint of the list
        midpoint = len(self.characters_to_assign) // 2
        # Check if the list has an odd number of people
        if len(self.characters_to_assign) % 2 == 1:
            # If odd, keep the person in the middle
            self.characters_to_be_assigned = self.characters_to_assign[midpoint + 1:]
            self.characters_to_assign = self.characters_to_assign[:midpoint + 1]
        else:
            # If even, drop the second half
            self.characters_to_be_assigned = self.characters_to_assign[midpoint:]
            self.characters_to_assign = self.characters_to_assign[:midpoint]
        for character in self.characters_to_assign:
            self.assign_fellowship_by_prev(character, date)

    def assign_fellowship_by_prev(self, character, date)            :
        for character_to_be in self.characters_to_be_assigned:
            if character.uuid not in character_to_be.fellowship_dict:
                character_to_be.fellowship_dict[character.uuid] = character_to_be.birthday
        characters_sorted = sorted(self.characters_to_be_assigned, key=lambda character_to: 
            datetime.strptime(str(character_to.fellowship_dict[character.uuid]), "%Y-%m-%d"))
        if len(characters_sorted) > 0:
            character2 = characters_sorted[0]
        else:
            character2 = None
        self.assign_fellowship(character, character2, date)
    
    def assign_fellowship(self, character1, character2, date, quest=None):
        new_fellowship = QuestFellowshipAssignment(character1, character2, quest)
        if character1:
            # if character1 in self.characters_to_assign:
            #     self.characters_to_assign.remove(character1)
            if character1 in self.characters_to_be_assigned:
                self.characters_to_be_assigned.remove(character1)
        if character2:
            # if character2 in self.characters_to_assign:
            #     self.characters_to_assign.remove(character2)
            if character2 in self.characters_to_be_assigned:
                self.characters_to_be_assigned.remove(character2)
        if character1 and character2:
            self.find_character_by_uuid(character1.uuid).fellowship_dict[character2.uuid] = date
            self.find_character_by_uuid(character2.uuid).fellowship_dict[character1.uuid] = date
        self.assigned_fellowships.append(new_fellowship)
        
    def find_character_by_uuid(self, uuid):
        return next(char for char in self.characters if char.uuid == uuid)
        
    def prioritize_and_classify_quests(self, day):
        self.quests_prioritized = {}

        for quest in self.quests_to_assign:
            priority = quest.priority
            schedules = quest.repeat[day]

            for schedule in schedules:
                if priority not in self.quests_prioritized:
                    self.quests_prioritized[priority] = {}

                if schedule not in self.quests_prioritized[priority]:
                    self.quests_prioritized[priority][schedule] = []

                self.quests_prioritized[priority][schedule].append(quest)


    def assign_quests_to_fellowships(self, date, priority):
        priority_morning = self.assign_quests_by_schedule(priority, 'morning', date)
        priority_evening = self.assign_quests_by_schedule(priority, 'evening', date)
        priority_noon = self.assign_quests_by_schedule(priority, 'noon', date)
        return min(priority_morning, priority_evening, priority_noon)
            
    def assign_quests_by_schedule(self, priority, schedule, date):
        if schedule not in self.quests_prioritized[priority]:
            return 3
        while len(self.quests_prioritized[priority][schedule]) <= 0:
            priority += 1
        
        for fellowship in self.assigned_fellowships:
            if priority not in self.quests_prioritized:
                return priority
            if schedule not in self.quests_prioritized[priority]:
                return priority
            quests_applicable = self.quests_prioritized[priority][schedule]
            quest = self.find_quest_for_character(quests_applicable, fellowship.mentor)
            if quest:
                if schedule not in fellowship.mentor_quest_schedule:
                    fellowship.mentor_quest_schedule[schedule] = []
                fellowship.mentor_quest_schedule[schedule].append(quest)
                fellowship.mentor.quest_last_assigned[quest.uuid] = date                
                self.quests_prioritized[priority][schedule].remove(quest)
                if len(self.quests_prioritized[priority][schedule]) == 0:
                    priority += 1
                    if priority not in self.quests_prioritized:
                        return priority
                    if schedule not in self.quests_prioritized[priority]:
                        return priority
                    quests_applicable = self.quests_prioritized[priority][schedule]
                
            while len(self.quests_prioritized[priority]) <= 0:
                priority += 1
            
            quest = self.find_quest_for_character(quests_applicable, fellowship.mentee)
            if quest:
                if schedule not in fellowship.mentee_quest_schedule:
                    fellowship.mentee_quest_schedule[schedule] = []
                fellowship.mentee_quest_schedule[schedule].append(quest)
                fellowship.mentee.quest_last_assigned[quest.uuid] = date                
                self.quests_prioritized[priority][schedule].remove(quest)
                if len(self.quests_prioritized[priority][schedule]) == 0:
                    priority += 1
            
        return priority
            
    def find_quest_for_character(self, quests_applicable, character):
        if len(quests_applicable) <= 0:
            return None
        quest_last_assigned = character.quest_last_assigned
        for quest in quests_applicable:
            if quest.uuid in quest_last_assigned:
                quest.last_assigned_to_character = quest_last_assigned[quest.uuid]
            else:
                quest.last_assigned_to_character = character.birthday
        sorted_quests = sorted(quests_applicable, key=lambda quest: 
            datetime.strptime(str(quest.last_assigned_to_character), "%Y-%m-%d"))
        return sorted_quests[0]

    def assign_all_quests_for_day(self, date):
        day = date.strftime('%A')
        self.characters_to_assign = self.sort_people_by_birthday(self.characters)
        self.assigned_fellowships = []
        
        # First gather and assign the quests that are assigned daily
        daily_quests = [quest for quest in self.quests if quest.assign_by_day]
        for daily_quest in daily_quests:
            mentor, mentee = daily_quest.get_mentor_and_mentee_for_day(day)
            if mentor or mentee:
                self.assign_fellowship(mentor, mentee, date, daily_quest)
                
        # Assign mentors by birthdate
        self.assign_all_fellowships(date)
        
        # Determine quests to assign based on priority
        self.quests_to_assign = [quest for quest in self.quests if day in quest.days]
        self.prioritize_and_classify_quests(day)
        
        # Assign the quests
        priority = 1
        while priority <= 1:
            priority = self.assign_quests_to_fellowships(date, priority)
    
    def assign_all_quests(self, last_date):
        current_date = datetime.now().date()
        while current_date <= last_date:
            self.assign_all_quests_for_day(current_date)
            self.fellowships_with_quests_by_date[current_date] = self.assigned_fellowships
            self.remaing_quests[current_date] = self.quests_prioritized
            current_date += timedelta(days=1)

    def compute_data(self):
        self.read_all_quests()
        self.read_all_characters()
        # self.assign_all_quests()
