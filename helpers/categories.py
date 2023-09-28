import random


##### Imports Lines and puts them in a list #####
def import_categories(categorie):

    with open(f"./categories/{categorie}.txt") as quest:
        quest_list = quest.read().splitlines()
        return quest_list



class Luck:
    def __init__(self, screen):

        self.colour = (255, 255, 0)
        self.type = 'luck'
        self.shots = random.randint(1, 3)
        self.theme = screen.fill(self.colour) # Yellow
        self.punish = False
        self.quests = []

    def get_quest(self):

        if not self.quests:
            self.quests = import_categories('luck')

        selected_quest = self.quests[0]
        self.quests.pop()
        return selected_quest



class Punishment:
    def __init__(self, screen):

        self.colour = (255, 0, 0)
        self.type = 'punishment'
        self.shots = random.randint(1, 3)
        self.theme = screen.fill(self.colour) #Red
        self.punish = True
        self.quests = []

    def get_quest(self):

        if not self.quests:
            self.quests = import_categories('punishment')

        selected_quest = self.quests[0]
        self.quests.pop()
        return selected_quest
    


class Quiz:
    def __init__(self, screen):

        self.colour = (0, 0, 255)
        self.type = 'quiz'
        self.shots = random.randint(1, 3)
        self.theme = screen.fill(self.colour) #Blue
        self.punish = True
        self.quests = []

    def get_quest(self):

        if not self.quests:
            self.quests = import_categories('quiz')

        selected_quest = self.quests[0]
        self.quests.pop()
        return selected_quest
    


class Task:
    def __init__(self, screen):

        self.colour = (0, 255, 255)
        self.type = 'task'
        self.shots = random.randint(1, 8)
        self.theme = screen.fill(self.colour) #Turqoise
        self.punish = True
        self.quests = []

    def get_quest(self):

        if not self.quests:
            self.quests = import_categories('task')

        selected_quest = self.quests[0]
        self.quests.pop()
        return selected_quest
    


class Virus:
    def __init__(self, screen):

        self.colour = (0, 255, 0)
        self.type = 'virus'
        self.shots = random.randint(1, 8)
        self.theme = screen.fill(self.colour) #Green
        self.punish = True
        self.quests = []

    def get_quest(self):

        if not self.quests:
            self.quests = import_categories('virus')

        selected_quest = self.quests[0]
        self.quests.pop()
        return selected_quest