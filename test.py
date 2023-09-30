import pygame

# Constants
NORMAL_BUTTON_COLOR = (0, 128, 255)
HOVER_BUTTON_COLOR = (0, 200, 255)
TEXT_COLOR = (255, 255, 255)

class Button:
    def __init__(self, x, y, width, height, text, click_callback=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.normal_color = NORMAL_BUTTON_COLOR
        self.hover_color = HOVER_BUTTON_COLOR
        self.is_hovered = False
        self.click_callback = click_callback

    def draw(self, screen):
        # Change the button color based on whether the mouse is hovering
        button_color = self.hover_color if self.is_hovered else self.normal_color
        
        # Draw the button rectangle
        pygame.draw.rect(screen, button_color, self.rect)
        
        # Create a font
        font = pygame.font.Font(None, 36)
        
        # Create text surface
        text_surface = font.render(self.text, True, TEXT_COLOR)
        
        # Center the text on the button
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        
        # Blit the text onto the button
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # Check if the mouse is over the button
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button is pressed over the button
            if self.rect.collidepoint(event.pos) and self.click_callback:
                self.click_callback()

# Example callback function
def on_button_click():
    print("Button clicked!")
