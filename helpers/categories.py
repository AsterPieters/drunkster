from settings import *
import random
from random import shuffle

# Import the task per categorie
def import_categories(categorie):

    with open(f"./categories/{categorie}.txt") as task:
        task_list = task.read().splitlines()
        shuffle(task_list)
        return task_list
    
class Categorie():
    """Represents the categories of the tasks"""

    def __init__(self, colour, type, punish, max_shots):
        self.colour = colour
        self.type = type
        self.punish = punish
        self.punishment = random.randint(1, max_shots)
        self.tasks = []

    def get_task(self):
        if not self.tasks:
            self.tasks = import_categories(self.type)
            print("Getting new tasks!")

        selected_task = self.tasks[0]
        self.tasks.pop(0)
        return selected_task

    def display_task(self, selected_player):

        # Get task
        selected_task = self.get_task()

        # Fill the screen
        self.theme = SCREEN.fill(self.colour)

        # ##### Display quest icon #####
        # icon = pygame.image.load(f'ui/icons/{self.type}.png')
        # icon_width, icon_height = icon.get_size()
        # x = (SCREEN_WIDTH - icon_width) // 2
        # y = (SCREEN_HEIGHT - icon_height) // 5
        # SCREEN.blit(icon, (x, y))

        # Define task and lower fond if string is too long
        if len(selected_task) > 55:
            task_text = FONT_1.render((str(selected_player) + str(selected_task)), True, BLACK)
        else:
            task_text = FONT_2.render((str(selected_player) + str(selected_task)), True, BLACK)
        
        ##### Display text in the middle of the screen #####
        quest_width, quest_height = task_text.get_size()
        x = (SCREEN_WIDTH - quest_width) // 2
        y = (SCREEN_HEIGHT - quest_height) // 2.5
        SCREEN.blit(task_text, (x, y))

        # Display punishment if needed
        if self.punish == True:

            # Define and display or
            or_text = FONT_2.render('or', True, BLACK)
            or_width, or_height = or_text.get_size()
            x = (SCREEN_WIDTH - or_width) // 2
            y = (SCREEN_HEIGHT - or_height) // 2.5
            SCREEN.blit(or_text, (x, y+75))

            # Define and display punishment
            punishment_text = FONT_2.render('Take ' + str(self.punishment) + ' shot(s)', True, BLACK)
            punishment_width, punishment_height = punishment_text.get_size()
            x = (SCREEN_WIDTH - punishment_width) // 2
            y = (SCREEN_HEIGHT - punishment_height) // 2.5
            SCREEN.blit(punishment_text, (x, y+150))

class Tasker():
    def __init__(self):

        # Create categories
        self.luck = Categorie(YELLOW, 'luck', False, 3)
        self.punishment = Categorie(RED, 'punishment', True, 3)
        self.quiz = Categorie(ORANGE, 'quiz', True, 3)
        self.quest = Categorie(BLUE, 'quest', True, 8)
        self.virus = Categorie(GREEN, 'virus', True, 8)
    
    def next_task(self, select_player, task_count):
        # Randomly get category
        random_number = random.randint(1, 10)
        if task_count % 5 == 0:
            category = self.virus.display_task(select_player)

        elif random_number == 2:
            category = self.luck.display_task(select_player)

        elif random_number == 3:
            category = self.punishment.display_task(select_player)
        
        elif random_number == 4:
            category = self.quiz.display_task(select_player)

        else: 
            category = self.quest.display_task(select_player)