# if else statement
# e.g.

# print('welcome to the ghost house!')
# age = int(input('what is your age? '))

# if age >= 10:
#     print('you can enter the ghost house!')
# else:
#     print('sorry, you have to be 10 or more')

# ---
# additional feature for the program
print('welcome to the rollercouster!')
height = int(input('what is your height in cm? '))
# if height >= 120:
#     print('you can enter the rollercouster!')
#     age = int(input('what is your age? '))
#     if age < 11:
#         print('you have to pay for $5')
#     elif age < 16:
#         print('you have to pay for $7')
#     else:
#         print('you have to pay for $10')
# else:
#     print('sorry, you have to be 120cm or more')

# ---
# again, with additional photos charge
bill = 0
# if height >= 120:
#     print('you can enter the rollercouster!')
#     age = int(input('what is your age? '))
#     if age < 11:
#         bill = 5
#         print('you have to pay for $5')
#     elif age < 16:
#         bill = 7
#         print('you have to pay for $7')
#     else:
#         bill = 10
#         print('you have to pay for $10')
#     wants_photo = input('do you want a photo taken? y or n? ')
#     if wants_photo == 'y':
#         bill += 3
#     print(f'your total bill is ${bill}')
# else:
#     print('sorry, you have to be 120cm or more')

# ---
# again, with additional midlife crisis(45-55y) charge
if height >= 120:
    print('you can enter the rollercouster!')
    age = int(input('what is your age? '))
    if age < 11:
        bill += 5
        print('you have to pay for $5')
    elif age < 16:
        bill += 7
        print('you have to pay for $7')
    elif age < 45:
        bill += 10
        print('you have to pay for $10')
    elif age > 44 and age < 56:
        bill = 0
        print('you do not have to pay for the rollercoaster bill')
    wants_photo = input('do you want a photo taken? y or n? ')
    if wants_photo == 'y':
        bill += 3
    print(f'your total bill is ${bill}')
else:
    print('sorry, you have to be 120cm or more')


