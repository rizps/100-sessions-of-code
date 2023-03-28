#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt', mode='r') as n:
    namesr = n.readlines()
    names = []
    for i in namesr:
        names.append(i.replace('\n', ''))
    # print(names)

# there are no letters before this code executed
for n in names:
    with open('Input/Letters/starting_letter.txt') as l:
        letter = l.read()
        with open(f'Output/ReadyToSend/letter_for_{n}.txt', mode='w') as lf:
            new_letter = letter.replace("[name]", str(n))
            lf.write(new_letter)



