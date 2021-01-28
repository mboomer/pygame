import pygame           # import pygame module

class GameObject:

    def __init__(self, x, y, width, height, image_path):         # constructor
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))