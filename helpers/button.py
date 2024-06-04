import pygame

class Button:
    def __init__(self, x, y, width, height, text, screen, event):

        # Text
        self.text = text
        self.text_color = (255, 255, 255)

        # Color
        self.color = (0, 0, 0)
        self.color_hover = (100, 100, 100)

        # Form
        self.hovered = False
        self.rect = pygame.Rect(x, y, width, height)


        self.check_event(event)

        # Function
        self.draw(screen)

    def draw(self, screen):

        # Change color when hovering over the object
        if self.hovered:
            button_color = self.color_hover
        else:
            button_color = self.color

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
    
    def check_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                return True
