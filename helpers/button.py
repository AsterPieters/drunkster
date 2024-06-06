import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text, colour, hover_colour, text_colour):

        # Text
        self.text = text
        self.text_colour = text_colour
        
        # Color
        self.colour = colour
        self.colour_hover = hover_colour

        # Form
        self.hovered = False
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        # Change color when hovering over the object
        if self.hovered:
            button_colour = self.colour_hover
        else:
            button_colour = self.colour

        # Draw the button rectangle
        pygame.draw.rect(SCREEN, button_colour, self.rect)
        
        # Assign a font
        font = FONT_1
        
        # Create text surface
        text_surface = font.render(self.text, True, self.text_colour)
        
        # Center the text on the button
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        
        # Blit the text onto the button
        SCREEN.blit(text_surface, text_rect)
    
    def check_event(self, event):
        # Check if user hovering over the button
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        
        # Check if user clicked on button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                return True
