import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

choosen_word = random.choice(word_list).lower()
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print(choosen_word)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

guess = input('guess a letter: ').lower()
for i in choosen_word:
  if i == guess:
    print('right')
  else:
    print('wrong')