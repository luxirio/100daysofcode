
# Importing the modules
from turtle import clear
from art_day_14 import logo #importing the logo from the art file
from art_day_14 import vs  
from random import sample  #importing the sample function from the random module
from game_data_day_14 import data #importing the data from the data module

# Printing the game art logo
print(logo)
# We're going to access the data by choosing randomly the number with and accessing the keys manually (data[x]["name"])
# the keys are: "name", "folower_count", "description", "country"

# We need to compare two folower_counts and see which one is higher. First we need to pick 2 random integers and 
# the second needs to be different from the first so we use the sample function from the random module
chosen_ones = sample(data, 4) # I'm doing 4 because because the game that we've played has 3 attempts, we're going to start from that.
#defining initial score
score = 0
 
# We must define the function to compare who has more followers:
def more_followers(first_item, second_item):
    """Compare two dict items (names) and see which one has more followers"""
    first = chosen_ones[first_item]["follower_count"]
    second = chosen_ones[second_item]["follower_count"]
    #print(f"We're now comparing {first} with {second}")
    
    if first > second:
        return chosen_ones[first_item]["name"]
    else:
        return chosen_ones[second_item]["name"]

def check_user_guess(user_option, who_has_more):
    global score
    if user_option == who_has_more:
         print("You guessed correctly!")
         score = score + 1
         return 
    else:
        print(f"You are wrong, {who_has_more} has more followers")
        if score - 1 <= 0:
            return 
        else: 
            score = score - 1
            return 

#We can compare the first element with the second, the second turns the first and it repeats until its done comparing everything
def compare(chosen_ones):
    item_to_compare = 0
    
    while item_to_compare < (len(chosen_ones) - 1):
    
        print(f"A: {chosen_ones[item_to_compare]['name']} who is a {chosen_ones[item_to_compare]['description']} from {chosen_ones[item_to_compare]['country']} (psst, who has {chosen_ones[item_to_compare]['follower_count']})")
        a_option = chosen_ones[item_to_compare]['name']
        
        next = item_to_compare + 1
        print(vs)
        
        print(f"B: {chosen_ones[next]['name']} who is {chosen_ones[next]['description']} from {chosen_ones[next]['country']} (psst, who has {chosen_ones[next]['follower_count']}).\n")
        b_option = chosen_ones[next]['name']
        
        #We need to execute who has more followers before we assign the item to compare to the next
        who_has_more = more_followers(item_to_compare, next)
        
        #Ask the user to select an option
        user_option = input("Choose which has more followers?: Type 'A' or 'B': ")
        
        #changing the user option
        if user_option == "A":
            user_option = a_option
        elif user_option == "B":
            user_option = b_option
        
        #We now call a function to see if the user has guessed correctly:
        check_user_guess(user_option=user_option, who_has_more=who_has_more)
        
        print(f"\nYour current score is: {score}\n")
            
        item_to_compare = next

compare(chosen_ones= chosen_ones)
print(f"Thanks for playing! Your final score is {score}.")


