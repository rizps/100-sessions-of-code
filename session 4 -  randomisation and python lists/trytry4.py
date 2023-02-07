import random

random_integer = random.randint(1, 10) # will generate one random number from 1 to 10
print(random_integer)

random_float = random.random()
print(random_float)

# generate 5 random float number
float_list = []
for i in range(5):
    float_list.append(random_float)
print(float_list)

# generate a random float number between 0-5 not including 5
random_float_range = random.randrange(0, 5)
print(random_float_range)

# generate a random float number times 5, so it will generate random between 0-5 (0.00000.. - 4.99999..)
print(random_float * 5)

# ---

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)