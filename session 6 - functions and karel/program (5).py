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



while front_is_clear():
    move()
turn_left()

#while not at_goal():
#    if front_is_clear():
#        move()
#    if not wall_on_right():
#        turn_right()
#    if wall_in_front():
#        if wall_on_right():
#            turn_left()
    
# other way, first 297 steps, second 268 steps
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
        
 
        
        
        
        
        
    
        
    
        
    
        
    
