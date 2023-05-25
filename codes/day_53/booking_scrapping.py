# I have made this exercise for myself
# The idea is pretty simple, is to scrape some data from booking.com and then save it into a .csv file

# Importing dependencies
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Possible user inputs
BOOKING_ENDPOINT = "https://www.booking.com/"
DESTINATION = "Águas de Lindoia"
DATE_START = "sáb., 27 de mai."
DATE_END = "qui., 1º de jun."


class BookingInfo():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(BOOKING_ENDPOINT)
        sleep(3)
    
    def select_destination(self, destination):
        sleep(1)
        """
        Recieves a destination in a string format and inputs it on https://www.booking.com/ website

        Inputs: destination (name of the destination separated by space)
        """
        destination_input = self.driver.find_element(By.ID, ":Ra9:")
        destination_input.send_keys(destination)

    def date_start_end(self, date_start, date_end):
        sleep(1)
        """
        Used to input the period of time of the search

        Inputs: date_start (booking start date, the first day), date_end (booking final date, the last day)
        """
        date_start_input = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div/button[1]")
        date_end_input = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div/button[2]")

        self.driver.execute_script(f"arguments[0].innerText = '{date_start}'", date_start_input)
        self.driver.execute_script(f"arguments[0].innerText = '{date_end}'", date_end_input)
    
    def search(self):
        """
        Method to click the search button on booking website
        """
        sleep(2)
        search_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div[1]/div[4]/button")
        search_button.click()

    def page_source(self):
        """
        Return page source
        """
        sleep(5)
        source = self.driver.page_source
        return source

my_booking = BookingInfo()
my_booking.select_destination(destination=DESTINATION)
my_booking.date_start_end(date_start=DATE_START, date_end=DATE_END)
my_booking.search()
#Retrieving the page_source
my_booking_raw = my_booking.page_source()
