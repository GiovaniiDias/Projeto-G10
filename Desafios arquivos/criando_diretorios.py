import os
#Crie um novo diretorio dentro do diretorio atual, chamado "arquivos"
try:
    if not os.path.isdir('Arquivos'):
        os.mkdir('Arquivos')
    else:
        print('Diretorio já foi criado')
except OSError:
    print('Esse diretorio já existe')
#Em um outro comando , crie um novo diretorio "arquivos" chamado "arquivos pdf"
try:
    if not os.path.isdir('Arquivos PDF'):
        os.mkdir('Arquivos PDF')
    else:
        print('Diretorio já foi criado')
except OSError:
    print('Esse diretorio já existe')


#em apenas uma linha crie o diretorio "fotos" e dentro o sub diretorio "fotos verão"
try:
    if not os.path.isdir('Fotos'):
        os.makedirs('Fotos' + os.sep + 'Fotos Verão')
    else:
        print('Diretorio já existe')
except OSError:
 print('Diretorio já existe!')