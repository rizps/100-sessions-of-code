def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_square():
    move()
    turn_right()
    turn_right()
    turn_right()
    move()
    turn_right()
    turn_right()
    turn_right()
    move()
    turn_right()
    turn_right()
    turn_right()
    move()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# The conditions front_is_clear() or wall_in_front(), 
# at_goal(), and their negation.
#while at_goal() != True:
#    if at_goal() != True:
#        while wall_in_front():
#            jump()
#    if at_goal() != True:     
#        while front_is_clear():
#            move()

#other way
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
    
