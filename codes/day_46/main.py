# Importing libraries
import requests
from bs4 import BeautifulSoup
import re

YEAR = "2000-08-12"
# URL endpoint
BILLBOARD_END = "https://www.billboard.com/charts/hot-100/"

# In order to do the request in the URL we need to append the date selection to the URL END
date_selection = input("Which year do you want to travel to? Type this date in this format YYYY-MM-DD: ")
request_url = f'{BILLBOARD_END}{date_selection}/'
request = requests.get(request_url)
# To text
billboard_site = request.text

# Creating a soup object
billboard_soup = BeautifulSoup(billboard_site, "html.parser")

# Retrieving the first and top 99
billboard_first = billboard_soup.find("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet",id="title-of-a-story").string.split()

billboard_rest = [' '.join(title.string.split()) for title in billboard_soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only",id="title-of-a-story")]

# Final list
music_list_100 = billboard_first + billboard_rest
