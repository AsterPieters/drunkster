import random
from .categories import Virus, Luck, Punishment, Quiz, Task

def task_(screen, task_index):

    random_number = random.randint(1, 10)
    task_index += 1

    if task_index % 5 == 0:
        category = Virus(screen)

    elif random_number == 2:
        category = Luck(screen)

    elif random_number == 3:
        category = Punishment(screen)
    
    elif random_number == 4:
        category = Quiz(screen)

    else: 
        category = Task(screen)
    
    return category, task_index