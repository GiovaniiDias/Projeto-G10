#como pegar e arrastar arquivos para outro lugar?
import pyautogui

for i in range(3):

    # mover até uma coordenada
    pyautogui.moveTo(909,244,duration=0.8)
    # clicar 
    # arrastar até um ponto
    # soltar 
    pyautogui.dragTo(855,680,button="left", duration=0.8)
    # repetir 