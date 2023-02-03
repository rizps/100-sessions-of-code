# SESSION 2 - DATA TYPES

# previously we saw that we can know the lenght of some strings with len
print(len('Hello'))
# but we can't use it for integer
# e.g
# print(len(123))  # it will cause an error

# String
# the first character is always counting from zero
print("Hello"[0])
print("Hello"[1])
# concatenate a string
cs = "123" + "456"
print(cs)
# number in quotes is still called a string
print(type(cs))

# Integer
ci = 123 + 456
print(ci)
print(type(ci))
# type a large number
# e.g 23.500.000
# we can use underscore instead dot

#Float
a = 23.455_678
b = 12_987.654
c = 92_345_765
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

# Boolean
print(True)
print(False)

# ---

# we can't concatenate string with integer(number)
# but we can simply turn integer to string
# e.g.
# num_char = len(input('What is your name? '))
# # print("your name has " + num_char + "characters")  # this will cause an error
# new_num_char = str(num_char)
# print("your name has " + new_num_char + " characters")
# or convert to float and integer
print(float('100'))
print(int('100'))