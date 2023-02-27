from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
menu_i = MenuItem
money_machine = MoneyMachine()

print(menu.find_drink('latte'))

coffee_again = True
while coffee_again:
    choose = input(f"what would you like to choose? {menu.get_items()}: ")
    if choose == 'off':
        coffee_again = False
    elif choose == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choose)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
