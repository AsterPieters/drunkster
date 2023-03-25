# Drunkster, Get drunk or DIE!
# A drinking game by Aster Pieters

# Imports
import pygame
import random
import time

# Initializing pygame
pygame.init()


""""
This part of the code is for the start screen.

"""


# Define resolution
screen_width=1535
screen_height=715
player_width = 500

# Define colors
white = (255, 255, 255)
light_gray = (205, 205, 205)
gray = (50, 50, 50)
dark_gray = (150, 150, 150)
black = (0, 0, 0)
red = (255, 0, 0)
dark_red = (155, 0, 0)
light_blue = (188, 218, 255)
blue = (143, 189, 255)
dark_brown = (104, 59, 1)
yellow = (225, 225, 31)
green = (133, 217, 37)
dark_green = (205, 255, 157)
turqoise = (37, 183, 217)
purple = (158, 37, 217)

# Define fonts
font_1 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 50)
font_2 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 80)
font_3 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 150)
font_4 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 25)
font_5 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 50)
font_6 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 35)

# Add player to list function
player_list = ['test1', 'test2']

# Define "enter a player" text
enter_player_text = font_1.render('Enter a player:', True, black)
title_top_text = font_3.render('Drunkster', True, black)
title_bottom_text = font_2.render('Get drunk or DIE', True, black)

# Define enter player textbox & Rectangle
enter_player_textbox_rect = pygame.Rect(365, 516, 200, 60)
active = False
enter_player_textbox_input = ''
error_code = ''

# Define added players text
added_players_text = font_4.render('Players: ', True, black)

def add_player_func():

    error_code = ''
    if enter_player_textbox_input == '':
        error_code = "Please enter a name!"
        return error_code
    elif len(enter_player_textbox_input) > 8:
        error_code = "Please use 8 or less charachters!"
        return error_code
    elif enter_player_textbox_input in player_list:
        player_list.remove(enter_player_textbox_input)
    else:
        player_list.append(enter_player_textbox_input)

# Define display
screen = pygame.display.set_mode([screen_width, screen_height])

# Stores the width & height into variables
width = screen.get_width()
height = screen.get_height()

# Inializing start screen
start_screen_running = True
game_screen_running = False
while start_screen_running:

    # Fills the background
    bg = pygame.image.load('ui/images/bar.png')
    screen.blit(bg, (0,0))

    # Ends loop when quit window button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_screen_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if enter_player_textbox_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        # Checks for textbox events
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                enter_player_textbox_input = enter_player_textbox_input[:-1]

            # Unicode standard is used for string formation
            else:
                enter_player_textbox_input += event.unicode

        # Checks for textbox events
        if event.type == pygame.KEYDOWN:

            # Checks for enters
            if event.key == pygame.K_RETURN:
                enter_player_textbox_input = enter_player_textbox_input[:-1]
                error_code = add_player_func()
                enter_player_textbox_input = ''

        
        # For events that occur upon clicking the mouse (left click)
        mouse = pygame.mouse.get_pos()
        #print(mouse)                                                                                   # DELETE TO DISPLAY MOUSE LOCATION
        if event.type == pygame.MOUSEBUTTONDOWN:
              if 20 <= mouse[0] <= 380 and 470 <= mouse[1] <= 510:
                if len(player_list) < 2:
                    error_code = 'Please add at least 2 players!'
                else:
                    game_screen_running = True
                    start_screen_running = False
                    pygame.display.update()
        
        # Changes color when hovering over start game button
        if 20 <= mouse[0] <= 380 and 470 <= mouse[1] <= 510:
            start_game_text = font_1.render('Start Drunkster' , True , gray)
        else:
            start_game_text = font_1.render('Start Drunkster' , True , black)

    # Display error
    error_text = font_1.render(error_code, True, red)
    screen.blit(error_text, (400, 640))

    # Display left plank
    left_plank = pygame.image.load('ui/images/left_plank.png')
    screen.blit(left_plank, (5, 437))

    for player in player_list:
        if player == 'Marc' or player == 'marc':
        # Display Marc
            marc = pygame.image.load('ui/images/marc.png')
            screen.blit(marc, (1200, 120))

    # Display right plank
    left_plank = pygame.image.load('ui/images/right_plank.png')
    screen.blit(left_plank, (1169, 344))

    # Set the pygame window name
    pygame.display.set_caption('Drunkster')

    # Displays text
    screen.blit(enter_player_text, (20, 520))
    screen.blit(title_top_text, (440, 0))
    screen.blit(title_bottom_text, (480, 135))

    # Displays "Add player" textbox
    text_surface = font_1.render(enter_player_textbox_input, True, (black))
    screen.blit(text_surface, (380, 520))

    # Displays "Start Drunkster" button
    screen.blit(start_game_text , (20, 460))

    # Display added players text & rectangle
    screen.blit(added_players_text, (1200, 400))
    
    # Displays the players
    for player in player_list:
        player_list_text = font_1.render(player, True, black)
        screen.blit(font_4.render(player, True, black), (1300 , 400 + (25 * player_list.index(player))))

    # Update the display
    pygame.display.update()


