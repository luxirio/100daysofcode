from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

# Don't forget to export the TWITTER_PASSWORD environment variable

TWITTER_EMAIL = "luxirio12@gmail.com"
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')
MY_USERNAME = "@Gustavo55417008"

# 1) Open twitter page and login
driver = webdriver.Firefox()
driver.get("https://twitter.com/login")
sleep(5)

# Email
email_input = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
email_input.click()
email_input.send_keys(TWITTER_EMAIL)
email_input.send_keys(Keys.RETURN)
sleep(2)

# Username
username_input = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
username_input.send_keys(MY_USERNAME)
username_input.send_keys(Keys.RETURN)
sleep(2)

# Password
password_input = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password_input.send_keys(TWITTER_PASSWORD)
password_input.send_keys(Keys.RETURN)
sleep(2)
print(driver.title)
