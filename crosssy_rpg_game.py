# ==========================================================
# Pygame development
# ==========================================================

# access the pygame libraries
import pygame

#initialise pygame
pygame.init()

# set screen size & title
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Crossing Game"

#colours RGB codes in tuples
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)
RED_COLOR   = (255,0,0)
GREEN_COLOR = (0,255,0)
BLUE_COLOR  = (0,0,255)
SHADE_COLOR = (125,125,125)

# clock used to update game events & frames
clock = pygame.time.Clock()
# typical tick rate = 60fps
TICK_RATE = 60
# used to exit the game loop
is_game_over = False

# Create a window to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# set background colour and title for game screen
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

# Load the player image from the file directory
player_image = pygame.image.load('img/player.png')
# Scale the image up as its very small
player_image = pygame.transform.scale(player_image, (50, 50))

# main game loop, updates movements, checks, graphics etc
# runs until is_game_over = True

while not is_game_over:

    # get all events occuring at a given time
    # eg mouse clicks, key presses, button clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

    pygame.draw.rect(game_screen, BLACK_COLOR, [50,50,50,50])
    pygame.draw.circle(game_screen, SHADE_COLOR, [75, 25], 25)
    
    # Draw the player image on top of the screen at (x, y) position
    game_screen.blit(player_image, (375, 375))

    # update game graphics
    pygame.display.update()

    # tick the clock to update everything
    clock.tick(TICK_RATE)

# quit game when game loop exits
pygame.quit()
quit()
