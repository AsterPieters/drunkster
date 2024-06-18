# Drunkster, Get drunk or DIE!
# A drinking game by Aster Pieters

import pygame
import random
import argparse

from helpers.players import *
from helpers.button import Button
from helpers.textbox import Textbox
from helpers.categories import Tasker
from helpers.animations import *

from settings import *

def drunkster(debug=False):
    # Initializing pygame
    pygame.init()

    # Initialize variables
    players = []
    user_input = ''
    message = ''
    message_colour = BLACK
    task_count = 0
    previous_player = None

    # Inializing loops
    start_screen_running = True
    game_screen_running = False
    game_running = True

    # Define start game button
    start_game_text = FONT_2.render('Start Drunkster' , True , BLACK)

    # Define "enter a player" text
    enter_player_text = FONT_1.render('Enter a player:', True, BLACK)

    # Define and center the title 
    title_top_text = FONT_4.render('Drunkster', True, BLACK)
    title_top_rect = title_top_text.get_rect()
    title_top_rect.center = (SCREEN_WIDTH // 2, 75)

    # Define added players text
    added_players_text = FONT_0.render('Players: ', True, BLACK)

    # Define fore/back ground
    bg = pygame.image.load('ui/images/start_screen.png')
    fg = pygame.image.load('ui/images/game_screen.png')

    # Create textbox
    new_player = None
    left_plank = pygame.image.load('ui/images/left_plank.png')
    SCREEN.blit(left_plank, (5, SCREEN_HEIGHT - 465))
    enter_player_textbox = Textbox(50, SCREEN_HEIGHT - 300, 300, 75, user_input, BLACK, WHITE)

    # Create buttons
    start_game_button = Button(50, SCREEN_HEIGHT - 200, 300, 75, "Start Drunkster", BLACK, GREEN, WHITE)
    next_task_button = Button(50, SCREEN_HEIGHT - 300, 300, 75, "Next task", BLACK, GREEN, WHITE)
    go_home_button = Button(50, SCREEN_HEIGHT - 200, 300, 75, "Back", BLACK, GRAY, WHITE)
    quit_game_button = Button(50, SCREEN_HEIGHT - 100, 300, 75, "Quit game", BLACK, RED, WHITE)

    # Debug mode
    if debug:
        players = ["Michael", "Meredith", "Dwight"]

    # Create the tasker
    tasker = Tasker()

    # Main loop
    while game_running:

        # Ends loop when quit window button is pressed
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_screen_running = False
                    game_screen_running = False
                    game_running = False

        while start_screen_running:

            # Fills the background
            SCREEN.fill(TURQUOISE)
            SCREEN.blit(bg, (0,0))

            # Add player textbox
            enter_player_textbox.draw()

            # Start game button
            start_game_button.draw()

            # Quit game button
            quit_game_button.draw()

            # Go to the game screen
            for event in pygame.event.get():
                # Quit the game
                if quit_game_button.check_event(event):
                    start_screen_running = False
                    game_screen_running = False
                    game_running = False

                if start_game_button.check_event(event):
                    # Check if players were entered.
                    if len(players) >= 2:

                        # Remove the title and message
                        title_top_text = FONT_4.render('', True, BLACK)
                        message = ''

                        # Run the start game animation
                        animate_start()

                        start_screen_running = False
                        game_screen_running = True
                        game_running = True
                    else:
                        message = "Please enter at least 2 players!"
                        message_colour = RED

                # Check if player is added
                new_player = enter_player_textbox.check_event(event)

            # Add new players to list
            if new_player:
                message, message_colour = add_player(new_player, players)

            # Display right plank
            right_plank = pygame.image.load('ui/images/right_plank.png')
            SCREEN.blit(right_plank, (SCREEN_WIDTH -350, SCREEN_HEIGHT - 350))

            # Set the pygame window name
            pygame.display.set_caption('Drunkster')

            # Displays text
            SCREEN.blit(enter_player_text, (50, SCREEN_HEIGHT - 350))
            SCREEN.blit(title_top_text, title_top_rect)

            # Displays the players
            for player in players:
                players_text = FONT_2.render(player, True, BLACK)
                for i, player in enumerate(players):
                    if i < 13:
                        SCREEN.blit(FONT_0.render(player, True, BLACK), (SCREEN_WIDTH - 335, SCREEN_HEIGHT - 335 + (25 * players.index(player))))
                    else:
                        SCREEN.blit(FONT_0.render(player, True, BLACK), (SCREEN_WIDTH - 180, SCREEN_HEIGHT - 335 + (25 * players.index(player) - 325)))

            # Display messages
            message_text = FONT_2.render(message, True, message_colour)
            message_rect = message_text.get_rect()
            message_rect.center = (SCREEN_WIDTH // 2, 300)
            SCREEN.blit(message_text, message_rect)

            # Update the display
            pygame.display.update()

        # Inializing game screen
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
                    tasker.next_task(selected_player, task_count)
                    task_count = task_count + 1

                    # Set player to previous player
                    previous_player = selected_player

                    # Define task count
                    task_count_text = FONT_0.render(('Task count: ' + str(task_count) ), True, BLACK)
                    SCREEN.blit(task_count_text, (1300, 20))

                    # Display the bar again
                    SCREEN.blit(fg, (0,0))

                # Go back to the start screen
                if go_home_button.check_event(event):

                    animate_back()
                    game_screen_running = False
                    start_screen_running = True


            # Set the pygame window name and Update the display
            pygame.display.set_caption('Drunkster, Get Drunk Or Die')
            pygame.display.update()

    # Sets the FPS to 15
    clock = pygame.time.Clock()
    clock.tick(60)

    # Quit screen
    pygame.quit()

def main():
    parser = argparse.ArgumentParser(description='Run drunkster in debug')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()

    # Call the animate_start function with the debug flag
    drunkster(debug=args.debug)

if __name__ == "__main__":
    main()