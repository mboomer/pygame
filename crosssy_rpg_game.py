# ==========================================================
# Pygame development
# ==========================================================

# access the pygame libraries
import pygame


# set screen size & title
SCREEN_TITLE = "Crossing Game"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#colours RGB codes in tuples
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)
RED_COLOR   = (255,0,0)
GREEN_COLOR = (0,255,0)
BLUE_COLOR  = (0,0,255)
SHADE_COLOR = (125,125,125)

# clock used to update game events & frames
clock = pygame.time.Clock()

class Game:
    
    # typical tick rate = 60fps
    TICK_RATE = 60

    def __init__(self, title, width, height):
    
        self.title  = title
        self.width  = width
        self.height = height
        
        # Create a window to display the game
        self.game_screen = pygame.display.set_mode((width, height))

        # set background colour and title for game screen
        self.game_screen.fill(WHITE_COLOR)

        # set title for game screen
        pygame.display.set_caption(title)

    def run_game_loop(self):

        # used to exit the game loop
        is_game_over = False

        # main game loop, updates movements, checks, graphics etc
        # runs until is_game_over = True

        while not is_game_over:
            # get all events occuring at a given time
            # eg mouse clicks, key presses, button clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True

                print(event)
            
            # Load the player image from the file directory
            player_image = pygame.image.load('img/player.png')
            # Scale the image up as its very small
            player_image = pygame.transform.scale(player_image, (50, 50))
            # Draw the player image on top of the screen at (x, y) position
            self.game_screen.blit(player_image, (375, 375))

            # draw a rect and circle
            pygame.draw.rect(self.game_screen, BLACK_COLOR, [50,50,50,50])
            pygame.draw.circle(self.game_screen, SHADE_COLOR, [75, 25], 25)
                
            # update game graphics
            pygame.display.update()

            # tick the clock to update everything, myst reference self as this belongs to the class now
            clock.tick(self.TICK_RATE)
        
#====================================================
# this the game object super class
# other game object will be sub classes of this object
# ====================================================
class GameObject:

    def __init__(self, image_path, x, y, w, h):

        # dont initialise w & h yet as they we will do this when image is loaded
        self.xpos = x
        self.ypox = y
    
        # Load the image from the file directory
        object_image = pygame.image.load(image_path)
        # Scale the image to width & height we want
        self.image   = pygame.transform.scale(object_image, (w,h))

    def draw(self, background):
        # Draw the player image on top of the screen at (x, y) position
        self.background.blit(self.image, (self.xpos, self.ypos))
        
#initialise pygame
pygame.init()

new_game = Game("First Game", 800, 800)
new_game.run_game_loop()

# quit game when game loop exits
pygame.quit()
quit()
