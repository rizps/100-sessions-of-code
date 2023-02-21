# guess a number
import random
from art import logo

def play_game():
    print(logo)
    print("welcome to the number guessing game!")
    print("i'm thinking a number between 1 to 100")
    thenumber = random.choice(range(100))
    print(f"psstt the number is {thenumber}")
    repeat = False
    attemp = 0
    while not repeat:
        repeat = True
        difficulty = input("choose the difficulty, type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            attemp = 10
        elif difficulty == 'hard':
            attemp = 5
        else:
            print("you better type the right word!")
            repeat = False

    for i in range(attemp):
        print(f"you have {attemp} attempts to guess the number")
        guess = int(input("make a guess: "))
        if guess == thenumber:
            print(f"you got it! the number was {thenumber}")
            break
        elif guess > thenumber:
            print("too high")
        elif guess < thenumber:
            print("too low")

        if attemp == 0:
            print("you've run out the guesses, you lose")
        attemp -= 1

while input("do you want to play the guess number game? type 'y' or 'n': ") == 'y':
    play_game()
print("goodbye")




