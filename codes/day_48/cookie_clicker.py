# Importing stuff
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import time, sleep

# Webdriver
driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Cookie object
cookie = driver.find_element(By.ID, "cookie")

# Clock mechanism
# Check each five seconds
check_time_seconds = 5
timeout = time() + check_time_seconds

while True:
    cookie.click()
    if time() >= timeout:
        current_money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        print(f"This is your current money {current_money}")

        # Get item and prices
        store_elements = driver.find_elements(By.CSS_SELECTOR, "#store b")
        items_and_prices = [item.text for item in store_elements[:len(store_elements)-1]]

        items = [item.split("-")[0].strip() for item in items_and_prices]
        prices = [int((price.split("-")[1].strip()).replace(",", "")) for price in items_and_prices]
        
        # Most affordable
        affordable = {}
        for item, price in zip(items, prices):
            if current_money >= price:
                affordable[item] = price
        max_affordable = "buy"+max(affordable, key=affordable.get)

        # Buy it
        print(f"You're buying the most affordable one: {max_affordable}")
        buy = driver.find_element(By.ID, max_affordable)
        buy.click()

        timeout = time() + check_time_seconds

