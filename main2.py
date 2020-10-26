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

db_conn = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="root", database="snkrs")
cursor = db_conn.cursor()

#1 preparar o conteudo html a partir da url
binary = FirefoxBinary('C:\\Program Files\\Firefox Developer Edition\\firefox.exe')
url = 'https://www.nike.com.br/Snkrs#calendario'

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)

time.sleep(15)



element = driver.find_element_by_xpath("/html/body/main/div/div[3]/section/div/div/div/div[@class='box-resultados vitrine-content--feed grid-produtos grid-produtos--3-col snkr-container']")
html_content = element.get_attribute("outerHTML")
soup = BeautifulSoup(html_content, 'lxml')

a_href = soup.find_all('a', href=True)

hreflist = []

for a in a_href:
    href = str(a['href'])
    hreflist.append(href)

for i in range(len(hreflist)):
    if hreflist[i-1] != hreflist[i] :
        url = hreflist[i-1]
        #print(url)
        driver.get(url)
        time.sleep(3)
        element = driver.find_element_by_xpath("/html/body/main/div/div[1]/div[3]/div/div[2]/div[@class='nome-preco-produto']")
        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, 'lxml') 
        modelo = soup.find_all('span')
        cw = soup.find_all('a')
        
        for node in modelo:
            #inserir no banco
            print (''.join(node.findAll(text=True)))
            
        for node in cw:
            #inserir no banco
            print (' '.join(node.findAll(text=True)))

        element = driver.find_element_by_xpath("/html/body/main/div/div[1]/div[3]/div/div[2]/div[2]/span/span/span[@class='js-valor-por']")
        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, 'lxml') 
        preco = soup.find_all('span')

        for node in preco:
            print (''.join(node.findAll(text=True)))

        element = driver.find_element_by_xpath("/html/body/main/div/div[1]/div[3]/div/div[2]/h3")
        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, 'lxml') 
        data = soup.find_all('h3')

        for node in data:
            print (''.join(node.findAll(text=True)))
        

driver.quit()


