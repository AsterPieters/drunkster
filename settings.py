# Settings
import pygame

# Initialize pygame
pygame.init()

# Fonts
FONT_0 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 25)
FONT_1 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 35)
FONT_2 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 50)
FONT_3 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 80)
FONT_4 = pygame.font.Font('ui/fonts/Ubuntu-Regular.ttf', 150)

# Screen
SCREEN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# Colours
BLACK = (0, 0, 0)
TURQOISE = (0, 153, 153)
RED = (204, 0, 0)
YELLOW = (204, 204, 0)
GREEN = (0, 204, 0)
BLUE = (0, 102, 204)
ORANGE = (204, 102, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
BROWN = (139,69,19)