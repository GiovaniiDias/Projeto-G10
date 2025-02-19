import pyautogui

#tirar print tela toda
pyautogui.screenshot('tela.jpg')


#tirar print pontos especificos
pyautogui.screenshot('recorte.jpg', region=(904,80,611,715))
# sempre colocar o nome e a extenção. a região de corte (ponto de partida'904,80', para direita'611', para baixo'715')   
  