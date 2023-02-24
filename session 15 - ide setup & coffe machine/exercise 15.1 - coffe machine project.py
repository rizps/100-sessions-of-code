MENU = {
    'espresso': {
        'ingredient': {
            'water': 100,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredient': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappucino': {
        'ingredient': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    },
}

available_stocks ={
    'ingredient': {
    'water': 700,
    'milk': 700,
    'coffee': 700,
    },
    'money': 0,
}

def coins():
    print("please insert coins. ")
    coin = 0
    coin = coin + int(input("how many quarters?: ")) * 0.25
    coin = coin + int(input("how many dimes?: ")) * 0.10
    coin = coin + int(input("how many nickles?: ")) * 0.05
    coin = coin + int(input("how many pennies?: ")) * 0.01
    return coin

def stock_calc():
    i = available_stocks['ingredient']
    l = MENU[choosee]['ingredient']
    for ii in i:
        for ll in l:
            if ii == ll:
                i[ii] = i[ii] - l[ii]
    return i

def stock_compare():
    i = available_stocks['ingredient']
    l = MENU[choosee]['ingredient']
    for ii in i:
        for ll in l:
            if ii == ll:
                if i[ii] < l[ii]:
                    return False

coffe_again = True
while coffe_again:
    choosee = input("would you like to choose? (espresso/latte/coppucino): ")
    if choosee == 'off':
        coffe_again = False
        print("goodbye")
    elif choosee != 'report':

        if not stock_compare():
            print("sorry there are not enough ingredients. type 'off' to turn the machine off")
            continue
        co = MENU[choosee]['cost']
        coin = coins()
        stock = stock_calc()
        if coin < co:
            print("sorry that's not enough money. money refunded")
            continue
        available_stocks['money'] += MENU[choosee]['cost']
        after_coin = round(coin - co, 2)

        print(f"here is {after_coin} in change")
        print(f"here is your {choosee}")
    elif choosee == 'report':
        mo = available_stocks['money']
        water = available_stocks['ingredient']['water']
        milk = available_stocks['ingredient']['milk']
        coffee = available_stocks['ingredient']['coffee']
        print(f"""
        Water = {water}ml
        Milk = {milk}ml
        Coffee = {coffee}gr
        Money = ${mo}
        """)


# other way, a.k.a. the instructor way
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





















