from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import re
import requests

RENTAL_LINK = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.663674728765756%2C%22north%22%3A37.88673992016921%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
FORM_LINK = "https://forms.gle/ktwz8W7DQqPhdqSA8"
SHEETY_ENDPOINT="https://api.sheety.co/350d5e8fc7a69a08e3f7c6d3de3b111e/sfAutomation/table"


# Another approach to the same problem
driver = webdriver.Firefox()
driver.get(RENTAL_LINK)
sleep(3)
zillow_raw = driver.page_source

# Transforming the request into a BeautifulSoup object
zillow_soup = BeautifulSoup(zillow_raw, "html.parser")

# GETTING ALL THE INFO
cards = zillow_soup.find_all("a", class_="property-card-link")
prices = zillow_soup.find_all("span", attrs={"data-test": "property-card-price"})
addressess = zillow_soup.find_all("address")

# We discovered that the links are doubled so we can skip every other 2 using slicing;
links_raw = [card.get("href") for card in cards[0::2]]
prices_raw = [price.text for price in prices]
address_raw = [address.text for address in addressess]

# Proper format of each information
links = []
prices = []
address = address_raw

for link in links_raw:
    if "https" not in link:
        links.append(f"https://www.zillow.com/{link}")
    else:
        links.append(link)

for price in prices_raw:
    match = re.search(r'\$([\d,]+)', price)
    if match:
        dollar_amount = match.group(1)
        prices.append(f"${dollar_amount}")

# Add into a google sheets
for location, price, link in zip(address, prices, links):
    data = {
        "table":{
            "address": str(location),
            "price": price,
            "link": link
        }
    }
    add_row = requests.post(SHEETY_ENDPOINT, json=data)
