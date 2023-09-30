import pygame

class Textbox:
    def __init__(self,x ,y , width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (50, 50, 50)
        self.color_hover = (133, 217, 37)
        self.is_hovered = False

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