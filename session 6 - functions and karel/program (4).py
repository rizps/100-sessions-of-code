def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def jump_long():
    while wall_on_right():
        while wall_in_front():
            turn_left()
        move()
        if at_goal():
            done()
        if not wall_on_right():
            turn_right()
            move()
            turn_right()

def jump_long2():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left() 
    
#while not at_goal():
#    if wall_in_front():
#        turn_left()
#        jump_long()  
#    else:
#        move()
        
# other way
while not at_goal():
    if wall_in_front():
        jump_long2()  
    else:
        move()

    
