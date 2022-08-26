# Program Requiremetns
# 1 - Printing a report
# Typing report returns the all the present resources (Water, Milk, Coffee and Money)

# 2 - Check the resources are sufficient?
# If resources are not sufficient to produce the chosen beverage, print "{resource} not available"

# 3 and 4 - Process coins (ONLY COINS) and check transaction success
# After asking how many coins of each are inserted, check if the value is less than required.
# If it is more than required, print back the {change}
# Else, print back "not enough money. Money refunded"

# 5 - Make coffe and deduct the resources

from day_15_menu import MENU, resources, art
from day_15_machine_functions import *

# The
machine_is_on = True

# Importing resources from menu file
current_resources = resources
machine_money = 0

print(f'\nWELCOME TO THE COFFEE MACHINE BUILT BY @GHMS!\n{art}')

while machine_is_on == True:
    #User input
    user_beverage = input("What would you like?: Type 'espresso', 'latte' or 'cappuccino': ")
    
    #If the user wants to shutdown the machine
    if user_beverage == "off":
        print("Turning the machine off. Thank you!")
        machine_is_on = False

    #Printing a report
    elif user_beverage == "report":
        report(resources = current_resources, money = machine_money)

    # If there are enough ingredients:
    elif (check_enough_ingredients(user_beverage, MENU= MENU, resources = current_resources)):
        #the value of the drink (to make the code more readable)
        drink_cost = MENU[user_beverage]["cost"]
        
        #Printing the cost of the user beverage
        print(f'The {user_beverage} costs ${drink_cost}. Please insert the coins.')
        user_value = process_coins()

        if user_value >= drink_cost:
            machine_money += drink_cost
            process_beverage(user_beverage, MENU = MENU, resources= current_resources)

            #If there is any change, print it
            if user_value > drink_cost:
                change = round((user_value) - (drink_cost), 3)
                print(f"You inserted {user_value} and the drink is {drink_cost}. Your change is {change}")
        else:
            print("Sorry, not enough money to buy the selected drink. Money refunded.")
    
    elif not (check_enough_ingredients(user_beverage, MENU= MENU, resources = current_resources)):
        print("There are not resources available to make your drink.")

    

    



