# Adds the player name and checks for errors
import random
from settings import *

def add_player(new_player, players):
    if new_player == '':
        message = "Name cannot be empty"
        message_colour = RED

    elif len(new_player) > 8:
        message = "Please use 8 or less charachters!"
        message_colour = RED

    # Double add to remove player
    elif new_player in players:
        players.remove(new_player)
        message = f"Removed player {new_player}!"
        message_colour = GREEN

    # Add player
    else:
        players.append(new_player)
        message = f"Added player {new_player}!"
        message_colour = GREEN

    return message, message_colour

def select_player(players, previous_player):
    # Select a random player
    selected_player = players[(random.randint(0,(len(players) -1)))]

    # Checks for previeus player
    while selected_player == previous_player:
        selected_player = players[(random.randint(0,(len(players) -1)))]

    return selected_player