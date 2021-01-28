import pygame                           # import pygame module

from gameObject import GameObject       # import GameObject class from gameObject.py
from player     import Player           # import Player class from player.py
from enemy      import Enemy            # import Player class from player.py

class Game:

    def __init__(self):         # constructor
        
        self.height = 700        # self. makes this a property rather than a variable
        self.width  = 800
        self.white_colour = (255, 255, 255)
        
        # part of pygame library
        self.clock = pygame.time.Clock()

        # set the game level, increment by 0.5
        self.level = 1.0

        # create the game window
        self.game_window = pygame.display.set_mode((self.width, self.height))

        # create the background image
        self.background = GameObject(0, 0, self.width, self.height, "assets/background.png")

        # create the treasure image
        self.treasure   = GameObject(375, 25, 50, 50, "assets/treasure.png")

        # set the game state based on the initial level
        self.reset_map()

# #############################################################################################################

    # ##############################################
    # method to move reset the game, levels etc.
    # ##############################################
    def reset_map(self):
        
        # set player to start position
        self.player = Player(375, 600, 50, 50, "assets/player.png", 10)

        # set the speed for the enemies
        speed = 2 + (self.level * 2)

        # create the enemy images
        if (self.level >= 4.0):
            self.enemies = [
                Enemy(100, 100, 50, 50, "assets/enemy.png", speed),
                Enemy(600, 200, 50, 50, "assets/enemy.png", speed),
                Enemy(200, 300, 50, 50, "assets/enemy.png", speed),
                Enemy(600, 400, 50, 50, "assets/enemy.png", speed),
                Enemy(100, 450, 50, 50, "assets/enemy.png", speed),
                Enemy(700, 550, 50, 50, "assets/enemy.png", speed)
            ]
        elif (self.level >= 2.0):
            self.enemies = [
                Enemy(100, 100, 50, 50, "assets/enemy.png", speed),
                Enemy(600, 200, 50, 50, "assets/enemy.png", speed),
                Enemy(200, 300, 50, 50, "assets/enemy.png", speed),
                Enemy(600, 400, 50, 50, "assets/enemy.png", speed)
            ]
        else:
            self.enemies = [
                Enemy(400, 200, 50, 50, "assets/enemy.png", speed),
                Enemy(600, 500, 50, 50, "assets/enemy.png", speed),
            ]
            
    # ##############################################
    # method to move the players and enemies
    # ##############################################
    def move_objects(self, direction):
        
        self.player.move(direction, self.height)                          

        for enemy in self.enemies:
            enemy.move(self.width)                            

    # ##############################################
    # method to draw the game objects
    # ##############################################
    def draw_objects(self):
        
        # fill game window with colour, wipes game window clean
        self.game_window.fill(self.white_colour)

        # draw the background image at position 0, 0 at top left
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))

        # draw the treasure image at position, at top , in middle
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))

        # draw the player image at position, at 50,50
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        # draw the enemy images
        for enemy in self.enemies: 
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

        pygame.display.update()             # update drawing and fill in all colors

    # ####################################################
    # method to run the detect collisions between objects
    # ####################################################
        
    def detect_collisions(self):
        
        # does player collide with enemy
        for enemy in self.enemies:
            if (self.collision(self.player, enemy)):
                self.level = 1.0                                # reset the game
                return True

        # does player collide with treasure
        if (self.collision(self.player, self.treasure)):
            self.level += 0.5                                   # increase the level
            return True

        return False

    # ####################################################
    # method to run the detect collisions between objects
    # ####################################################
        
    def collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False

        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False

        return True

    # ##############################################
    # method to run the game loop
    # needs self as it is a method and needs access 
    # to class properties
    # ##############################################
    def run_game_loop(self):

        player_direction = 0

        while True:

            events = pygame.event.get()                 # get list of all events that are happening

            for event in events:                        # check for any pygame quit event
                if event.type == pygame.QUIT:
                    return                              # break out of control flow & exit entire function
                elif event.type == pygame.KEYDOWN:      # check if a key has been pressed down
                    if event.key == pygame.K_UP:        # check which was pressed
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:        # check if a key has been released
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:        
                        player_direction = 0

            # execute logic

            # move player and enemies
            self.move_objects(player_direction)

            # draw objects
            self.draw_objects()                         

            # detect collisions
            if (self.detect_collisions() == True):
                self.reset_map()                        # reset the map after a collision

            # fill window and display updates 60 times per second
            self.clock.tick(60)

    # ##############################################
    # end of run_game_loop
    # ##############################################
