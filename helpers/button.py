import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text, screen):

        # Text
        self.text = text
        self.text_color = (255, 255, 255)

        # Color
        self.color = (0, 0, 0)
        self.color_hover = (100, 100, 100)

        # Form
        self.hovered = False
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        # Change color when hovering over the object
        if self.hovered:
            button_color = self.color_hover
        else:
            button_color = self.color

        # Draw the button rectangle
        pygame.draw.rect(self.screen, button_color, self.rect)
        
        # Assign a font
        font = FONT_1
        
        # Create text surface
        text_surface = font.render(self.text, True, self.text_color)
        
        # Center the text on the button
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        
        # Blit the text onto the button
        self.screen.blit(text_surface, text_rect)
    
    def check_event(self, event):
        # Check if user hovering over the button
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        
        # Check if user clicked on button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                return True
