#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_letters = 4
nr_symbols = 2
nr_numbers = 2
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for letter in range(len(letters)):
#     print(letter)

password = ''
num_letter = len(letters)
num_number = len(numbers)
num_symbol = len(symbols)
for letter in range(nr_letters):
    random_index = random.randint(0, num_letter - 1)
    random_letter = str(letters[random_index])
    password += random_letter
for number in range(nr_numbers):
    random_index = random.randint(0, num_number - 1)
    random_number = str(numbers[random_index])
    password += random_number
for symbol in range(nr_symbols):
    random_index = random.randint(0, num_symbol - 1)
    random_symbol = str(symbols[random_index])
    password += random_symbol

print(f'the ez password: {password} -> it is random characters but with a fixed sequance')


# other way - eazy
password = ''
for char in range(nr_letters):
    password += random.choice(letters)
for char in range(nr_numbers):
    password += random.choice(numbers)
for char in range(nr_symbols):
    password += random.choice(symbols)
print(f'this is the other way - eazy password: {password}')


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ''
num_letter = len(letters)  # make a lenght of the letters to make a random index
num_number = len(numbers)
num_symbol = len(symbols)

list = [num_symbol, num_number, num_letter]  # make a list of character type
num_list = len(list)  # make a lenght of the list to make a random index
# print(list)
for hard_pass in range(num_symbol + num_letter + num_number - 1):  # we loop until the total off the password lenght
    random_index = random.randint(0, num_list - 1)  # generate which character to be added from the list
    if random_index == 0:  # here, from the list 0 = symbol
        if nr_symbols > 0:  # check if number of symbol is stil needed or not based on the user preferences
            random_index = random.randint(0, num_symbol - 1)
            random_symbol = str(symbols[random_index])  # generate random character from symbols
            password += random_symbol  # adding random symbol to the password
            nr_symbols -= 1  # substract number of symbol that is need to be show
    elif random_index == 1:
        if nr_numbers > 0:
            random_index = random.randint(0, num_number - 1)
            random_number = str(numbers[random_index])
            password += random_number
            nr_numbers -= 1
    elif random_index == 2:
        if nr_letters > 0:
            random_index = random.randint(0, num_letter - 1)
            random_letter = str(letters[random_index])
            password += random_letter
            nr_letters -= 1

print(f'the hard password: {password} -> it is completely random characters')


# other way - hard
# here we chould re-define the nr_x because in the hard way we substract them until 0,
# or the other hard way can be moved up under the other ez way
nr_letters = 4
nr_symbols = 2
nr_numbers = 2
password_list = []

for chars in range(nr_letters):
    password_list += random.choice(letters)
for chars in range(nr_numbers):
    password_list += random.choice(numbers)
for chars in range(nr_symbols):
    password_list += random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for i in password_list:
    password += i
print(password)

