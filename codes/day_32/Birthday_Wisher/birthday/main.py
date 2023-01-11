import smtplib
import datetime as dt
from random import choice

# global variables
MY_EMAIL = "gustavo.100.days.of.code@gmail.com"
PASSWORD_APP = "ehtrnekaqypuuvkh"
RECIEVER_EMAIL = "gustavo.100daysofcode@yahoo.com"
text = "Subject::hello\n\n This is my message"
NOW = dt.datetime.now()
WEEK_DAY = NOW.weekday()


def pick_quote():
    new_line = '\n'
    with open("quotes.txt", "r") as quotes:
        lines = [line.strip("\n") for line in quotes]
    return f'Subject:Quote of the day!\n\n{choice(lines)}'

def send_email():
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD_APP)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=RECIEVER_EMAIL, 
            msg=pick_quote())

#send_email()
if WEEK_DAY == 2:
    send_email()