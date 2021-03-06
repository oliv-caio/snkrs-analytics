import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


binary = FirefoxBinary('C:\\Program Files\\Firefox Developer Edition\\firefox.exe')
url = 'https://www.instagram.com/'

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)

element = driver.find_element_by_xpath('//*[@name="username"]')
print(element)
element.clear()
element.send_keys('self.username')