# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(100)
# timmy.right(70)
# timmy.forward(100)
#
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
print(table)

table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
print(table)

table.align = 'r'
print(table)


