# functions
# implementing, calling, parameters, return values

x_pos = 0
e_x_pos = 4

# implementation
def move():
    global x_pos        # access to variable defined outside the function
    x_pos += 1

# calling
move()

print(x_pos)

# implementation
def move_by(amount):
    global x_pos        # access to variable defined outside the function
    x_pos += amount
    
# calling
move_by(5)

print(x_pos)            # x_pos = 6

# implementation
def check_collision():
    global x_pos        # access to variable defined outside the function
    global e_x_pos      # access to variable defined outside the function
    if x_pos == e_x_pos:
        return True
    else:
        return False
    
# calling
move_by(5)
collision = check_collision()

print(x_pos)            # x_pos = 6
print(collision)        # x_pos = 6

    
