import time
import requests
import pandas as pd
import mysql.connector
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import json

db_conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="")
#1 preparar o conteudo html a partir da url
binary = FirefoxBinary('C:\\Program Files\\Firefox Developer Edition\\firefox.exe')
url = 'https://www.nike.com.br/Snkrs#calendario'

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)

time.sleep(10)
#driver.find_element_by_xpath("//div[@class='nba-stat-table__overflow']//table//thead//tr//th[@data-field='PTS']").click()

#time.sleep(10)
#element = driver.find_element_by_xpath("//div[@class='box-resultados vitrine-content--feed grid-produtos grid-produtos--3-col snkr-container']//div//div[@class='produto__imagem']//div[@class='produto__detalhe']//h2[@class='produto__detalhe-titulo']")
element = driver.find_element_by_xpath("//div[@class='snkr-release__bottom']//a[@class='snkr-release__name']")
html_content = element.get_attribute("outerHTML")

#print(html_content)

#2 parsear counteudo Html - BeautifulSoup

soup = BeautifulSoup(html_content, 'lxml')

soup.findAll('a')
print(''.join(soup.findAll(text = True))) 
table = soup.find(name='div')

#3 estruturar o conteudo em um Data Frame Pandas
#df_full = pd.read_html(str(table))[0].head(10)
#print(dr)
#df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS' ]]
#df.columns = ['pos', 'player' , 'team', 'total']
#print(df_full)


#href nome modelo data em uma tabela -- outro bot para ler os href com preços e popular outra table

#4 Transformar os dados em um dicionario de dados próprio
#top10ranking = {}
#top10ranking['points'] = df.to_dict('records')
#print(top10ranking)

#5 Gravar os dados no banco 
#js = json.dumps(top10ranking)
#fp = open('test2_ranking.json', 'w')
#fp.write(js)
#fp.close()


#time.sleep(10)

driver.quit()


