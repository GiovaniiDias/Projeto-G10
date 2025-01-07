###DESAFIO 🥇
#1) Navegue até o site https://cursoautomacao.netlify.app/
#2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
#3) Clique em alerta, para gerar a alerta
#4) Feche a alerta
#5) Suba a página totalmente para cima
#6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
#7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"###

import pyautogui
import webbrowser
from time import sleep

#Acessando o site
webbrowser.open('https://cursoautomacao.netlify.app/')

# rolando até encontar a "exemplos de alertas"
pyautogui.moveTo(1480,300, duration=1)

for i in range(1):
    pyautogui.scroll(-1040)
    sleep(2)

pyautogui.click()
pyautogui.write('Giovani Dias')
 
 # criando o alerta
pyautogui.moveTo(1480,350,duration=0.5)
pyautogui.click()
sleep(1)
#fechando o alerta
pyautogui.hotkey('enter')

# subindo a tela 
for i in range(1):
    pyautogui.scroll(1100)
    sleep(2)
    #roland até os downloads

for i in range(2):
    pyautogui.scroll(-1100)
    sleep(2)

# clicando para baixar
pyautogui.click(957,649)
sleep(1)
pyautogui.click(1133,614)

sleep(1)
pyautogui.click(1336,644)

sleep(1)
pyautogui.click(1505,655)

sleep(1)
pyautogui.click(1012,767)

sleep(1)
pyautogui.click(1309,764)

sleep(1)

# emitindo alerta "voce terminou!"

pyautogui.alert('voce terminou!')
