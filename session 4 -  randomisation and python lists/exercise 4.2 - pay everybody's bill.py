# pay everybody's bill
# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work,
# you must enter all the names as names followed by comma then space. e.g. name, name, name
# Import the random module here
import random
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
names_string = 'abc, bc, cdef, def, efgh'
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(f'original list is: {names}')
random_index = random.randrange(len(names))
random_number = str(names[random_index])
print(f'{random_number} is going to buy the meal today!')

# other way
num_name = len(names)
random_index2 = random.randint(0, num_name - 1) # -1 because counting start from 0 -> 0, 1, 2, 3, 4
random_number2 = str(names[random_index2])
print(f'{random_number2} is going to buy the meal today 2!')


