# Drunkster, Get drunk or DIE!
# A drinking game by Aster Pieters

import pygame
import random

from helpers.task import *
from helpers.players import *
from helpers.button import Button
from helpers.textbox import Textbox
from helpers.categories import Tasker

from settings import *

# Initializing pygame
pygame.init()

# Define resolution
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Add player to list function
players = []
task_index = 0
user_input = ''
message = ''

# Define start game button
start_game_text = FONT_2.render('Start Drunkster' , True , BLACK)

# Define "enter a player" text
enter_player_text = FONT_1.render('Enter a player:', True, BLACK)

# Define and center the title 
title_top_text = FONT_4.render('Drunkster', True, BLACK)
title_top_rect = title_top_text.get_rect()
title_top_rect.center = (screen_width // 2, 75)

# Define and center the text
title_bottom_text = FONT_3.render('Get drunk or DIE', True, BLACK)
title_bottom_rect = title_bottom_text.get_rect()
title_bottom_rect.center = (screen_width // 2, 200)

# Define added players text
added_players_text = FONT_0.render('Players: ', True, BLACK)

# Stores the width & height into variables
width = SCREEN.get_width()
height = SCREEN.get_height()

# # Puts default background
# start_screen_background = SCREEN.fill(TURQOISE)

# Define options bar
options_bar_rect = pygame.Rect(365, 516, 200, 60)

# Initiate the variables
selected_task = 'Press enter to start the first round.'
selected_player = ''
previous_player = ''
task_count = 0
punishment = ''
click = 0

# Inializing loops
start_screen_running = True
game_screen_running = False
game_running = True

# Add player textbox
new_player = None
left_plank = pygame.image.load('ui/images/left_plank.png')
SCREEN.blit(left_plank, (5, screen_height - 465))
enter_player_textbox = Textbox(50, screen_height - 400, 300, 75, user_input, BROWN, WHITE)

# Create buttons
start_game_button = Button(50, screen_height - 100, 300, 75, "Start Drunkster", BLACK, GREEN, WHITE)
next_task_button = Button(50, screen_height - 300, 300, 75, "Next task", BLACK, GRAY, WHITE)
go_home_button = Button(50, screen_height - 200, 300, 75, "Back", BLACK, GRAY, WHITE)
quit_game_button = Button(50, screen_height - 100, 300, 75, "Quit game", BLACK, RED, WHITE)

tasker = Tasker()

while game_running:

    # Ends loop when quit window button is pressed
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_screen_running = False
                game_screen_running = False
                game_running = False

    while start_screen_running:

        # Fills the background
        bg = pygame.image.load('ui/images/bar.png')
        SCREEN.blit(bg, (0,0))

        # Add player textbox
        enter_player_textbox.draw()

        # Start game button
        start_game_button.draw()

        # Go to the game screen
        for event in pygame.event.get():
            if start_game_button.check_event(event):

                # Check if players were entered.
                if players:
                    start_screen_running = False
                    game_screen_running = True
                    game_running = True
                else:
                    message = "Please enter at least 2 players!"

            # Check if player is added
            new_player = enter_player_textbox.check_event(event)

        # Add new players to list
        if new_player:
            message = add_player(new_player, players)
        
        # Display messages
        if message:
            message_text = FONT_2.render(message, True, RED)
            SCREEN.blit(message_text, (400, 640))

        # Display right plank
        right_plank = pygame.image.load('ui/images/right_plank.png')
        SCREEN.blit(right_plank, (screen_width // 2, screen_height - 460 ))

        # Set the pygame window name
        pygame.display.set_caption('Drunkster')

        # Displays text
        SCREEN.blit(enter_player_text, (50, screen_height - 450))
        SCREEN.blit(title_top_text, title_top_rect)
        SCREEN.blit(title_bottom_text, title_bottom_rect)

        # Displays the players
        for player in players:
            players_text = FONT_2.render(player, True, BLACK)
            SCREEN.blit(FONT_0.render(player, True, BLACK), (1300 , 400 + (25 * players.index(player))))

        # Update the display
        pygame.display.update()

    # Inializing game screen
    start_screen_background = SCREEN.fill(BLUE)
    while game_screen_running:

        # Draw the buttons
        next_task_button.draw()
        go_home_button.draw()
        quit_game_button.draw()

        # Check the events
        for event in pygame.event.get():
            
            # Quit the game
            if quit_game_button.check_event(event):
                start_screen_running = False
                game_screen_running = False
                game_running = False

            # Next task
            if next_task_button.check_event(event):
                # Select a player
                selected_player = select_player(players, previous_player)

                # Show the new task
                #next_task(selected_player, task_count)
                tasker.next_task(selected_player, task_count)
                task_count = task_count + 1

                # Set player to previous player
                previous_player = selected_player

                # Define task count
                task_count_text = FONT_0.render(('Task count: ' + str(task_count) ), True, BLACK)
                SCREEN.blit(task_count_text, (1300, 20))

            # Go back to the start screen
            if go_home_button.check_event(event):
                start_screen_running = True
                game_screen_running = False
                game_running = True


        # Set the pygame window name and Update the display
        pygame.display.set_caption('Drunkster')
        pygame.display.update()

# Sets the FPS to 15
clock = pygame.time.Clock()
clock.tick(15)

# Quit screen
pygame.quit()