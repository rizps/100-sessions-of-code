# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# because the output of the input is always string we need to convert it to float
bmi = int(weight) / float(height)**2

print(round(bmi))
