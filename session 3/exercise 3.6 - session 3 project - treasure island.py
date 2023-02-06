print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# question
# * 'You\'re at a crossroad. Where do you want to go? Type "left" or "right"'
# * 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
# * "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"

# answer
# * "You fell into a hole. Game Over." -> right or anything else
# * "You get attacked by an angry trout. Game Over." -> swim or anything else
# * "It's a room full of fire. Game Over." -> red
# * "You enter a room of beasts. Game Over." -> blue
# * "You chose a door that doesn't exist. Game Over." -> anything else

# * "You found the treasure! You Win!" -> yellow
# to win, we can choose: left, wait, yellow

#Write your code below this line 👇
# left_right = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"? ').lower()
# example:
left_right = 'left'
if left_right == 'right':
    print("You fell into a hole. Game Over.")
elif left_right == 'left':
    # swim_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. '
    #                   'Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    # example:
    swim_wait = 'wait'
    if swim_wait == 'swim':
        print("You get attacked by an angry trout. Game Over.")
    elif swim_wait == 'wait':
        # door_color = input("You arrive at the island unharmed. There is a house with 3 doors. "
        #                    "One red, one yellow and one blue. Which colour do you choose?").lower()
        # example:
        door_color = 'yellow'
        if door_color == 'red':
            print("It's a room full of fire. Game Over.")
        elif door_color == 'blue':
            print("You enter a room of beasts. Game Over.")
        elif door_color == 'yellow':
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")



