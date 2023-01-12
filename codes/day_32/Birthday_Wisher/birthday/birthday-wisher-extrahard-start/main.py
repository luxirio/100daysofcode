##################### Extra Hard Starting Project ######################
# Importing libraries
import pandas as pd
import datetime as dt
import smtplib
from random import choice
import os
# Importing the data
birthdays = pd.read_csv("birthdays.csv")
# Global variables
# My email and connection data
MY_EMAIL = "gustavo.100.days.of.code@gmail.com"
PASSWORD = "ehtrnekaqypuuvkh"
# Date
NOW = dt.datetime.now()
MONTH = NOW.month
DAY = NOW.day
# Templates of the letters and correspondent dir
letter_templates_folder = "letter_templates"
templates = os.listdir(letter_templates_folder)
LETTERS_LIST = [f'{letter_templates_folder}/{template}' for template in templates]

# ---- FUNCTIONALITY ---- #
# Retrieve the birthdays of today
birthdays_today = birthdays[(birthdays["day"] == (DAY)) & (birthdays["month"] == (MONTH))]
names_list = list(birthdays_today["name"])
emails_list = list(birthdays_today["email"])

# Function to replace and write the letter
def pick_letter_replace_name(name):
    letter = choice(LETTERS_LIST)
    print(f"Choosing the letter file... {letter} for {name}")
    with open(letter, "r") as message:
        final_message = [line.replace("[NAME]", name) for line in message]
    return print("".join(final_message))

# 4. Send the letter generated in step 3 to that person's email address.
def send_email(message, reciever_email):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=reciever_email,
            msg=message)
        print(f"Email sent succefully for {reciever_email}")

#send_email(message=f'Subject:Test\n\n{pick_letter_replace_name(NAME_TEST)}', reciever_email=EMAIL_TEST)
for name, email in zip(names_list, emails_list):
    send_email(message=f'Subject:Happy Birthday\n\n{pick_letter_replace_name(name=name)}',reciever_email=email)