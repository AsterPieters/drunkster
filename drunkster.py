# Drunkster, Get drunk or DIE!
# A drinking game by Aster Pieters

# Imports
import pygame
import random

# Initializing pygame
pygame.init()
print("Hello World")


""""
This part of the code is for the start screen.

"""


# Define resolution
screen_width=1535
screen_height=715

# Define colors
white = (255, 255, 255)
light_gray = (205, 205, 205)
gray = (100, 100, 100)
dark_gray = (150, 150, 150)
black = (0, 0, 0)

# Define fonts
font_1 = pygame.font.SysFont(None, 50)
font_2 = pygame.font.SysFont(None, 100)

# Add player to list function
player_list = ['test']

# Define "enter a player" text
enter_player_text = font_1.render('Enter a player:', True, black)



# Define enter player textbox & Rectangle
enter_player_textbox_rect = pygame.Rect(300, 450, 200, 32)
enter_player_textbox_color_passive = pygame.Color(white)
enter_player_textbox_color_active = pygame.Color(light_gray)
enter_player_textbox_color = enter_player_textbox_color_passive
active = False
enter_player_textbox_input = ''

# Define title
title_text = font_2.render('Drunkster, get drunk or DIE!' , True , black)

def add_player_func():

    if enter_player_textbox_input == '':
        print("No name was given")
    
    else:
        player_list.append(enter_player_textbox_input)
        print(player_list)

# Define display
screen = pygame.display.set_mode([screen_width, screen_height])
start_screen_background = pygame.image.load("ui/images/start_screen_background.png")

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

                for p in player_list:
                    player_name_text = font_1.render(p, True, dark_gray)

                # Display players
                screen.blit(player_name_text, (20, 660))
        
        # For events that occur upon clicking the mouse (left click)
        mouse = pygame.mouse.get_pos()
        print(mouse)
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
            start_game_text = font_1.render('Start Drunkster' , True , dark_gray)
        else:
            start_game_text = font_1.render('Start Drunkster' , True , black)

    # Fills the background
    screen.blit(start_screen_background, (0, 0))

    # Set the pygame window name
    pygame.display.set_caption('(SS) Drunkster, get drunk or DIE!')

    # Displays "Enter a player" text
    screen.blit(enter_player_text, (20, 450))

    # Displays title
    screen.blit(title_text, (50, 50))

    # Changes color for textbox
    if active:
        enter_player_textbox_color = enter_player_textbox_color_active
    else:
        enter_player_textbox_color = enter_player_textbox_color_passive

    # Displays "Add player" textbox
    pygame.draw.rect(screen, enter_player_textbox_color, enter_player_textbox_rect)
    text_surface = font_1.render(enter_player_textbox_input, True, (black))
    screen.blit(text_surface, (enter_player_textbox_rect.x+5, enter_player_textbox_rect.y+5))
    
    # Set width of textfield so that text cannot get outside of user's text input
    enter_player_textbox_rect.w = max(150, text_surface.get_width()+10)

    # Displays "Start Drunkster" button
    screen.blit(start_game_text , (20, 400))

    # Update the display
    pygame.display.update()


"""
This part of the code is for the game screen

"""


# Gets the lines out of tasks.txt and puts them in a list
with open('/opt/drunkster/ui/tasks/single_user_tasks') as task:
    task_list = task.read().splitlines()

selected_task = 'Press enter to start the first round.'
selected_player = ''

# Inializing game screen
while game_screen_running:

    # Ends loop when quit window button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_screen_running = False

        # Checks for events
        if event.type == pygame.KEYDOWN:

            # Checks for enters and 
            if event.key == pygame.K_RETURN:

                print('New task button pressed')

                # Randomly selects a task, checks the amount of tasks, and removes the task from the list
                print('New task button pressed')
                selected_task = task_list[(random.randint(0,(len(task_list) -1)))]

                # Do we want to use the tasks once?
                #task_list.remove(selected_task)

                # Randomly selects a player, checks the amount of users.
                selected_player = player_list[(random.randint(0,(len(player_list) -1)))]

    # Define task
    task_text = font_1.render((selected_player + selected_task), True, black)
    taskrect = task_text.get_rect()

    # Fills the background
    screen.fill(white)

    # Displays task
    pygame.draw.rect(task_text, white, taskrect, 1)
    screen.blit(task_text, (20, 450))

    # Set the pygame window name
    pygame.display.set_caption('(GS) Drunkster, get drunk or DIE!')

    # Update the display
    pygame.display.update()

# Sets the FPS to 15
clock = pygame.time.Clock()
clock.tick(15)

# Quit screen
pygame.quit()
