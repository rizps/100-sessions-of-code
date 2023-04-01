# Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both files.

# with open('file1.txt') as f1:
#     numbers1 = f1.read()
#     list_num1 = [int(number) for number in numbers1 if number.isnumeric() == True]
#     print(list_num1)
# with open('file2.txt') as f2:
#     numbers2 = f2.read()
#     list_num2 = [int(number) for number in numbers2 if number.isnumeric() == True]
#     print(list_num2)
#
# # result = [over for over in list_num2 if over in list_num1]


# the right way
with open('file1.txt') as f1:
    data_num1 = f1.readlines()
    num1 = [int(num) for num in data_num1]
    print(data_num1)

with open('file2.txt') as f2:
    data_num2 = f2.readlines()
    num2 = [int(num) for num in data_num2]
    print(data_num2)
    print(num1)
    print(num2)

result = [int(num) for num in data_num1 if num in data_num2]

# Write your code above 👆

print(result)