# ======================================================= #
# arays/lists - can change, add, remove elements
# dictionaries - key : value pairs can be changed
# tuples - non mutable, cant change values
# ======================================================= #

size = (100, 200)
print(size)

width = size[0]     # width 100
height = size[1]     # height 100

d3_size = size + (300,)

print(d3_size)

len(size) # 2
max(size) # 200
min(size) # 100

max(d3_size) # 300

does_contain = 100 in size # does_contain = True

print(does_contain)

movement = [5,-2,4,6]

movement.append(10)
movement.remove(-3)

# ARRAYS
movement = [5, -2, -3, 4, -1]

first_movement = movement[0]    # first_movement = 5
movement[0] = 7                 # movement = [7, -2, -3, 4, -1]
movement.append(-5)             # movement = [7, -2, -3, 4, -1, -5]
movement.remove(-3)             # movement = [7, -2, 4, -1, -5]

# DICTIONARIES
starting_positions = {'p_0': 50, 'p_1': 100, 'p_2': 150}

starting_positions['p_0']           # 50

starting_positions.keys()           # ['p_0', 'p_1', 'p_2']

starting_positions['p_3'] = 200     #{'p_0': 50, 'p_1': 100, 'p_2': 150, 'p_3': 200}

del starting_positions['p_3']       #{'p_0': 50, 'p_1': 100, 'p_2': 150}

