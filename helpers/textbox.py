import pygame
import time

class Textbox:
    def __init__(self,x ,y , width, height, screen, input):

        # Input
        self.input = input
        self.text_color = (255, 255, 255)
        
        # Color
        self.color = (50, 50, 50)
        self.color_hover = (133, 217, 37)
        
        # Form
        self.screen = screen
        self.error_code = ''
        self.hovered = False
        self.active = False
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        # Change color when hovering over the object
        if self.hovered:
            textbox_color = self.color_hover
        else:
            textbox_color = self.color

        # Draw the rectangle
        pygame.draw.rect(self.screen, textbox_color, self.rect)

        # Create a font
        font = pygame.font.Font(None, 36)

        # Create the surface
        textbox_surface = font.render(self.input, True, self.text_color)

        # Center the text on the button
        textbox_rect = textbox_surface.get_rect()
        textbox_rect.center = self.rect.center

        self.screen.blit(textbox_surface, textbox_rect)
    
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