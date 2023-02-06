# true love score
# Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.
#
# Name 1	                Name 2	            Score
# Catherine Zeta-Jones      Michael Douglas    	99
# Brad Pitt	                Jennifer Aniston	73
# Prince William	        Kate Middleton	    67
# Angela Yu	                Jack Bauer	        53
# Kanye West	            Kim Kardashian	    42
# Beyonce	                Jay-Z	            23
# John Lennon	            Yoko Ono	        18

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = 'Catherine Zeta-Jones'
name2 = 'Michael Douglas '
merge_name = (name1 + name2).lower()
t = merge_name.count('t')
r = merge_name.count('r')
u = merge_name.count('u')
e = merge_name.count('e')

l = merge_name.count('l')
o = merge_name.count('o')
v = merge_name.count('v')

true = t + r + u + e
love = l + o + v + e
true = str(true)
love = str(love)
true_love = true + love
true_love = int(true_love)
# print(true_love)

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

