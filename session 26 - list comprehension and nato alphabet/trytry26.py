# list comprehension
numbers = [1, 2,3]
# tradiotional method
new_number = []
for n in numbers:
    n +=1
    new_number.append(n)
print(new_number)

# with list comprehension
new_number2 = [n+1 for n in numbers]
print(new_number2)

doubled_number = [n*2 for n in range(1, 5)]
print(doubled_number)

names = ['agus', 'bagus', 'cagus', 'debagus', 'egus']
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)


# dictionary comprehension
import random
student_scores = {student:random.randint(50, 100) for student in names}
print(student_scores)

not_passed_students = {student:'not passed' for student in names if student_scores[student]<60}
print(not_passed_students)

passed_students = {student:score for (student, score) in student_scores.items() if score > 60}
print(passed_students)



student_dict = {
    'student' : ['angela', 'james', 'lily'],
    'scores' : [66, 87, 69]
}

# looping through dictionary
print('looping with dictionary')
print('key:')
for (key, value) in student_dict.items():
    print(key)
print('value:')
for (key, value) in student_dict.items():
    print(value)

# using pandas
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print('loop through dataframe:')
print(student_data_frame)
print('key:')
for (key, value) in student_data_frame.items():
    print(key)
print('value:')
for (key, value) in student_data_frame.items():
    print(value)

print('loop through rows of a data frame')
for index, row in student_data_frame.iterrows():
    print(row)
print('key:')
for index, row in student_data_frame.iterrows():
    print(row.student)
print('value:')
for index, row in student_data_frame.iterrows():
    print(row.scores)