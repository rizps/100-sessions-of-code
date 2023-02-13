# prime number number checker
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
#
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# Write your code below this line 👇
def prime_checker(n):
    p = False
    # Corner case
    if n <= 1:
        print(f'{number} is not a prime number')
    elif n > 1:
        # Check from 2 to n-1
        for i in range(2, n):
            if n % i == 0:
                p = True
                break
    if p:
        print(f'{number} is not a prime number')
    else:
        print(f'{number} is a prime number')


# Write your code above this line 👆

# Do NOT change any of the code below👇
number = int(input("Check this number: "))
prime_checker(number)
