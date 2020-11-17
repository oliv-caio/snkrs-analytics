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
url = 'https://www.shop-pineapple.co/TENIS-nike?pagina=1'

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)

time.sleep(15)

site = "Pineapple Co"

for i in range(13):
    element = driver.find_element_by_id('listagemProdutos')
    #element = driver.find_element_by_xpath("//*[@id='listagemProdutos']")
    html_content = element.get_attribute("outerHTML")
    soup = BeautifulSoup(html_content, 'lxml')
    datetimedb = datetime.datetime.now()
    modelolist = []
    a_modelo = soup.find_all('a', {'class': 'nome-produto cor-secundaria'})

    for a in a_modelo:
        modelo = ''.join(a.findAll(text=True))
        modelolist.append(modelo)
        print(modelo)

    precolist = []
    a_preco = soup.find_all('strong', {'class': 'preco-venda cor-principal '})

    for a in a_preco:
        preco = str(''.join(a.findAll(text=True)))
        precolist.append(preco)
        print(preco)

    #for i in range(len(modelolist)):
        #print(modelolist[i])
        #print(precolist[i])
        #sql = """insert into site_reven (reven_html, reven_preco, reven_modelo, reven_data) values(%s, %s, %s, %s)""" 
        #val = (site, precolist[i], modelolist[i], datetimedb)
        #cursor.execute(sql, val)
        #sql = """insert into logs(html_logs, data_hora_logs, tipo_site) values(%s, %s, 0)"""
        #val = (site, datetimedb)
        #cursor.execute(sql, val)
        #db_conn.commit()
    
    driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/div[2]/div[3]/div/div/div/ul/li[8]/a").click()
    time.sleep(5)

driver.quit()
db_conn.close()