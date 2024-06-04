import random

# Import the task per categorie
def import_categories(categorie):

    with open(f"./categories/{categorie}.txt") as task:
        task_list = task.read().splitlines()
        return task_list



class Luck:
    def __init__(self, screen):

        self.colour = (255, 255, 0)
        self.type = 'luck'
        self.shots = random.randint(1, 3)
        self.theme = screen.fill(self.colour) # Yellow
        self.punish = False
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('luck')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task



class Punishment:
    def __init__(self, screen):

        self.colour = (255, 0, 0)
        self.type = 'punishment'
        self.shots = random.randint(1, 3)
        self.theme = screen.fill(self.colour) #Red
        self.punish = True
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('punishment')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task
    


class Quiz:
    def __init__(self, screen):

        self.colour = (0, 0, 255)
        self.type = 'quiz'
        self.shots = random.randint(1, 3)
        self.theme = screen.fill(self.colour) #Blue
        self.punish = True
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('quiz')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task
    


class Quest:
    def __init__(self, screen):

        self.colour = (0, 255, 255)
        self.type = 'task'
        self.shots = random.randint(1, 8)
        self.theme = screen.fill(self.colour) #Turqoise
        self.punish = True
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('quest')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task
    


class Virus:
    def __init__(self, screen):

        self.colour = (0, 255, 0)
        self.type = 'virus'
        self.shots = random.randint(1, 8)
        self.theme = screen.fill(self.colour) #Green
        self.punish = True
        self.tasks = []

    def get_task(self):

        if not self.tasks:
            self.tasks = import_categories('virus')

        selected_task = self.tasks[0]
        self.tasks.pop()
        return selected_task