"""Class for Character"""
# 1. Standard python libraries
import os
# 2. Third party modules
from docx import Document

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class QuestScribe:
    """Chronicle of fellowships and their quests for a day."""
    def __init__(self, directory):
        """Initialize the character class"""
        self.basename = 'AssignedQuests.docx'
        self.filename = os.path.join(directory, self.basename)
        
    def create_word_document(self, assigned_quests, remaining_quests):
        # Create a new Word document
        doc = Document()

        pageIndex = 1
        for date in assigned_quests:
          if pageIndex != 1:
            doc.add_page_break()
          fellowship_count = 1    
          # Add a title
          doc.add_heading(date.strftime('%A, %B %d, %Y'), level=1)

          for fellowship in assigned_quests[date]:
              doc.add_heading(f'Fellowship {fellowship_count}', level=2)
              fellowship_count += 1
              
              if fellowship.mentor:
                doc.add_heading(fellowship.mentor.first_name, level=3)
                quests = {}
                if fellowship.mentor_daily_quest:
                  quests['Daily'] = fellowship.mentor_daily_quest
                else:
                  quests = fellowship.mentor_quest_schedule
                for schedule in quests:
                  for quest in quests[schedule]:
                    doc.add_paragraph(f'{schedule}: {quest.name}; {quest.description}')
                  
              if fellowship.mentee:
                doc.add_heading(fellowship.mentee.first_name, level=3)
                if fellowship.mentee_daily_quest:
                  quests['Daily'] = fellowship.mentee_daily_quest
                else:
                  quests = fellowship.mentee_quest_schedule
                for schedule in quests:
                  for quest in quests[schedule]:
                    doc.add_paragraph(f'{schedule}: {quest.description}')
                
          doc.add_heading('Remaining Quests', level=2)
          for quest_index in remaining_quests[date]:
            for schedule in remaining_quests[date][quest_index]:
              quest_count = 0
              quest_line = schedule + ': '
              for quest in remaining_quests[date][quest_index][schedule]:
                quest_line += quest.name
                quest_count += 1
              if quest_count > 0:
                doc.add_paragraph(quest_line)
            
          pageIndex += 1

        # Save the document with a specified filename
        doc.save(self.filename)
        print(f"Word document '{self.filename}' created successfully.")

