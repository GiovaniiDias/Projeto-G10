import pyautogui
import pyperclip


pyautogui.moveTo(1205,369)
pyautogui.click()

def escrever_blocodenotas (frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')


escrever_blocodenotas('Automação é incrivel')