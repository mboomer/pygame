# control flow
# if statements
# pay attention to the : and the indentation

#if condition:
#        code to execte if true

is_game_over = False


p_0_x_pos = 0   # player position
e_0_x_pos = 3   # enemy position
e_1_x_pos = 5   # enemy position

p_0_x_pos += 2  # move the player

if p_0_x_pos == e_0_x_pos:
        is_game_over = True
elif p_0_x_pos == e_1_x_pos:
        is_game_over = True
else:
    e_0_x_pos += 1
    e_1_x_pos += 1
    
print(is_game_over)

if p_0_x_pos == e_0_x_pos or p_0_x_pos == e_1_x_pos:
        is_game_over = True
else:
    e_0_x_pos += 1
    e_1_x_pos += 1
    
print(is_game_over)

# ===========================================
# while / for in loops
# ===========================================
# while not is_game_over:
#     do something until is_game_over = False
# ===========================================
# for item in array:
#    do something until end of the array
# ===========================================

is_game_over = False

p_x_pos = 0
e_x_pos = 3
end_x_pos = 10

while not is_game_over:
        print(p_x_pos)
        print(e_x_pos)
        if p_x_pos == e_x_pos:
            print("You Lose")
            is_game_over = True
        elif p_x_pos >= end_x_pos:
            print("You Won !!")
            is_game_over = True
        else:
            print("Coming to get you !!")
            p_x_pos += 2
            e_x_pos += 2

x_pos = 5
movements = [1, -2, 6, -3, -2, 4]

for movement in movements:
    print(x_pos)
    print (movement)
    x_pos += movement

print(x_pos)            # x_pos = 9




