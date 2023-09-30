import pygame

class Button:
    def __init__(self, x, y, width, height, text, click_callback=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = (255, 255, 255)
        self.color = (50, 50, 50)
        self.color_hover = (133, 217, 37)
        self.is_hovered = False
        self.click_callback = click_callback
        self.handle_event()

    def draw(self, screen):

        button_color = self.color_hover if self.is_hovered else self.color
        # Draw the button rectangle
        pygame.draw.rect(screen, button_color, self.rect)
        
        # Create a font
        font = pygame.font.Font(None, 36)
        
        # Create text surface
        text_surface = font.render(self.text, True, self.text_color)
        
        # Center the text on the button
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        
        # Blit the text onto the button
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
            
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)

        ##### Check if button is clicked #####
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos) and self.click_callback:
                    self.click_callback()

