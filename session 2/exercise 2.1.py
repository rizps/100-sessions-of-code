# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# first check the input data type
print(type(two_digit_number))
# we know that we can take some value in string
# so we take first and second value convert them to integer and then add them up
sum_of_2_digits = int(two_digit_number[0]) + int(two_digit_number[1])

print(sum_of_2_digits)