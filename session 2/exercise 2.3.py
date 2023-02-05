# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left
# if we live until 90 years old.
left = 90 - int(age)
days = left * 365
weeks = left * 52
months = left * 12

# e.g.
# You have 12410 days, 1768 weeks, and 408 months left.

print(f"you have {days} days, {weeks} weeks, and {months} months left ")
