# ==========================================================
# Pygame development
# ==========================================================

# access the pygame libraries
import pygame


# set screen size & title
SCREEN_TITLE = "Crossing Game"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

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
        # local variable - specify whether moving up or down the screen
        direction = 0

        # create a player character
        player = PlayerObject("img/player.png", 375, 550, 50, 50)
        
        # create an enemy character
        enemy = EnemyObject("img/enemy.png", 650, 300, 50, 50)

        # create a treasue object - this is what the player is trying to reach
        treasure = GameObject('img/treasure.png', 375, 50, 50, 50)
        
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
                        
            # update the player position, pass the screen height from the game
            player.move(direction, self.height)
            
            # update the enemy position pass in screen width from the game
            enemy.move(self.width)
            
            # redraw the background before redrawing the game objects again
            self.game_screen.fill(WHITE_COLOR)

            # Draw the treasure
            treasure.draw(self.game_screen)

            # Draw the player character 
            player.draw(self.game_screen)

            # Draw the enemy character 
            enemy.draw(self.game_screen)

            # does player collidie with enemy
            if player.detect_collision(enemy):
                is_game_over = True

            # does player collidie with treasure
            if player.detect_collision(treasure):
                is_game_over = True

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
        self.ypos   = y
        self.width  = w
        self.height = h
    
    def draw(self, background):
        # Draw the player image on top of the screen at (x, y) position
        background.blit(self.image, (self.xpos, self.ypos))
        
#====================================================
# this is the Player game object class
# ====================================================
class PlayerObject(GameObject):

    # how many tiles the characters moves per second
    SPEED = 5
    
    def __init__(self, image_path, x, y, w, h):
        super().__init__(image_path, x, y, w, h)
        
        self.xpos = x
        self.ypos = y
        self.width  = w
        self.height = h
    
    # down the screen an increasing ypos / up the screen is a decreasing ypos
    # direction -1 is down direction +1 is up 
    def move(self, direction, max_height):
        # up the screen is a decreasing ypos 
        if direction > 0 and self.ypos > 5 :
            self.ypos -= self.SPEED
            print(self.ypos)
        # down the screen is an increasing ypos
        elif direction < 0 and self.ypos < max_height - 50:
            self.ypos += self.SPEED

    # if player ypos is above enemy ypos or below enemy ypos then no chance of a collision
    # Return False if y positions and x positions do not overlap
    # Return True if x and y positions overlap
    def detect_collision(self, other_body):

        if self.ypos > other_body.ypos + other_body.height:
            return False
        elif self.ypos + self.height < other_body.ypos:
            return False

        if self.xpos > other_body.xpos + other_body.width:
            return False
        elif self.xpos + self.width < other_body.xpos:
            return False

        # so if all collision checks fail there is an overlap
        return True
        
#====================================================
# this is the Enemy game object class
# ====================================================
class EnemyObject(GameObject):

    # how many tiles the characters moves per second
    SPEED = 5
    
    def __init__(self, image_path, x, y, w, h):
        super().__init__(image_path, x, y, w, h)
        
        self.xpos = x
        self.ypos = y
        self.width  = w
        self.height = h
    
    # left - an increasing xpos / right - a decreasing xpos
    # pass in width of screen from Game object so we know our right boundary
    def move(self, max_width):
        if self.xpos <= 5:
            self.SPEED = abs(self.SPEED)
        elif self.xpos >= max_width - 50:
            self.SPEED = -abs(self.SPEED)

        self.xpos += self.SPEED

#initialise pygame
pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# quit game when game loop exits
pygame.quit()
quit()
