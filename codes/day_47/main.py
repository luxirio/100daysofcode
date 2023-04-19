import requests
from bs4 import BeautifulSoup
from pprint import pprint
import smtplib

# Getting the raw data from the live web!
url_amazon = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

request = requests.get(
    url=url_amazon,
    headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
    "Accept-Language": "en-US,en;q=0.5",}
    )

# Transforming the request text into a BeautifulSoup object
amazon_raw = request.text
amazon_soup = BeautifulSoup(amazon_raw, "lxml")

# Fetching the price
price = amazon_soup.select_one(".a-price-whole")
price = float(price.getText().strip("."))

# Setting up the e-mail
MY_EMAIL = "gustavo.100.days.of.code@gmail.com"
PASSWORD_APP = "lptryuwjqjnvelzh"
RECIEVER_EMAIL = "luxirio12@gmail.com"

def send_email():
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD_APP)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIEVER_EMAIL,
            msg=f"Subject:Price Alert from your Python Bot\n\nInstant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Saute, Yogurt Maker, Warmer and Sterilizer, Includes Free App with over 1900 Recipes, Stainless Steel, 3 Quart has is now {str(price)}, just now! Just go there! \n{url_amazon}"
        )

if price <= 99:
    send_email()

