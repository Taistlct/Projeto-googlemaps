import os
from ast import Pass
from sys import displayhook
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
import time
import urllib
from easygui import *
import win32gui
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
from subprocess import CREATE_NO_WINDOW # This flag will only be available in windows
from pathlib import Path
import random
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#lendo a planilha
contatos_df = pd.read_excel("Contatos.xlsx", engine="openpyxl")
total = len(contatos_df.index)



agentes = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" ,
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		];

agente = agentes[random.randint(0, len(agentes) - 1)]

chrome_options = Options()
#chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--disable-application-cache")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3") 
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("user-agent=" + agente)
chrome_options.add_argument("user-data-dir=/path/to/your/custom/profile/")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-offline-load-stale-cache')
chrome_options.add_argument('--disk-cache-size=0')

#abrir navegador 
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=chrome_options)
maps = 'https://www.google.com.br/maps/'
driver.get(maps)


#Escondendo cmd do webdriver
def enumWindowFunc(hwnd, windowList):
    """ win32gui.EnumWindows() callback """
    text = win32gui.GetWindowText(hwnd)
    className = win32gui.GetClassName(hwnd)
    if 'chromedriver' in text.lower() or 'chromedriver' in className.lower():
        win32gui.ShowWindow(hwnd, False)
win32gui.EnumWindows(enumWindowFunc, [])

procurar = input(str('Digite aqui oque deseja procurar(Ex.Restaurante)'))
lugar = input(str('Digite qual lugar(Ex.Mogi das Cruzes)'))

procurar = procurar + ' ' + lugar
lista_lugares = []
lista_links = []

def scrool():
	# encontra o elemento
	elemento = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')

	# rola o elemento para baixo em 1000 pixels
	#driver.execute_script("arguments[0].scrollBy(0, 9000);", elemento)
	driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollBy(0, -200);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollBy(0, -300);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollBy(0, -200);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollBy(0, -200);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", elemento)
	time.sleep(1)
	driver.execute_script("arguments[0].scrollBy(0, -200);", elemento)

def pesquisar(procurar):
	
	#elementos
	campo_pesquisa = driver.find_element(By.ID, "searchboxinput")
	campo_pesquisa.send_keys(procurar)
	campo_pesquisa.send_keys(Keys.ENTER)
	time.sleep(2)
	
	scrool()
	scrool()
	scrool()

	wait = WebDriverWait(driver, 10)
	wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hfpxzc')))

	lista_lug_nave = driver.find_elements(By.CLASS_NAME, 'hfpxzc')
	for i in lista_lug_nave:
		url = i.get_attribute("href")
		lista_links.append(url)
	print(lista_links)

	

def consulta_dados():
	time.sleep(1)
	wait = WebDriverWait(driver, 10)
	for i in lista_links:
		lista_auxiliar = []
		driver.get(i)
		time.sleep(2)
		wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1')))
		nome_lugar = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1').text
		try:
			endreco_lugar = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[3]/button/div[1]/div[3]/div[1]').text
		except:
			endreco_lugar = 'não tem'
		try:
			telefone_lugar = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[6]/button/div[1]/div[3]/div[1]').text
		except:
			try:
				telefone_lugar = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[7]/button/div[1]/div[3]/div[1]').text
			except:
				try:
					telefone_lugar = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[9]/button/div[1]/div[3]/div[1]').text
				except:
					try:
						telefone_lugar = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[9]/button/div[1]/div[3]/div[1]').text
					except:
						telefone_lugar = 'não tem'

		lista_auxiliar.append(nome_lugar)
		lista_auxiliar.append(endreco_lugar)
		lista_auxiliar.append(telefone_lugar)
		lista_lugares.append(lista_auxiliar)
	
	


pesquisar(procurar)
print(len(lista_links))
consulta_dados()
for lista in lista_lugares:
	inseri = len(contatos_df) + 1
	contatos_df.loc[inseri] = lista
writer = pd.ExcelWriter("Contatos.xlsx", engine='openpyxl')
contatos_df.to_excel(writer, index=False)
writer.close()
print(lista_lugares)









