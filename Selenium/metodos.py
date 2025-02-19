from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random


driver = webdriver.Chrome()
driver.get('https://google.com')


driver.get('Link do Site desejado') #navega até o site desejado
driver.maximize_window() #maximizar a tela
driver.refresh() # recarrega a pagina
driver.back() # volta para a pagina anterior
driver.forward() #avança uma pagina
print(driver.title) #obtem o titulo da pagina
print(driver.current_url) #obtem URL da pagina atual
print(driver.page_source) #obtem o codigo fonte da pagina 

#obtem o texto dentro de um elemento
print(driver.find_element(By.XPATH, '//a[@class="navbar-brand"]').text)
print(driver.find_element(By.XPATH, '//a[@class="navbar-brand"]').get_attribute("style"))


# digitar lentamente e aleatoriamente 
texto = 'texto que deseja colar e digitar naturalmentre'
paragrafo = driver.find_element(By.XPATH, "//textarea[@placeholder='digite seu texto aqui]")
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)

digitar_naturalmente(texto,paragrafo)



driver.close() #fecha a janela atual