from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

# Global
similar = "edgy_memes__"
USERNAME = "gustavo.100.days.of.code@gmail.com"
PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')
INSTAGRAM_ADDRESS = "https://www.instagram.com/"
print(f"This is your instagram password: {PASSWORD}")

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(f"{INSTAGRAM_ADDRESS}accounts/login/")
        sleep(3)

        email_field = self.driver.find_element(By.NAME, 'username')
        password_field = self.driver.find_element(By.NAME, 'password')

        email_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)
        sleep(5)


    def find_followers(self):
        self.driver.get(f"{INSTAGRAM_ADDRESS}{similar}")
        sleep(5)
        followers_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        sleep(5)
        scrollable_popup = self.driver.find_element(By.CLASS_NAME, '_aano')
        for i in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            sleep(2)
        sleep(5)

    def follow(self):
        buttons = self.driver.find_elements(By.CLASS_NAME, "_acan._acap._acas._aj1-")
        for button in buttons:
            try:
                button.click()
                sleep(1)
            except:
                print("You went into an exception!")
                self.driver.find_element(By.CLASS_NAME, "_a9--._a9_1").click()
                sleep(5)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()