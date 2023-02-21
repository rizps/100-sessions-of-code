from art import logo, vs
from game_data import data
import random
# skretching, just to check
# print(logo)
# print(f"compare A: ... ")
# print(vs)
# print(f"against b: ... ")
#
# print(len(data))
# the constraction of the data is like this:
# 'name': 'Instagram',
# 'follower_count': 346,
# 'description': 'Social media platform',
# 'country': 'United States'
# print(data[1])
# for i in range(len(data)-1):
#     print(data[i])

# def random_data():
#     rd = random.choice(data)
#     for i in rd:
#         print(i)
#         print(rd[i])

# print(random_data())
# random_data()

# lets code
score = 0
true_answer = False
change = False
ar = random.choice(data)
br = random.choice(data)
while not true_answer:
    print(logo)
    if score != 0:
        print(f"you are right!, current score is {score}")

    if change:
        ar = br
        if ar == br:
            br = random.choice(data)
    print(f"compare a: {ar['name']}, {ar['description']}, from {ar['country']}")
    print(vs)
    print(f"compare b: {br['name']}, {br['description']}, from {br['country']}")
    ans = input("who has the more ig followers? type 'a' or 'b': ")
    if ar['follower_count'] > br['follower_count'] and ans == 'a':
        score += 1
        change = True
    elif ar['follower_count'] < br['follower_count'] and ans == 'b':
        score += 1
        change = True
    else:
        true_answer = True
        print(f"your answer is wrong, the final score is {score}")
        print("goodbye")


# other way, a.k.a. the constructor way
# this code contains more line but more structure i think
def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
# game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''

# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.