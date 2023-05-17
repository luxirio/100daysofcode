from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

TWITTER_EMAIL = "luxirio12@gmail.com"
# Don't forget to export the environment variable of your password
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')
MY_USERNAME = "@Gustavo55417008"

# INTERNET PARAMETERS
PROMISED_UP = 10
PROMISED_DOWN = 300

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self) -> tuple:
        """ 
        Get the internet speed using the speedtest.net, returning a tuple of upload and download values
        """
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test.test-mode-multi")
        go_button.click()
        sleep(80)
        self.down = self.driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed").text
        return (self.up, self.down)

    def tweet_at_provider(self) -> None:
        """
        Tweet the upload and download values obtained from the get_internet_speed method.
        """
        self.driver.get("https://twitter.com/login")
        sleep(3)
        # Email
        email_input = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.click()
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.RETURN)
        sleep(2)

        # Username
        username_input = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        username_input.send_keys(MY_USERNAME)
        username_input.send_keys(Keys.RETURN)
        sleep(2)

        # Password
        password_input = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        sleep(2)

        # send message
        message = f"Hey, internet service provider, why I am getting {self.down}down/{self.up}up speed when I am paying {PROMISED_DOWN}down/{PROMISED_UP}up speed?"
        print(message)
        sleep(5)
        text_box = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
        text_box.click()
        text_box.send_keys(message)
        send_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send_tweet.click()
        sleep(5)
        print("Your message was tweeted.")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

# Final comment:
"""
The function to do the tweeting could be less repetitive, but either way, that is a good exercise for the use of selenium;
"""