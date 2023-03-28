# basic open file
my_file = open('my_text.txt')
file_contents = my_file.read()
print(file_contents)
my_file.close()  # close the file for memory saving

# next method
with open('my_text.txt') as file:
    contents = file.read()
    print(contents)

# write a new file
with open('some_file.txt', mode='w') as some_file:  # some_file.txt will generated when the file does not exist
    some_file.write("this is a new text")


