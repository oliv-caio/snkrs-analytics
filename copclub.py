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
url = 'https://www.copclub.com.br/marca/nike.html'

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)

time.sleep(6)

site = "CopClub"

element = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/div/div[3]/ul")
html_content = element.get_attribute("outerHTML")
soup = BeautifulSoup(html_content, 'lxml')
datetimedb = datetime.datetime.now()

a_href = soup.find_all('a', href=True)

hreflist = []

for a in a_href:
    href = str(a['href'])
    hreflist.append(href)

for i in range(len(hreflist)):
    if hreflist[i-1] != hreflist[i] :
        url = hreflist[i-1]
        driver.get(url)
        time.sleep(1)
        element = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div/div[1]")
        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, 'lxml')
        modelo = soup.find_all('h1', {'class': 'nome-produto titulo cor-secundaria' })

        for node in modelo:
            modelodb = str(''.join(node.findAll(text=True)))
            print(modelodb)

        element = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[@class='principal']")
        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, 'lxml')
        preco = soup.find('strong', {'class': 'preco-promocional cor-principal'})
        precodb = str(''.join(preco.find(text=True)).strip())
        print(precodb)

        sql = """insert into site_reven (reven_html, reven_preco, reven_modelo, reven_data) values(%s, %s, %s, %s)""" 
        val = (site, precodb, modelodb, datetimedb)
        cursor.execute(sql, val)
        sql = """insert into logs(html_logs, data_hora_logs, tipo_site) values(%s, %s, 0)"""
        val = (site, datetimedb)
        cursor.execute(sql, val)
        db_conn.commit()
driver.quit()
db_conn.close()