from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Acessing tinder website
WEB_ADDRESS = "https://tinder.com/"

driver = webdriver.Firefox()
driver.get(WEB_ADDRESS)
sleep(20)