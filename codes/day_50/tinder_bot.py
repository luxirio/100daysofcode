from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

EMAIL = "gustavo.100.days.of.code@gmail.com"

# 1) LOG IN ON TINDER
driver = webdriver.Chrome()
driver.get("https://tinder.com/")

# 1.1) Click the button to log in
login_button = driver.find_element(By.XPATH, "//*[@id='u-1779218560']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]")
login_button.click()
sleep(5)

# 1.2) Click the button to 
login_with_fb = driver.find_element(By.XPATH, '//*[@id="u787367660"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
login_with_fb.click()
sleep(2000)

# 