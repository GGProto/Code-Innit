from selenium import webdriver
from selenium.webdriver.remote.command import Command
import time
import random

browser = webdriver.Chrome("/Users/georgehill/Downloads/chromedriver")
def realisticTyping(elementName,text):
    browser.find_element_by_name(elementName).click()
    for letter in text:
        time.sleep(random.randint(1,100)/100)
        browser.find_element_by_name(elementName).send_keys(letter)