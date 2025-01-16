# 1 - Navegar até o site https://www.instagram.com/
# 2 -acessar com usuario e senha e logar
# 3 - pesquisar pagina e clicar na pagina
# 4 - clicar na postagem mais recente 
# 5 - verificar se ja foi curtida
# 6 - se já foi curtidca, não realizar nenhuma ação e pausar por 24h
# 7 - se ainda não foi curtida, curtir e deixar um comentario e pausar por 24h


import pyautogui
import webbrowser
from time import sleep

def curtido():
    pyautogui.alert('Já foi curtido e comentado!')
    
    


while True:

    # 1 - Navegar até o site https://www.instagram.com/
    webbrowser.open_new('https://www.instagram.com/')
    sleep(3)

    # 2 -acessar com usuario e senha e logar


    # 3 - pesquisar pagina e clicar na pagina
    pyautogui.click(69,251,duration=1)
    sleep(1)
    pyautogui.write('Adidas')
    sleep(2)
    pyautogui.click(254,252,duration=1)
    sleep(3)

    # 4 - clicar na postagem mais recente 
    pyautogui.scroll(-500)
    pyautogui.click(480,480,duration=1)
    sleep(3)

    # 5 - verificar se ja foi curtida
    #like = pyautogui.locateCenterOnScreen('likeTrue.png',confidence=0.9)
    #sleep(1)

    try: 
        like = pyautogui.locateCenterOnScreen('likeTrue.png',confidence=0.9)
    except pyautogui.ImageNotFoundException:
        like = None
        print('A imagem "likeTrue.png" não foi encotrada na tela ')

    # 6 - se já foi curtidca, não realizar nenhuma ação e pausar por 24h
    if like is not None:
        curtido()
        sleep(3)
        pyautogui.click(726,436)
        sleep(2) 

    # 7 - se ainda não foi curtida, curtir e deixar um comentario e pausar por 24h

    elif like == None:
        pyautogui.click(696,571,duration=1)
        sleep(1)
        pyautogui.click(737,577,duration=1)
        sleep(1)
        pyautogui.click(763,680,duration=1)
        sleep(1)
        pyautogui.typewrite(' Up!')
        pyautogui.click(1130,675,duration=1)
        sleep(2)








    pyautogui.alert('Hello Word!')