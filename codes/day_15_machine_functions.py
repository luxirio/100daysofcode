#Functions of the coffee machine


def report(resources, money):
        print("The current resoruces values are:")
        for ingredient, quantity in resources.items():
            print(f'{ingredient.title()}: {quantity}')
        print(f'The current money in the machine is: {money}')


def check_enough_ingredients(beverage, MENU, resources):
    is_enough = True
    for ingredient, value in MENU[beverage]["ingredients"].items():
        if resources[ingredient] < value:
            is_enough = False
    return is_enough


def process_coins():
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    total = ((quarters*25) +( dimes*10) + (nickles*5) + (pennies))/100
    return total 


def process_beverage(beverage, resources, MENU):
    for ingredient, value in MENU[beverage]["ingredients"].items():
        resources[ingredient] -= value
    print("Thank you! Enjoy your drink!☕")