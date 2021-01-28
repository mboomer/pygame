from gameObject import GameObject       # import GameObject class from gameObject.py

class Enemy(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):
    
        super().__init__(x, y, width, height, image_path)

        self.speed = speed

    def move(self, max_width):                      # enemies move horizontally

        if (self.x <= 0):                           # is enemy at left edge of screen
            self.speed = abs(self.speed)            # swap speed to move right
        elif (self.x > max_width - self.width):     # is enemey at right edge of screen
            self.speed = -self.speed                # swap speed to move left

        self.x += self.speed