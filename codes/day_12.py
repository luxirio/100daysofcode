#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." 
# depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, 
# only 5 guesses in hard mode).

def guessing_game():
    import random 
    #Defining the range of the numbers (1, 100):
    numbers = list(range(0,101))
    selected_number = random.choice(numbers)
    continue_playing = 'y'

    #Defining the level selection function
    def levels(user_selection):
        if user_selection == "hard":
            return 5
        else:
            return 10

    #printing logo/initial message:
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")

    #input of the user
    selection = input("Choose a difficulty. Type 'easy' or 'hard': ")
    #number of lives based on user selectiong
    lives = levels(selection)

    #Checking if it is working
    print(f'This is the selected number: {selected_number}')

    #creating a flag:
    guessed_number = False

    while lives > 0 and guessed_number == False:
        print(f'You have {lives} attempts remaining to guess the number')
        user_guess = int(input("Make a guess: "))
        
        if user_guess > selected_number:
            print("Too high.\nGuess again")
            lives -= 1
        elif user_guess < selected_number:
            print("Too low.\nGuess again.")
            lives -= 1
        elif user_guess == selected_number:
            print(f"You guessed the number!, the number was {selected_number}")
            guessed_number = True
            
    if lives == 0:
        print("You've run out of lives, try again!")
    
    continue_playing = input("Want to start again? Type 'y' to run again or 'n' to exit this game.")

    if continue_playing == "y":
        guessing_game()

guessing_game()