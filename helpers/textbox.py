import pygame
import time

from settings import *

class Textbox:
    def __init__(self,x ,y , width, height, input, colour, text_colour):

        # Input
        self.input = input
        self.text_colour = text_colour
        
        # Color
        self.colour = colour
        
        # Form
        self.error_code = ''
        self.hovered = False
        self.active = False
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        # Draw the rectangle
        pygame.draw.rect(SCREEN, self.colour, self.rect)

        # Create a font
        font = pygame.font.Font(None, 36)

        # Create the surface
        textbox_surface = font.render(self.input, True, self.text_colour)

        # Center the text on the button
        textbox_rect = textbox_surface.get_rect()
        textbox_rect.center = self.rect.center

        SCREEN.blit(textbox_surface, textbox_rect)
    
    def check_event(self, event):
        if event.type == pygame.KEYDOWN:

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                # Remove one char
                self.input = self.input[:-1]

            # Checks for enters
            elif event.key == pygame.K_RETURN:
                # Keeps data from entering twice
                time.sleep(0.2)
                output = self.input
                self.input = ''
                return output

            # Add char to input
            else:
                self.input += event.unicode