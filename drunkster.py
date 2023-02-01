# Drunkster, Get drunk or DIE!
# A drinking game by Aster Pieters

# Imports
import pygame
import random

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
gray = (100, 100, 100)
dark_gray = (150, 150, 150)
black = (0, 0, 0)
red = (255, 0, 0)
dark_red = (155, 0, 0)
light_blue = (188, 218, 255)
blue = (143, 189, 255)

# Task colors
green = (133, 217, 37)
turqoise = (37, 183, 217)
purple = (158, 37, 217)

# Define fonts
font_1 = pygame.font.SysFont(None, 50)
font_2 = pygame.font.SysFont(None, 100)
font_3 = pygame.font.SysFont(None, 200)
font_4 = pygame.font.SysFont(None, 25)
font_5 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 50)

# Add player to list function
player_list = []

# Define "enter a player" text
enter_player_text = font_1.render('Enter a player:', True, black)
title_top_text = font_3.render('Drunkster', True, black)
title_bottom_text = font_2.render('Get drunk or DIE', True, black)

# Define enter player textbox & Rectangle
enter_player_textbox_rect = pygame.Rect(280, 445, 200, 40)
active = False
enter_player_textbox_input = ''

# Define added players text
added_players_text = font_4.render('Players: ', True, black)

def add_player_func():

    if enter_player_textbox_input == '':
        print("No name was given")
    
    elif len(enter_player_textbox_input) > 8:
        print("Max 8 charachters")

    else:
        player_list.append(enter_player_textbox_input)
        print(player_list)

# Define display
screen = pygame.display.set_mode([screen_width, screen_height])

# Stores the width & height into variables
width = screen.get_width()
height = screen.get_height()

# Inializing start screen
start_screen_running = True
game_screen_running = False
while start_screen_running:

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
                add_player_func()
                enter_player_textbox_input = ''

        
        # For events that occur upon clicking the mouse (left click)
        mouse = pygame.mouse.get_pos()
        print(mouse)                                                                                   # DELETE TO DISPLAY MOUSE LOCATION
        if event.type == pygame.MOUSEBUTTONDOWN:
              if 20 <= mouse[0] <= 270 and 400 <= mouse[1] <= 430:
                if player_list == []:
                    print('player list is empty')
                else:
                    print("Start button pushed")
                    game_screen_running = True
                    start_screen_running = False
                    pygame.display.update()
        
        # Changes color when hovering over start game button
        if 20 <= mouse[0] <= 270 and 400 <= mouse[1] <= 430:
            start_game_text = font_1.render('Start Drunkster' , True , gray)
        else:
            start_game_text = font_1.render('Start Drunkster' , True , black)

    # Fills the background
    screen.fill(light_blue)

    # Set the pygame window name
    pygame.display.set_caption('Drunkster')

    # Displays text
    screen.blit(enter_player_text, (20, 450))
    screen.blit(title_top_text, (490, 50))
    screen.blit(title_bottom_text, (530, 170))

    # Displays "Add player" textbox
    pygame.draw.rect(screen, blue, enter_player_textbox_rect)
    text_surface = font_1.render(enter_player_textbox_input, True, (black))
    screen.blit(text_surface, (enter_player_textbox_rect.x+5, enter_player_textbox_rect.y+5))
    
    # Set width of textfield so that text cannot get outside of user's text input
    enter_player_textbox_rect.w = max(150, text_surface.get_width()+10)

    # Displays "Start Drunkster" button
    screen.blit(start_game_text , (20, 400))

    # Display added players text & rectangle
    pygame.draw.rect(screen, blue, pygame.Rect(1190, 390, 300, 280))
    screen.blit(added_players_text, (1200, 400))
    
    # Displays the players
    for player in player_list:
        player_list_text = font_1.render(player, True, black)
        screen.blit(font_4.render(player, True, black), (1280 , 400 + (17 * player_list.index(player))))

    # Update the display
    pygame.display.update()


"""
This part of the code is for the game screen

"""


start_screen_background = screen.fill(turqoise)

# Gets the lines out of the single_user_tasks file and puts them in a list
with open('/opt/drunkster/ui/tasks/single_user_tasks') as task:
    single_user_tasks_list = task.read().splitlines()

# Gets the lines out of the single_user_tasks file and puts them in a list
with open('/opt/drunkster/ui/tasks/virus_tasks') as task:
    virus_tasks_list = task.read().splitlines()

selected_task = 'Press enter to start the first round.'
selected_player = ''
previous_player = ''
task_count = 0
task_index = 0
punishment = ''

# Define Quit button
quit_button_text = font_1.render('Quit game', True, black)
quit_game_button_rect = pygame.Rect(1300, 650, 200, 36)


def task_func():

    global task_index
    task_index = task_index +1

    punishment = random.randint(1, 8)

    if task_index == 5:
        
        # Randomly selects a task and checks the amount of tasks
        start_screen_background = screen.fill(green)
        selected_task = virus_tasks_list[(random.randint(0,(len(virus_tasks_list) -1)))]
        task_index = 0

        return start_screen_background, selected_task, punishment

    else:
        # Fills the background
        # Randomly selects a task and checks the amount of tasks
        start_screen_background = screen.fill(turqoise)
        selected_task = single_user_tasks_list[(random.randint(0,(len(single_user_tasks_list) -1)))]

        return start_screen_background, selected_task, punishment



def select_player_func():
    global previous_player

    # Randomly selects a player and avoids choosing it twice in a row
    selected_player = player_list[(random.randint(0,(len(player_list) -1)))]
    while selected_player == previous_player:
        selected_player = player_list[(random.randint(0,(len(player_list) -1)))]
    previous_player = selected_player
    return selected_player

click = 0

# Inializing game screen
while game_screen_running:

    # Fills the background
    #start_screen_background

    # Ends loop when quit window button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_screen_running = False
        
        mouse = pygame.mouse.get_pos()
        print(mouse)                                                                                   # DELETE TO DISPLAY MOUSE LOCATION
        if event.type == pygame.MOUSEBUTTONDOWN:
              if 1300 <= mouse[0] <= 1500 and 650 <= mouse[1] <= 686:
                game_screen_running = False

        # Checks for events
        if event.type == pygame.KEYDOWN:

            # Checks for enters and 
            if event.key == pygame.K_RETURN:

                # Calls the randomizers
                selected_player = select_player_func()
                start_screen_background, selected_task, punishment = task_func()
                task_count = task_count + 1

                # Define and display task
                task_text = font_5.render((str(selected_player) + str(selected_task)), True, black)
                screen.blit(task_text, (250, 350))

                # Define and display or
                screen.blit(font_5.render('of', True, black), (300, 420))

                # Define and display punishment
                punishment_text = font_5.render('Drink ' + str(punishment) + ' shots', True, black)
                screen.blit(punishment_text, (250, 490))

                # Define task count
                task_count_text = font_1.render(('Task count: ' + str(task_count) ), True, black)
                screen.blit(task_count_text, (1200, 20))

    # Changes color when hovering over Quit game button
    if 1300 <= mouse[0] <= 1500 and 650 <= mouse[1] <= 686:
        pygame.draw.rect(screen, dark_red, quit_game_button_rect)
    else:
        pygame.draw.rect(screen, red, quit_game_button_rect)

    # Display quit button
    screen.blit(quit_button_text, (1317, 650))

    # Set the pygame window name and Update the display
    pygame.display.set_caption('Drunkster')
    pygame.display.update()

# Sets the FPS to 15
clock = pygame.time.Clock()
clock.tick(15)

# Quit screen
pygame.quit()