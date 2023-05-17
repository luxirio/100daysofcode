from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

LOGIN_PAGE = "https://www.linkedin.com/jobs/search/?currentJobId=3452558156&f_WT=2&keywords=python%20developer"
USERNAME = "luxirio12@gmail.com"
PASSWORD = os.environ.get("MY_PWD")

driver = webdriver.Chrome()
driver.get(LOGIN_PAGE)
sleep(2)

# Step 1) sign in
sign_in_button = driver.find_element(By.XPATH, "/html/body/div[3]/a[1]")
sign_in_button.click()

user_name_field = driver.find_element(By.ID, "username")
user_name_field.clear()
user_name_field.send_keys("luxirio12@gmail.com")

password_field = driver.find_element(By.ID, "password")
password_field.clear()
password_field.send_keys(PASSWORD)

enter_button = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
enter_button.click()

# Get the links
# This part is still WIP
a = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
for element in a:
    try:
        element.click()
        driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button").click()
        sleep(1)
    except:
        print("Not clickable")
sleep(1000)
