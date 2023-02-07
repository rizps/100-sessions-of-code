# counting even number from 1 to 100
# Write your code below this row 👇

t_even_number = 0
for number in range(1, 101):
    if number % 2 == 0:
        t_even_number += number

print(f'the total even number from 1 to 100 is {t_even_number}')

# other way
t_even_number2 = 0
for number in range(2, 101, 2): # because 1 is not evene number, we start from 2 with adding step 2
    t_even_number2 += number
print(f'with other way: {t_even_number2}')
