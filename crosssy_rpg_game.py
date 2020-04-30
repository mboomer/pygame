# ==========================================================
# Pygame development
# ==========================================================

# access the pygame libraries
import pygame

# initial the font
pygame.font.init()


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

# choose a specific font
font = pygame.font.SysFont("comicsans", 75)

#====================================================
# this the game class
# has a method to run the game loop
# ====================================================
class Game:
    
    # typical tick rate = 60fps
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height):
    
        self.title  = title
        self.width  = width
        self.height = height
        
        # Create a window to display the game
        self.game_screen = pygame.display.set_mode((width, height))

        # set background colour and title for game screen
        self.game_screen.fill(WHITE_COLOR)

        # set title for game screen
        pygame.display.set_caption(title)

        # Load the background image from the file directory
        background_image = pygame.image.load(image_path)
        # Scale the image to width & height we want
        # can use w,h as we havent yet initialised self.width self.height      
        self.image = pygame.transform.scale(background_image, (width, height))
        
    def run_game_loop(self, level_speed):

        # used to exit the game loop
        is_game_over = False
        player_wins = False
        
        # local variable - specify whether moving up or down the screen
        direction = 0

        # create a player character
        player = PlayerObject("img/player.png", 375, 650, 50, 50)
        
        # create an enemy character
        enemy = EnemyObject("img/enemy.png", 25, 150, 50, 50)
        # Speed increased as we advance in difficulty
        if level_speed <= 6:   
            enemy.SPEED += level_speed
            
        # create an enemy character
        enemy_1 = EnemyObject("img/enemy-yel.png", 675, 250, 50, 50)
        # set the enemy speed - increase for each level
        if level_speed <= 4:   
            enemy_1.SPEED += level_speed
        
        # create an enemy character
        enemy_2 = EnemyObject("img/enemy-red.png", 450, 400, 50, 50)
        # set the enemy speed - increase for each level
        if level_speed <= 8:   
            enemy_2.SPEED += level_speed
        
        # create an enemy character
        enemy_3 = EnemyObject("img/enemy-blu.png", 150, 500, 50, 50)
        # set the enemy speed - increase for each level
        if level_speed <= 5:   
            enemy_3.SPEED += level_speed
        
        # create an enemy character
        enemy_4 = EnemyObject("img/enemy.png", 350, 350, 50, 50)
        # set the enemy speed - increase for each level
        if level_speed <= 5:   
            enemy_4.SPEED += level_speed
        
        # create a treasue object - this is what the player is trying to reach
        treasure = GameObject('img/treasure.png', 375, 5, 50, 50)
        
        # ==================================================================================
        # main game loop, updates movements, checks, graphics etc
        # runs until is_game_over = True
        # ==================================================================================
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
                        
            # draw the background before redrawing the game objects again
            self.game_screen.fill(WHITE_COLOR)
            # draw the background
            self.game_screen.blit(self.image, (0, 0))
                
            # Draw the treasure
            treasure.draw(self.game_screen)

            # update the player position, pass the screen height from the game
            player.move(direction, self.height)
            # Draw the player character 
            player.draw(self.game_screen)
            
            # creates an array dependant on the level to control number of enemies
            enemies = [enemy]
            
            if level_speed >= 5:   
                enemies = [enemy, enemy_1, enemy_2, enemy_3, enemy_4]
            elif level_speed >= 4:   
                enemies = [enemy, enemy_1, enemy_2, enemy_3]
            elif level_speed >= 3:   
                enemies = [enemy, enemy_1, enemy_2]
            elif level_speed >= 2:   
                enemies = [enemy, enemy_1]
            else:   
                enemies = [enemy]
                
            # move and draw all the enemies in the enemy array - which depends on the level
            for nmy in enemies:
                nmy.move(self.width)
                nmy.draw(self.game_screen)

            if player.detect_collision(treasure):
                is_game_over = True
                player_wins = True
                text = font.render("You Won", True, RED_COLOR)
                self.game_screen.blit(text,(285, 200))
                pygame.display.update()
                clock.tick(1)
                break    
            else:
                for nmy in enemies:
                    if player.detect_collision(nmy):
                        is_game_over = True
                        player_wins = False
                        text = font.render("You Lost...Try Again", True, RED_COLOR)
                        self.game_screen.blit(text,(200, 200))
                        pygame.display.update()
                        clock.tick(1)
                        break

            # update game graphics
            pygame.display.update()

            # tick the clock to update everything, myst reference self as this belongs to the class now
            clock.tick(self.TICK_RATE)

        # ==================================================================================
        # end of main game loop
        # ==================================================================================
        
        # if player wins then run the game loop again
        # increase the enemy speed
        if player_wins:
            self.run_game_loop(level_speed + 0.5)
        # if player loses then break out of loop completely
        else:
            return
        
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
    SPEED = 10
    
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
        # down the screen is an increasing ypos
        elif direction < 0 and self.ypos < max_height - 50:
            self.ypos += self.SPEED

    # if player ypos is above enemy ypos or below enemy ypos then no chance of a collision
    # Return False if y positions and x positions do not overlap
    # Return True if x and y positions overlap
    def detect_collision(self, other_body):
        # use floor operator to be a bit less stringent of when an oeverlap causes a collision
        if self.ypos > other_body.ypos + (other_body.height // 3):
            return False
        elif self.ypos + (self.height // 3) < other_body.ypos:
            return False

        if self.xpos > other_body.xpos + (other_body.width // 3):
            return False
        elif self.xpos + (self.width // 3) < other_body.xpos:
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

#====================================================
# Start the game 
# ====================================================

#initialise pygame
pygame.init()

new_game = Game("img/background.png", SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
# pass in 1 as the multiplier for the enemy speed
new_game.run_game_loop(1)

# quit game when game loop exits
pygame.quit()
quit()
