# for loop with list
fruits = ['grape', 'apple', 'durian']
for fruit in fruits:
    print(fruit)

# for loop with range
for number in range(1, 10): # 1-10 not including 10
    print(number)

# counting number from 1 to 100
t_number = 0
for number in range(1, 101):
    t_number += number
print(f'the total number between 1-100 is {t_number}')