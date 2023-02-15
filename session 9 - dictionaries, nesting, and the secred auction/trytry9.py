# dictionary
makanan = {
    'nasi goreng': 'nasi goreng adalah makanan yang terbuat dari nasi yang digoreng',
    'mie goreng': 'mie goreng adalah makanan yang terbuat dari mie yang digoreng',
    'mie kuah': 'mie kuah adalah makananan yang terbuat dari mie yang dimasak dengan kuah',
}

# retrieving items from dictionary
print('-- a value in dictionary --')
print(makanan['nasi goreng'])

# adding a new item in dictionary
print('-- new item --')
makanan['seblak'] = 'seblak adalah makanan yang terbuat dari sayur-sayuran'
print(makanan['seblak'])

# create an empty dict
empty_dict = {}

# edit a dict value
print('-- edit a dict value --')
makanan['seblak'] = 'seblak adalah makanan yang terbuat dari sosis'
print(makanan['seblak'])

# print all the dictionary key and value
print('-- for loop --')
for i in makanan:
    print(i)  # key
    print(makanan[i])  # value


# ---
# nesting dict in a dict
travel_log = {
    'France': {'cities_visited':['paris', 'Lille', 'Dijon']},
    'Indonesia':{'cities_visited':['jombang','kediri', 'malang'], 'total_visits': 5}

}

# nesting dict in a list
travel_log2 = [
    {
        'country': 'France',
        'cities_visited':['paris', 'Lille', 'Dijon'],
         'total_visits':3

    },
    {
        'country': 'Indonesia',
        'cities_visited':['jombang','kediri', 'malang'],
         'total_visits': 5,
    },
]

# print(travel_log2)
print(travel_log2)

bid = {'yaya': 123, 'yoyo': 234, 'lala': 456}
print(bid["yoyo"])