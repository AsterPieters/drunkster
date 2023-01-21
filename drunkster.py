# Drunkster, Get drunk or DIE!
# A drinking game by Aster Pieters

# Imports
import pygame



# Initializing pygame
pygame.init()
print("Hello World")

# Define resolution
screen_width=1200
screen_height=600

# Define colors
white = (255, 255, 255)
light_gray = (205, 205, 205)
gray = (100, 100, 100)
dark_gray = (150, 150, 150)
black = (0, 0, 0)

# Define fonts
font_1 = pygame.font.SysFont(None, 45)

# Define "enter a player" text & Rectangle
enter_player_text = font_1.render('Enter a player:', True, black)
textrect = enter_player_text.get_rect()

# Define enter player textbox & Rectangle
enter_player_textbox_rect = pygame.Rect(300, 450, 200, 32)
enter_player_textbox_color_passive = pygame.Color(light_gray)
enter_player_textbox_color_active = pygame.Color(dark_gray)
enter_player_textbox_color = enter_player_textbox_color_passive
active = False
enter_player_textbox_input = ''

# Define "start game" button
start_game_text = font_1.render('Start Drunkster' , True , black)

# Add player to list function
players = []

def add_player_func():

    if enter_player_textbox_input == '':
        print("No name was given")
    
    else:
        players.append(enter_player_textbox_input)
        print(players)

# Define display
screen = pygame.display.set_mode([screen_width, screen_height])

# Stores the width & height into variables
width = screen.get_width()
height = screen.get_height()

# Inializing start screen
game_running = True
while game_running:

    # Ends loop when quit window button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if enter_player_textbox_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
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
                add_player_func()
                enter_player_textbox_input = ''
        
        # Checks if a mouse is clicked
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
              
            # If the mouse is clicked on the button the game is started
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
        
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(screen,light_gray,[width/2,height/2,140,40])
          
        else:
            pygame.draw.rect(screen,dark_gray,[width/2,height/2,140,40])
                

    # Fills the background
    screen.fill(white)

    # Set the pygame window name
    pygame.display.set_caption('Drunkster, get drunk or DIE!')

    # Displays "Enter a player" text
    pygame.draw.rect(enter_player_text, white, textrect, 1)
    screen.blit(enter_player_text, (20, 450))

    # Changes color for textbox
    if active:
        enter_player_textbox_color = enter_player_textbox_color_active
    else:
        enter_player_textbox_color = enter_player_textbox_color_passive

    # Displays "Add player" textbox
    pygame.draw.rect(screen, enter_player_textbox_color, enter_player_textbox_rect)
    text_surface = font_1.render(enter_player_textbox_input, True, (black))
    screen.blit(text_surface, (enter_player_textbox_rect.x+5, enter_player_textbox_rect.y+5))
    
    # Set width of textfield so that text cannot get outside of user's text input
    enter_player_textbox_rect.w = max(150, text_surface.get_width()+10)

    # Displays "Start Drunkster" button
    screen.blit(start_game_text , (width/2+50,height/2))

    # Update the display
    pygame.display.update()

# Sets the FPS to 60
clock = pygame.time.Clock()
clock.tick(60)

# Quit screen
pygame.quit()

