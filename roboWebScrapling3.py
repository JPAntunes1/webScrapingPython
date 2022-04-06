from lib2to3.pgen2 import driver
from optparse import Option
from ssl import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print('Iniciando o robô... \n')



driver= webdriver.Chrome (r'C:\Users\User\Desktop\pythonbot/chromedriver')
driver.get("https://registro.br/")



# Escrever o que pesquisar
dominios = ['roboscompython.com.br', 'hotmart.com.br', 'uol.com.br', 'pythoncurso.com.br']

for dominio in dominios:

    # Clicar na barra de pesquisa
    pesquisa = driver.find_element_by_id("is-avail-field")

    # Limpar a barra de pesquisa
    pesquisa.clear()

    pesquisa.send_keys(dominio)

    # Dar enter na barra de pesquisa
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)

    # Localizar a disponibilidade no site
    driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong')

    # Escrever no terminal se está disponível ou não
    print('Domínio %s %s' %(dominio, driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))


driver.close()