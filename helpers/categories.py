import random

from random import shuffle

from settings import *

# Import the task per categorie
def import_categories(categorie):

    with open(f"./categories/{categorie}.txt") as task:
        task_list = task.read().splitlines()
        shuffle(task_list)
        return task_list

class Luck:
    def __init__(self):

        self.colour = YELLOW
        self.type = 'luck'
        self.shots = random.randint(1, 3)
        self.theme = SCREEN.fill(self.colour) # Yellow
        self.punish = False
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('luck')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task

class Punishment:
    def __init__(self):

        self.colour = RED
        self.type = 'punishment'
        self.shots = random.randint(1, 3)
        self.theme = SCREEN.fill(self.colour) #Red
        self.punish = True
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('punishment')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task
    
class Quiz:
    def __init__(self):

        self.colour = BLUE
        self.type = 'quiz'
        self.shots = random.randint(1, 3)
        self.theme = SCREEN.fill(self.colour) #Blue
        self.punish = True
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('quiz')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task
    
class Quest:
    def __init__(self):

        self.colour = ORANGE
        self.type = 'task'
        self.shots = random.randint(1, 8)
        self.theme = SCREEN.fill(self.colour) #Turqoise
        self.punish = True
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('quest')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task
    
class Virus:
    def __init__(self):

        self.colour = GREEN
        self.type = 'virus'
        self.shots = random.randint(1, 8)
        self.theme = SCREEN.fill(self.colour) #Green
        self.punish = True
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('virus')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task