"""
This part of the code is for the game screen

"""

# Puts default background
start_screen_background = screen.fill(turqoise)


# Imports the tasks
def single_user_task_func():
    # Gets the lines out of the single_user_tasks file and puts them in a list
    with open('ui/tasks/single_user_tasks') as task:
        single_user_tasks_list = task.read().splitlines()
        random.shuffle(single_user_tasks_list)
        return single_user_tasks_list

def virus_tasks_func():
    # Gets the lines out of the virus file and puts them in a list
    with open('ui/tasks/virus_tasks') as task:
        virus_tasks_list = task.read().splitlines()
        random.shuffle(virus_tasks_list)
        return virus_tasks_list
    
def luck_tasks_func():
    # Gets the lines out of the luck file and puts them in a list
    with open('ui/tasks/luck_tasks') as task:
        luck_tasks_list = task.read().splitlines()
        random.shuffle(luck_tasks_list)
        return luck_tasks_list
    
def punish_tasks_func():
    # Gets the lines out of the punish file and puts them in a list
    with open('ui/tasks/punish_tasks') as task:
        punish_tasks_list = task.read().splitlines()
        random.shuffle(punish_tasks_list)
        return punish_tasks_list
    
def quiz_tasks_func():
    # Gets the lines out of the single_user_tasks file and puts them in a list
    with open('ui/tasks/quiz_tasks') as task:
        quiz_tasks_list = task.read().splitlines()
        random.shuffle(quiz_tasks_list)
        return quiz_tasks_list
    
# Calls function to put tasks into the lists
single_user_tasks_list = single_user_task_func()
virus_tasks_list = virus_tasks_func()
luck_tasks_list = luck_tasks_func()
punish_tasks_list = punish_tasks_func()
quiz_tasks_list = quiz_tasks_func()

# Initiate the variables
selected_task = 'Press enter to start the first round.'
selected_player = ''
previous_player = ''
task_count = 0
punishment = ''
click = 0

# Define manage player function
enter_player_textbox_rect = pygame.Rect(365, 516, 200, 60)
active = False
enter_player_textbox_input = ''
error_code = ''

# Define options bar
options_bar_rect = pygame.Rect(365, 516, 200, 60)

def task_func():

    task_type = random.randint(1, 10)

    global single_user_tasks_list, virus_tasks_list, luck_tasks_list, punish_tasks_list, quiz_tasks_list

    # Virus
    if task_type == 1:

        task_type = 'Virus'
        punishment = random.randint(1, 3)
        start_screen_background = screen.fill(green)
        selected_task = virus_tasks_list[0]
        virus_tasks_list.pop(0)
        if virus_tasks_list == []:
            virus_tasks_list = virus_tasks_func()
        punishment_display = True
        return start_screen_background, selected_task, punishment, punishment_display, task_type

    # Luck
    elif task_type == 2:

        task_type = 'Luck'
        punishment = random.randint(1, 3)
        start_screen_background = screen.fill(yellow)
        selected_task = luck_tasks_list[0]
        luck_tasks_list.pop(0)
        if luck_tasks_list == []:
            luck_tasks_list = luck_tasks_func()
        punishment_display = False
        return start_screen_background, selected_task, punishment, punishment_display, task_type

    # Punish
    elif task_type == 3:

        task_type = 'Punishment'
        punishment = random.randint(1, 3)
        start_screen_background = screen.fill(red)
        selected_task = punish_tasks_list[0]
        punish_tasks_list.pop(0)
        if punish_tasks_list == []:
            punish_tasks_list = punish_tasks_func()
        punishment_display = False
        return start_screen_background, selected_task, punishment, punishment_display, task_type
    
    # Quiz
    elif task_type == 4:

        task_type = 'Quiz'
        punishment = random.randint(1, 3)
        start_screen_background = screen.fill(blue)
        selected_task = quiz_tasks_list[0]
        quiz_tasks_list.pop(0)
        if quiz_tasks_list == []:
            quiz_tasks_list = quiz_tasks_func()
        punishment_display = True
        return start_screen_background, selected_task, punishment, punishment_display, task_type
    # Task
    else:

        task_type = 'Task'
        punishment = random.randint(1, 8)
        start_screen_background = screen.fill(turqoise)
        selected_task = single_user_tasks_list[0]
        single_user_tasks_list.pop(0)
        if single_user_tasks_list == []:
            single_user_tasks_list = single_user_task_func()
        punishment_display = True
        return start_screen_background, selected_task, punishment, punishment_display, task_type

