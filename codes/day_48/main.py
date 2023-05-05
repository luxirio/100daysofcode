# Importing the webdriver, By and Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initializing driver
driver = webdriver.Firefox()
driver.get("http://www.python.org")

event_elements = driver.find_elements(By.CLASS_NAME, "event-widget li a")
date_elements = driver.find_elements(By.CLASS_NAME, "event-widget time")

events = {}
for i in range(len(event_elements)):
    events[i] = {'time': date_elements[i].get_attribute("datetime").split("T")[0], 'name':event_elements[i].text}

driver.close()
