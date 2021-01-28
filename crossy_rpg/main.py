import pygame               # import pygame library

from game import Game       # import Game class from game.py

# ##############################################
# initialise pygame library
# ##############################################
pygame.init()

# ##############################################
# create an instance of Game and run game loop
# ##############################################
game = Game()
game.run_game_loop()

# ##############################################
# quit the game
# ##############################################
pygame.quit()
quit()
