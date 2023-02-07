import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# choose = int(input('what do you choose? 0: rock, 1: paper, 2: scissors '))
# computer_choose = random.randint(0, 2)
#
# # print the image
# if choose == 0:
#     print(rock)
# elif choose == 1:
#     print(paper)
# elif choose == 2:
#     print(scissors)
#
# # print the image computer choose image
# print('computer choose: ')
# if computer_choose == 0:
#     print(rock)
# elif computer_choose == 1:
#     print(paper)
# elif computer_choose == 2:
#     print(scissors)
#
# # if you choose 0: rock
# if choose == 0 and computer_choose == 0:
#     print('draw')
# elif choose == 0 and computer_choose == 1:
#     print('you lose')
# elif choose == 0 and computer_choose == 2:
#     print('you win')
#
# # if you choose 1: paper
# if choose == 1 and computer_choose == 0:
#     print('you win')
# elif choose == 1 and computer_choose == 1:
#     print('draw')
# elif choose == 1 and computer_choose == 2:
#     print('you lose')
#
# # if you choose 2: scissors
# if choose == 2 and computer_choose == 0:
#     print('you lose')
# elif choose == 2 and computer_choose == 1:
#     print('you win')
# elif choose == 2 and computer_choose == 2:
#     print('draw')

# ---
# other way
choose = int(input('what do you choose? 0: rock, 1: paper, 2: scissors: \n'))
computer_choose = random.randint(0, 2)
game_images = [rock, paper , scissors]
if choose >= 3 or choose < 0:
    print('you choose an invalid number, you lose')
else:
    print(game_images[choose]) # game_images in else so when the user type an invalid number it will not cause an error
    print('computer choose: ')
    print(game_images[computer_choose])
    if choose == 0 and computer_choose == 2:
        print('you win')
    elif computer_choose == 0 and choose == 2:
        print('you lose')
    elif computer_choose > choose:
        print('you lose')
    elif choose > computer_choose:
        print('you win')
    elif choose == computer_choose:
        print('draw')
