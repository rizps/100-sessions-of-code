import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
print(gray_squirrels_count)
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Color" : ['Gray', 'Red', 'Black'],
    "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_data = pd.DataFrame(data_dict)
print(new_data)
new_data.to_csv('squirrel_count.csv')
