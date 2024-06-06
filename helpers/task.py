import random
import pygame
from settings import *
from .categories import *

def task_(screen, task_count, select_player, ):

    random_number = random.randint(1, 10)
    if task_count % 5 == 0:
        category = Virus(screen)

    elif random_number == 2:
        category = Luck(screen)

    elif random_number == 3:
        category = Punishment(screen)
    
    elif random_number == 4:
        category = Quiz(screen)

    else: 
        category = Quest(screen)
    
    return category

