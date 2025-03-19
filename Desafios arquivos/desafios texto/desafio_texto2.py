# crie 3 listas
 # lista com 5 frutas
 # lista com 5 cores
 # lista com 5 liguagens de programação

import os


fruitas = ['maça','banana','melão','morango','laranja']
colors = ['azul','branco','vermelho','preto','amarelo']
linguagem_programa = ['php','python','java','typescript','c++']

# Desafio 1
 # crie um novo arquivo chamado 'frutas.txt' e insira dentro dele todos as 5 frutas que estão na lista de frutas

with open('frutas.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for tipo in fruitas:
        arquivo.write(str(tipo)+os.linesep)

# Desafio 2
 # imprima na tela todas as linhas que estão no arquivo 'frutas.txt'

with open('frutas.txt', 'r',newline='',encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)

# Desafio 3
 # Sem apagar os dados que já estão dentro do 'frutas.txt' , adicione todas as cores que estão dentro da sua lista de cores ao arquivos 'frutas.txt'
with open('frutas.txt', 'a', newline='', encoding='utf-8') as arquivo:
    for cores in colors:
        arquivo.write(str(cores)+os.linesep)


# Desafio 4
 # Crie um novo arquiovo chamado 'top 5 linguagem de programação' e popule o arquivo , de forma com que cada linguagem ocupe apenas uma linha 

with open('top5linguagens_programacao.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for codigo in linguagem_programa:
        arquivo.write(str(codigo)+os.linesep)

with open( 'top5linguagens_programacao.txt', 'r',newline='',encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)