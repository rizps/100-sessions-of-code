# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     print(value)
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     print(row)
#     #Access row.student or row.score
#     print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# with open('nato_phonetic_alphabet.csv') as n:
#     nato_alphabet = n.read()
#     print(nato_alphabet)
df = pd.read_csv('nato_phonetic_alphabet.csv')
# print(df)

nato_alphabet = {row.letter: row.code for index, row in df.iterrows()}
print(nato_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def to_phonetic():
    word = input('type a word to be phonetic: ')
    phonetic_word = [nato_alphabet[w] for w in word.upper()]
    print(phonetic_word)

to_phonetic()

