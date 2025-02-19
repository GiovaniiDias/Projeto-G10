import webbrowser
import pyautogui
from time import sleep

mensagem = ('Teste de envio automatico de mensagem.')
#essa opção não usa o arquivo esterno TXT. Logo Remove o laço seguinte
# telefones = [ 5551983405464, 555196330402]
telefones =[]

# essa opção usa o arquivo externo TXT 
with open('Contatos.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(666,342)
    sleep(10)
    pyautogui.typewrite(f'{mensagem}')
    sleep(5)
    pyautogui.press('enter')