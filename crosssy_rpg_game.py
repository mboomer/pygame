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

#====================================================
# this the game class
# has a method to run the game loop
# ====================================================
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
        # specify whether moving up or down the screen
        direction = 0

        # create a player character
        player = PlayerObject("img/player.png", 375, 600, 50, 50)
        
        # main game loop, updates movements, checks, graphics etc
        # runs until is_game_over = True

        while not is_game_over:
            # get all events occuring at a given time
            # eg mouse clicks, key presses, button clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Detect when a key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # if up key was pressed move up screen
                    if event.key == pygame.K_UP:
                        direction = 1
                    # if down key pressed Move down 
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Detect when the key is released
                elif event.type == pygame.KEYUP:
                    # Stop movement if up or down key is released
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                        
                print(event)
            
            # update the player position
            player.move(direction)
            
            # redraw the background before redrawing the game objects again
            self.game_screen.fill(WHITE_COLOR)

            # Draw the player character 
            player.draw(self.game_screen)

            # draw a rect and circle
            pygame.draw.rect(self.game_screen, BLACK_COLOR, [50,50,50,50])
            pygame.draw.circle(self.game_screen, SHADE_COLOR, [75, 25], 25)
                
            # update game graphics
            pygame.display.update()

            # tick the clock to update everything, myst reference self as this belongs to the class now
            clock.tick(self.TICK_RATE)
        
#====================================================
# this is the game object super class
# other game objects will be subclasses of this object
# ====================================================
class GameObject:

    def __init__(self, image_path, x, y, w, h):

        # Load the image from the file directory
        object_image = pygame.image.load(image_path)
        # Scale the image to width & height we want
        self.image = pygame.transform.scale(object_image, (w, h))         # can use w,h as we havent yet initialised self.width self.height      

        self.xpos   = x
        self.ypox   = y
        self.width  = w
        self.height = h
    
    def draw(self, background):
        # Draw the player image on top of the screen at (x, y) position
        background.blit(self.image, (self.xpos, self.ypos))
        
#====================================================
# this is the Player game object class
# other game objects will be subclasses of this object
# ====================================================
class PlayerObject(GameObject):

    # how many tiles the characters moves per second
    SPEED = 10
    
    def __init__(self, image_path, x, y, w, h):
        super().__init__(image_path, x, y, w, h)
        
        self.xpos = x
        self.ypos = y
        self.width  = w
        self.height = h
    
    # down the screen an increasing ypos / up the screen is a decreasing ypos
    # direction -1 is down direction +1 is up 
    def move(self, direction):
        # up the screen is a decreasing ypos 
        if direction > 0:
            self.ypos -= self.SPEED
        # down the screen is an increasing ypos
        elif direction < 0:
            self.ypos += self.SPEED
        
#initialise pygame
pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# quit game when game loop exits
pygame.quit()
quit()
