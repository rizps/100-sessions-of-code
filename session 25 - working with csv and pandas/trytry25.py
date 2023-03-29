# import pandas as pd
# import csv
#
# # open csv file with readlines
# with open('weather_data.csv') as data_file:
#     data_open = data_file.readlines()
#     print('-----> open csv file with readlines <-----')
#     print(data_open)
#
# # open csv file with csv library
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     print('-----> open csv file with csv library <-----')
#     for row in data:
#         print(row)
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     print('-----> open csv file with csv library <-----')
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)
#
# # open csv file with pandas
# data = pd.read_csv('weather_data.csv')
# print('-----> open csv file with pandas <-----')
# print(data)
# print(data['temp'])
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# average = 0
# for t in temp_list:
#     average += t
# average /= len(temp_list)
# print(f'the temperature average is {round(average, 2)}')
# average2 = sum(temp_list)/len(temp_list)
# print(average2)
#
# average3 = data['temp'].mean()
# print(average3)
# print(data['temp'].max())
#
# # get data in column
# print(data['day'])
# print(data.day)
#
# # get data in row
# print(data[data['temp'] == data['temp'].max()])
#
#
# # create dataframe from scratch
# data_dict = {
#     'students' : ['ami', 'angela', 'john'],
#     'scores' : [78, 86, 79]
# }
# data = pd.DataFrame(data_dict)
# print(data)


import pandas as pd
data = pd.read_csv('us-states-game-start/50_states.csv')
print(data.state)
y = data[data.state == 'Ohio'].y
print(type(y))
print(int(y))
y2 = data.astype({'y' : 'int'})
print(type(y2))
print(y2)

word = 'good job guys'
print(word.title())
print(word.capitalize())
