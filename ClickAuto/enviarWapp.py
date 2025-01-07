import pyautogui
import pyperclip

# função para usar caracteres especiais 
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

# clicar na guia (acaso não esteja aberto a paguina)
pyautogui.moveTo(1333,12,duration=0.5)

pyautogui.click()

# clicar no campo de msg
pyautogui.moveTo(1460,977,duration=1)

pyautogui.click()
# frase desejada
escrever_frase('Este é um teste de automação')
# clicar no botão de envio 
pyautogui.click(1637,978,duration=1)