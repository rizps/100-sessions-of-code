#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('welcome to the tip calculator')
bill = input("what was the total bill? ")
tip = input('what the total tip would you like to give? 10, 12, or 15%? ')
people = input('how many people to split the bill? ')

fl_bill = float(bill)
int_tip = int(tip)
int_people = int(people)

real_tip = int_tip/100 * fl_bill
real_bill = fl_bill + real_tip
each_person_pay = real_bill / int_people

print(round(each_person_pay, 2))

# other way
bill = float(input("what was the total bill? $"))
tip = int(input('what the total tip would you like to give? 10, 12, or 15%? '))
people = int(input('how many people to split the bill? '))

real_tip = tip/100 * bill
real_bill = bill + real_tip
each_person_pay = real_bill / people

print("{:.2f}".format(each_person_pay)) # use .2f to show zero comma -> 35.60 or 35.00

