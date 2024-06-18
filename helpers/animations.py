
from settings import *




def animate_start():

    x_pos = 0
    y_pos = 0

    # Define fore/back ground
    bg = pygame.image.load('ui/images/start_screen.png')
    fg = pygame.image.load('ui/images/game_screen.png')
    start_animation_bg = pygame.image.load('ui/images/start_animation_screen.png')

    speed = 2

    while True:
        # Stop the image if it reaches the end
        if x_pos <= (-SCREEN_WIDTH):
            SCREEN.fill(TURQUOISE)
            SCREEN.blit(fg, (0, 0))
            pygame.display.update()
            break

        # Slow down towards the end
        elif x_pos <= (-SCREEN_WIDTH / 2):
            if speed > 2:
                speed -= 2

        # Speed up the image
        else:
            speed += 2

        # Move the image
        x_pos -= speed
        SCREEN.fill(TURQUOISE)
        SCREEN.blit(start_animation_bg, (x_pos, y_pos))

        print(speed)

        # Update the display
        pygame.display.update()

def animate_back():

    x_pos = -SCREEN_WIDTH
    y_pos = 0

    # Define fore/back ground
    bg = pygame.image.load('ui/images/start_screen.png')
    fg = pygame.image.load('ui/images/game_screen.png')
    start_animation_bg = pygame.image.load('ui/images/start_animation_screen.png')

    speed = 2

    while True:
        # Stop the image if it reaches the end
        if x_pos >= 0:
            SCREEN.fill(TURQUOISE)
            SCREEN.blit(fg, (SCREEN_WIDTH, 0))
            pygame.display.update()
            break

        # Slow down towards the end
        elif x_pos >= (-SCREEN_WIDTH / 2):
            if speed > 2:
                speed -= 2

        # Speed up the image
        else:
            speed += 2

        # Move the image
        x_pos += speed
        SCREEN.fill(TURQUOISE)
        SCREEN.blit(start_animation_bg, (x_pos, y_pos))

        print(speed)

        # Update the display
        pygame.display.update()