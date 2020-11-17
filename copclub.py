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

#db_conn = mysql.connector.connect(host="129.213.131.233", port="600", user="root", passwd="root", database="snkrs")
#cursor = db_conn.cursor()

#1 preparar o conteudo html a partir da url
binary = FirefoxBinary('C:\\Program Files\\Firefox Developer Edition\\firefox.exe')
url = 'https://www.copclub.com.br/marca/nike.html'

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)

time.sleep(15)

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

modelolist = []
a_modelo = soup.find_all('a', {'class': 'nome-produto cor-secundaria'})

#for a in a_modelo:
        #modelo = ''.join(a.findAll(text=True))
        #modelolist.append(modelo)
        #print(modelo)

#precolist = []
a_preco = soup.find_all('strong', {'class': 'preco-promocional cor-principal'})

#for a in a_preco:
    #preco = str(''.join(a.findAll(text=True)).strip())
    #precolist.append(preco)
    #print(preco)

#a_travis = soup.find_all('strong', {'class': 'preco-venda cor-principal '})
#for a in a_travis:
#    travis = str(''.join(a.findAll(text=True)).strip())
#    precolist.append(travis)
#    #print(travis)

for i in range(len(hreflist)):
    if hreflist[i-1] != hreflist[i] :
        url = hreflist[i-1]
        #print(url)
        driver.get(url)
        time.sleep(4)
        element = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div/div[1]")
        #element = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/div")
        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, 'lxml')
        modelo = soup.find_all('h1', {'class': 'nome-produto titulo cor-secundaria' })

        for node in modelo:
            modelo = str(''.join(node.findAll(text=True)))
            print(modelo)

        element = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div/div[5]/div[1]/div[@class='preco-produto destaque-avista ']")
        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, 'lxml')
        preco = soup.find_all('strong', {'class': 'preco-promocional cor-principal'})
        for node in preco:
            preco = str(''.join(node.findAll(text=True)).strip())
            print(preco)
        #print(modelolist[i])
        #print(precolist[i])

        # sql = """insert into site_reven (reven_html, reven_preco, reven_modelo, reven_data) values(%s, %s, %s, %s)""" 
        # val = (site, precolist[i], modelolist[i], datetimedb)
        # cursor.execute(sql, val)
        # sql = """insert into logs(html_logs, data_hora_logs, tipo_site) values(%s, %s, 0)"""
        # val = (site, datetimedb)
        # cursor.execute(sql, val)
        # db_conn.commit()

driver.quit()
#db_conn.close()