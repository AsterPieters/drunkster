# Adds the player name and checks for errors
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


# Randomly selects a player and avoids choosing it twice in a row
def select_player_func():
    global previous_player

    selected_player = player_list[(random.randint(0,(len(player_list) -1)))]
    while selected_player == previous_player:
        selected_player = player_list[(random.randint(0,(len(player_list) -1)))]
    previous_player = selected_player
    return selected_player
