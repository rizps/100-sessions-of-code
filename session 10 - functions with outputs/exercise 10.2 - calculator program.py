# calculator program
from art import logo

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

def calculator():
    print(logo)
    num1 = float(input('what is the first number? '))
    repeat = True
    while repeat:
        for i in calc:
            print(i)
        choose = input('what operasion? ')

        num2 = float(input("what is the next number? "))
        cals = calc[choose]
        answer = cals(num1, num2)

        print(f"{num1} {choose} {num2} = {answer}")
        repeat_again = input(f"type 'y' to continue calculatin with {answer}, or 'n' to repeat the calculation: ").replace(' ', '').lower()
        if repeat_again == 'y':
            num1 = answer
        else:
            repeat = False
            calculator()
calculator()
