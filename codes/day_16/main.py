from importlib.resources import is_resource
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

### Initialization of the program, printing logo and options for the user
print(logo)
print("Welcome to the Coffee Machine!\n by: @GHMS\n")

## Init of Menu, CoffeeMaker
machine_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

## Variable to control turn-on and off the machine
machine_is_on = True

## Checking what the user would like:
while machine_is_on:
    user_input = input("What would you like?: (latte/espresso/cappuccino): ")
    
    # Process the drink
    if user_input in machine_menu.get_items():
        # Transforming the user_input into an object
        drink_object = machine_menu.find_drink(user_input)
        
        # If there is resources:
        if coffee_maker.is_resource_sufficient(drink_object):
            #Process the money
            print(f'The selected drink costs: ${drink_object.cost}')
            money_machine.make_payment(drink_object.cost)
        
            # Make the drink!
            coffee_maker.make_coffee(drink_object)
        else: print("Sorry for the incovenience but there is not resources available to make your drink.")
        
    # To report the current resources available
    elif user_input == "report":
        print("The resources available are:")
        coffee_maker.report()
        print("\nThe total profit is:")
        money_machine.report()
    # To turn-off the machine    
    elif user_input == "off":
        machine_is_on = False
    
    