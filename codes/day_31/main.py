from tkinter import *
import pandas as pd
from tkinter import messagebox
from random import choice, randint

BACKGROUND_COLOR = "#B1DDC6"

# --------- DATA --------- #
# Loading the data
words = pd.read_csv("data/french_words.csv")

# Place holder for random_word
RANDOM_WORD = ""

# Create the data words_to learn
try:
    words_to_learn = pd.read_csv("data/words_to_learn.csv")
# Create data if it doenst exists
except FileNotFoundError:
    print("File not found, generating the file....")
    words.to_csv("data/words_to_learn.csv", index= False)
    words_to_learn = pd.read_csv("data/words_to_learn.csv")
finally:
    words_to_learn = words_to_learn.to_dict(orient="records")

# -------- FUNCTIONALITY -------- #

# ----- Remove a card and update the words_to_learn dataset
def remove_card():
    global words_to_learn
    # Remove the word from the dataset
    words_to_learn.remove(RANDOM_WORD)
    
    # Updates 
    update_words = pd.DataFrame.from_records(words_to_learn)
    update_words.to_csv("data/words_to_learn.csv")
    next_card()
    
# ---- Just pass to the next card
def next_card():
    # Define a random word
    global RANDOM_WORD, FLIP_TIMER

    flash_window.after_cancel(FLIP_TIMER)
    RANDOM_WORD = words_to_learn[randint(0,len(words_to_learn)-1)]
    # Substitute the random French word, fill and background
    flash_card.itemconfigure(flash_image, image=front_image)
    flash_card.itemconfigure(word, text = RANDOM_WORD["French"], fill = "black")
    flash_card.itemconfigure(language, text = "French", fill = "black")

    # Reseting flip timer
    FLIP_TIMER = flash_window.after(3000, func=change_cards)

# CHANGE CARDS
def change_cards():
    # Change background image, English translation and background
    flash_card.itemconfigure(flash_image, image=back_image)
    flash_card.itemconfigure(language, text="English", fill = "white")
    flash_card.itemconfigure(word, text = RANDOM_WORD["English"], fill = "white")
    

# ---------- UI ---------- #

# Main window
flash_window = Tk()
flash_window.config(height=700, width=900, bg=BACKGROUND_COLOR)


# -------- CARDS -------- #
# Front card
front_image = PhotoImage(file="images/card_front.png")
# Back card
back_image = PhotoImage(file="images/card_back.png")

flash_card = Canvas(height=520, width=810, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_image = flash_card.create_image(405, 260, image=front_image)


# Texts of the front card
# Language
language = flash_card.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
#Meaning
word = flash_card.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
#Packing up the card
flash_card.grid(row=0, column=0, columnspan=2, padx= 50, pady= 50)

# -------- BUTTONS --------- #
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command= remove_card)
right_button.grid(row=1, column=1)


# FIRST PASSAGE:
FLIP_TIMER  = flash_window.after(3000, func=change_cards)
next_card()


flash_window.mainloop()
