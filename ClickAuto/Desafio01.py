# Desafio

# Crie um programa que pede o usuário e senha e na sequencia , copia e cola o usuario e a senha dentro de um bloco de notas

import pyautogui


email = pyautogui.prompt(text='Digite seu email', title= 'informações do usuario')

senha =pyautogui.password(text='Digite sua senha', title= 'informações do usuario', mask='*')

print(f'usuario: {email}  senha: {senha}')

pyautogui.moveTo(1205,369)
pyautogui.click()

pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)
