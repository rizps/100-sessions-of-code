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
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() != True:
    jump()