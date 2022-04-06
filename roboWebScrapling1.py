from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome (r'C:\Users\User\Desktop\pythonbot/chromedriver')
driver.get("https://registro.br/")

# Clicar na barra de pesquisa
pesquisa = driver.find_element_by_id("is-avail-field")

# Limpar a barra de pesquisa
pesquisa.clear()

# Escrever o que pesquisar
pesquisa.send_keys("roboscompython.com.br")

# Dar enter na barra de pesquisa
pesquisa.send_keys(Keys.RETURN)


time.sleep(8)
driver.close()