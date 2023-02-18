def format_name():
    name = input('what is your name? ').split()
    f_name = ''
    l_name = ''
    # for i in name:
    f_name = name[0].capitalize()
    l_name = name[-1].capitalize()
    print(f'your first name is: {f_name}')
    print(f'your last name is: {l_name}')

# format_name()

# simple calculator program
# add
def add(a, b):
    return a + b

# substract
def substract(a, b):
    return a - b

# multiply
def multiply(a, b):
    return a * b

# divide
def divide(a, b):
    c = a / b
    return c
calc = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide,
}

# basic calculator
# num1 = int(input('what is the first number? '))
# for i in calc:
#     print(i)
# choose = input('what operasion? ')
# num2 = int(input('what is the second number? '))
#
# cals = calc[choose]
# answer = cals(num1, num2)
# print(f"{num1} {choose} {num2} = {answer}")
#
# choose2 = input('what other operasion? ')
# cals2 = calc[choose2]
# num3 = int(input('what is the next number? '))
# answer2 = cals2(answer, num3)
# print(f"{answer} {choose2} {num3} = {answer2}")


