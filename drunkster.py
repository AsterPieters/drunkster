# Drunkster, Get drunk or DIE!
# A drinking game by Aster Pieters

import pygame
from helpers.task import *
from helpers.players import *
from helpers.button import Button
from helpers.textbox import Textbox
from helpers.categories import Tasker

# Initializing pygame
pygame.init()

# Define resolution
player_width = 500
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
# Define colors
white = (255, 255, 255)
light_gray = (205, 205, 205)
gray = (50, 50, 50)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (143, 189, 255)
green = (133, 217, 37)
dark_green = (205, 255, 157)
turqoise = (37, 183, 217)

# Define fonts
font = pygame.font.Font(None, 36)
font_1 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 50)
font_2 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 80)
font_3 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 150)
font_4 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 25)
font_5 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 50)
font_6 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 35)

# Add player to list function
players = []
task_index = 0
user_input = ''
message = ''

# Define start game button
start_game_text = font_1.render('Start Drunkster' , True , black)

# Define "enter a player" text
enter_player_text = font_6.render('Enter a player:', True, black)

# Define and center the title 
title_top_text = font_3.render('Drunkster', True, black)
title_top_rect = title_top_text.get_rect()
title_top_rect.center = (screen_width // 2, 75)

# Define and center the text
title_bottom_text = font_2.render('Get drunk or DIE', True, black)
title_bottom_rect = title_bottom_text.get_rect()
title_bottom_rect.center = (screen_width // 2, 200)

# Define added players text
added_players_text = font_4.render('Players: ', True, black)

# Define display
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

# Stores the width & height into variables
width = screen.get_width()
height = screen.get_height()

# Puts default background
start_screen_background = screen.fill(turqoise)

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
screen.blit(left_plank, (5, screen_height - 465))
enter_player_textbox = Textbox(50, screen_height - 400, 300, 75, screen, user_input)

# Create buttons
start_game_button = Button(50, screen_height - 100, 300, 75, "Start Drunkster", screen)
next_task_button = Button(50, screen_height - 300, 300, 75, "Next task", screen)
go_home_button = Button(50, screen_height - 200, 300, 75, "Back", screen)
quit_game_button = Button(50, screen_height - 100, 300, 75, "Quit game", screen)

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
        screen.blit(bg, (0,0))

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
            message_text = font_1.render(message, True, red)
            screen.blit(message_text, (400, 640))

        # Display right plank
        right_plank = pygame.image.load('ui/images/right_plank.png')
        screen.blit(right_plank, (screen_width // 2, screen_height - 460 ))

        # Set the pygame window name
        pygame.display.set_caption('Drunkster')

        # Displays text
        screen.blit(enter_player_text, (50, screen_height - 450))
        screen.blit(title_top_text, title_top_rect)
        screen.blit(title_bottom_text, title_bottom_rect)

        # Displays the players
        for player in players:
            players_text = font_1.render(player, True, black)
            screen.blit(font_4.render(player, True, black), (1300 , 400 + (25 * players.index(player))))

        # Update the display
        pygame.display.update()

    # Inializing game screen
    start_screen_background = screen.fill(blue)
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
                tasker.next_task(screen, selected_player, task_count)
                task_count = task_count + 1

                # Set player to previous player
                previous_player = selected_player

                # Define task count
                task_count_text = font_4.render(('Task count: ' + str(task_count) ), True, black)
                screen.blit(task_count_text, (1300, 20))

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