def select_player_func():
    global previous_player

    # Randomly selects a player and avoids choosing it twice in a row
    selected_player = player_list[(random.randint(0,(len(player_list) -1)))]
    while selected_player == previous_player:
        selected_player = player_list[(random.randint(0,(len(player_list) -1)))]
    previous_player = selected_player
    return selected_player

# Initialize game screen buttons
quit_button_text = font_4.render('Quit game', True, black)
add_remove_button_text = font_4.render('Add/Remove', True, black)

# Inializing game screen
while game_screen_running:

    # Ends loop when quit window button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_screen_running = False
        
        mouse = pygame.mouse.get_pos()
        print(mouse)                                                                                   # DELETE TO DISPLAY MOUSE LOCATION
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1300 <= mouse[0] <= 1500 and 650 <= mouse[1] <= 686:
                game_screen_running = False
            
            elif 1100 <= mouse[0] <= 1275 and 650 <= mouse[1] <= 686:
                print("add player")
            







            else:
                # Calls the randomizers
                selected_player = select_player_func()
                start_screen_background, selected_task, punishment, punishment_display, task_type = task_func()
                task_count = task_count + 1

                # Define task and lower fond if string is too long
                if len(selected_task) > 55:
                    task_text = font_6.render((str(selected_player) + str(selected_task)), True, black)
                else:
                    task_text = font_5.render((str(selected_player) + str(selected_task)), True, black)
                screen.blit(task_text, (20, 250))

                # Define and task type
                task_type_text = font_2.render((str(task_type)), True, black)
                
                # Displays task type in the midle of the screen
                if task_type == 'Punishment':
                    screen.blit(task_type_text, (600, 70))
                else:
                    screen.blit(task_type_text, (700, 70))

                # Display punishment if needed
                if punishment_display == True:

                    # Define and display or
                    screen.blit(font_5.render('of', True, black), (150, 330))

                    # Define and display punishment
                    punishment_text = font_5.render('Drink ' + str(punishment) + ' slok(ken)', True, black)
                    screen.blit(punishment_text, (20, 410))

                # Define task count
                task_count_text = font_4.render(('Task count: ' + str(task_count) ), True, black)
                screen.blit(task_count_text, (1300, 20))


        # Changes color when hovering over Quit game button
        if 1300 <= mouse[0] <= 1500 and 650 <= mouse[1] <= 686:
            quit_button_text = font_4.render('Quit game', True, red)
        else:
            quit_button_text = font_4.render('Quit game', True, black)
        start_screen_background

        # Changes color when hovering over add/remove button
        if 1100 <= mouse[0] <= 1275 and 650 <= mouse[1] <= 686:
            add_remove_button_text = font_4.render('Add/Remove', True, dark_green)
        else:
            add_remove_button_text = font_4.render('Add/Remove', True, black)
        start_screen_background

    # Display options bar
    pygame.draw.rect(screen , light_gray, pygame.Rect(1105, 641, 400, 50))

    # Display quit button
    screen.blit(quit_button_text, (1317, 650))

    # Display add/remove button
    screen.blit(add_remove_button_text, (1117, 650))

    # Set the pygame window name and Update the display
    pygame.display.set_caption('Drunkster')
    pygame.display.update()

# Sets the FPS to 15
clock = pygame.time.Clock()
clock.tick(15)

# Quit screen
pygame.quit()