import random
import pygame
from settings import *
from .categories import *

def task_(task_count):
    random_number = random.randint(1, 10)
    if task_count % 5 == 0:
        category = Virus()

    elif random_number == 2:
        category = Luck()

    elif random_number == 3:
        category = Punishment()
    
    elif random_number == 4:
        category = Quiz()

    else: 
        category = Quest()
    
    return category


def next_task(selected_player, task_count):
    # Select the category
    category = task_(task_count)


    start_screen_background = category.theme
    selected_task = category.get_task()
    punishment = category.shots
    punishment_display = category.punish
    task_type = category.type

    ##### Display quest icon #####
    icon = pygame.image.load(f'ui/icons/{task_type}.png')
    icon_width, icon_height = icon.get_size()
    x = (SCREEN_WIDTH - icon_width) // 2
    y = (SCREEN_HEIGHT - icon_height) // 8
    SCREEN.blit(icon, (x, y))

    # Define task and lower fond if string is too long
    if len(selected_task) > 55:
        task_text = FONT_1.render((str(selected_player) + str(selected_task)), True, BLACK)
    else:
        task_text = FONT_2.render((str(selected_player) + str(selected_task)), True, BLACK)
    
    ##### Display text in the middle of the screen #####
    quest_width, quest_height = task_text.get_size()
    x = (SCREEN_WIDTH - quest_width) // 2
    y = (SCREEN_HEIGHT - quest_height) // 2
    SCREEN.blit(task_text, (x, y))

    # Display punishment if needed
    if punishment_display == True:

        # Define and display or
        or_text = FONT_2.render('or', True, BLACK)
        or_width, or_height = or_text.get_size()
        x = (SCREEN_WIDTH - or_width) // 2
        y = (SCREEN_HEIGHT - or_height) // 2
        SCREEN.blit(or_text, (x, y+75))

        # Define and display punishment
        punishment_text = FONT_2.render('Take ' + str(punishment) + ' shot(s)', True, BLACK)
        punishment_width, punishment_height = punishment_text.get_size()
        x = (SCREEN_WIDTH - punishment_width) // 2
        y = (SCREEN_HEIGHT - punishment_height) // 2 
        SCREEN.blit(punishment_text, (x, y+150))
