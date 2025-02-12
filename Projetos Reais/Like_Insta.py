import pyautogui
import webbrowser
from time import sleep

# 1 - Navegar até o site
webbrowser.open_new('https://www.instagram.com/')

# 2 - login e senha 

pyautogui.click(1230,330, duration=1)


# senha
pyautogui.click(1203,376, duration=1)

# Não salvar logs de entada

pyautogui.click('', duration=1)

# procurar por pagina 

pyautogui.click(876,270, duration=1)