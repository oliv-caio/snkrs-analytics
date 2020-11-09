import time
import requests
import pandas as pd
import mysql.connector
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import json
import datetime

db_conn = mysql.connector.connect(host="129.213.131.233", port="600", user="root", passwd="root", database="snkrs")
cursor = db_conn.cursor()

#1 preparar o conteudo html a partir da url
binary = FirefoxBinary('C:\\Program Files\\Firefox Developer Edition\\firefox.exe')
url = 'https://alfasneakers.com.br/collections/tenis-nike'

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)

time.sleep(15)

element = driver.find_element_by_xpath("/html/body/main/div/div/div/div[3]/div/div[@class='product-list product-list--per-row-4 product-list--image-shape-natural']")
html_content = element.get_attribute("outerHTML")
soup = BeautifulSoup(html_content, 'lxml')

#a_href = soup.find_all('a', href=True)


# modelolist = []
# a_modelo = soup.find_all('div', {'class': 'product-block__title'})

# for a in a_modelo:
#      modelo = ''.join(a.findAll(text=True))
#      modelolist.append(modelo)

# precolist = []
# a_preco = soup.find_all('span', {'class': 'theme-money'})

# for a in a_preco:
#     preco = ''.join(a.findAll(text=True))
#     precolist.append(preco)

for i in range(13):
    element = driver.find_element_by_xpath("/html/body/main/div/div/div/div[3]/div/div[@class='product-list product-list--per-row-4 product-list--image-shape-natural']")
    html_content = element.get_attribute("outerHTML")
    soup = BeautifulSoup(html_content, 'lxml')
    modelolist = []
    a_modelo = soup.find_all('div', {'class': 'product-block__title'})

    for a in a_modelo:
        modelo = ''.join(a.findAll(text=True))
        modelolist.append(modelo)

    precolist = []
    a_preco = soup.find_all('span', {'class': 'theme-money'})

    for a in a_preco:
        preco = ''.join(a.findAll(text=True))
        precolist.append(preco)

    for i in range(len(modelolist)):
        print(modelolist[i])
        print(precolist[i])
    driver.find_element_by_xpath("/html/body/main/div/div/div/div[4]/div/a[@class='next']").click()
    time.sleep(8)

driver.quit()
db_conn.close()