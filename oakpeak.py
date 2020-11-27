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

binary = FirefoxBinary('C:\\Program Files\\Firefox Developer Edition\\firefox.exe')
url = 'https://oakpeak.com.br/product-category/nike/'

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)

time.sleep(10)

site = "Oak Peak"

for i in range(2):
    element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/ul")
    html_content = element.get_attribute("outerHTML")
    soup = BeautifulSoup(html_content, 'lxml')
    datetimedb = datetime.datetime.now()
    modelolist = []
    a_modelo = soup.find_all('h3', {'class': 'product-title fusion-responsive-typography-calculated'})

    for a in a_modelo:
        modelo = str(''.join(a.findAll(text=True)).strip())
        modelolist.append(modelo)

    precolist = []
    a_preco = soup.find_all('span', {'class': 'price'})

    for a in a_preco:
        preco = str(''.join(a.findAll(text=True)).strip())
        precolist.append(preco)

    for i in range(len(modelolist)):
        print(modelolist[i])
        print(precolist[i])
        sql = """insert into site_reven (reven_html, reven_preco, reven_modelo, reven_data) values(%s, %s, %s, %s)""" 
        val = (site, precolist[i], modelolist[i], datetimedb)
        cursor.execute(sql, val)
        sql = """insert into logs(html_logs, data_hora_logs, tipo_site) values(%s, %s, 0)"""
        val = (site, datetimedb)
        cursor.execute(sql, val)
        db_conn.commit()
    
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/nav/a[@class='next page-numbers']").click()
    time.sleep(3)

driver.quit()
db_conn.close()