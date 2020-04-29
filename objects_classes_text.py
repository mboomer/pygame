# classes and objects
# class fields, methods, constructors
# object instantiation

# objects - state & behaviour
# object is an instance of the class

class GameCharacter:

    speed = 5                                                   # field variable
    
    def __init__(self, name, width, height, x_pos, y_pos):      # constructor
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):                   # method
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

character_0 = GameCharacter("Mark", 25, 25, 100, 100)           # new instance

print(character_0.name)

character_0.name = "Mark Boomer"                                # change value
print(character_0.name)

character_0.move(50, 100)                                       # call method

print(character_0.x_pos)                                        
print(character_0.y_pos)

# =================== CHALLENGE =========================================
# count no of times an enemy collides
# =================== CHALLENGE =========================================

class EnemyCharacter:

        collisions = 3
        
        def __init__(self, width, height, colour, xpos, ypos):
            self.width = width
            self.height = height
            self.colour = colour
            self.xpos = xpos
            self.ypos = ypos

        def collide(self):                                      # dont forget self if no paras are passed
            self.collisions += 1

enemy_small = EnemyCharacter(10, 10, "blue", 50, 50)

print(enemy_small.colour)

enemy_small.collide()

print(enemy_small.collisions)

print("==================================")

# ============================================================
# subclasses, superclasses and inheritance
# ============================================================

class Player1Character(GameCharacter):

    def __init__(self, name, width, height, x_pos, y_pos):      # constructor
        super().__init__(name, width, height, x_pos, y_pos)     # super class constructor


Player1 = Player1Character("Player-1", 25, 25, 40, 175)

print(Player1.name)

Player1.move(50, 50)

print(Player1.x_pos)
print(Player1.y_pos)
print("==================================")

# ============================================================
# player cannot specify width and height
# superclass sets width/height to be 100, 100
# ============================================================
class PlayerCharacter(GameCharacter):

    def __init__(self, name, x_pos, y_pos):                 # constructor
        super().__init__(name, 100, 100, x_pos, y_pos)       # super class constructor

    def move(self, by_y_amount):                            # overide super method
        super().move(0, by_y_amount)                        # call super method
        
Player2 = PlayerCharacter("Player-2", 100, 100)

print(Player2.name)

Player2.move(50)

print(Player2.x_pos)
print(Player2.y_pos)

print("==================================")

# ============================================================
# CHALLENGE
# ============================================================
class NonPlayerCharacter(GameCharacter):                   

    def __init__(self, name, colour, width, height, x_pos, y_pos):  # constructor
        self.colour = colour                                            # init the colour
        super().__init__(name, width, height, x_pos, y_pos)         # super class constructor

    
    def position_at(self, x_coord, y_coord):                        
        self.x_pos = x_coord
        self.y_pos = y_coord
        
redCharacter = NonPlayerCharacter("Red Character", "red", 50, 30, 100, 200)

print(redCharacter.name)
print(redCharacter.x_pos)
print(redCharacter.y_pos)

redCharacter.position_at(50,95)

print("==== position at ==============================")
print(redCharacter.x_pos)
print(redCharacter.y_pos)

print("==================================")

    
    



























