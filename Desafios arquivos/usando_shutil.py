





# compacte o diretorio inteiro, para um arquivo chamado  backup arquivos python.zip

import shutil
import os
from time import sleep


# 1 copie o arquivo nome.txt para a pasta Arquivos 2010

# Descrevenco o caminho dos arquivos e das pastas
nome = os.getcwd() + os.sep + 'nome.txt'
arq2010 = os.getcwd() + os.sep + 'Arquivos 2010'

# copiando o arquivo nome para a pasta arquivos 2010
shutil.copy(nome, arq2010)
print('ação 1 execudata!')
sleep(5)

# 2 Mova o arquivo inscrições.pdf para a pasta documentação

inscri = os.getcwd() + os.sep + 'inscrição.pdf'
docs = os.getcwd() + os.sep + 'Documentação'
shutil.move(inscri, docs )
print('ação 2 execudata!')
sleep(5)

# 3 Faça uma copia da pasta arquivos 2010 e tudo oq tiver contido nela para uma nova pasta chamada beckup arquivos 2010
# como eu já criei o caminho da arq2010, só vou criar a pasta backup
backup_arquivos_2010 = os.getcwd() + os.sep + 'backup arquivos 2010'
shutil.copytree(arq2010, backup_arquivos_2010, dirs_exist_ok=True )
print('ação 3 execudata!')
sleep(5)

# 4 Compacte todo o conteudo da pasta Documentação no formato zip
shutil.make_archive('docs_zipado', 'zip', docs)
print('ação 4 execudata!')
sleep(5)

# 5 Mova o arquivo compactado para dentro dapasta backup
dcs_zp = os.getcwd() + os.sep + 'docs_zipado.zip'
bckup = os.getcwd() + os.sep + 'Backup'
shutil.move(dcs_zp, bckup )
print('ação 5 execudata!')
sleep(5)

# 6 Exclua o diretorio Arquivos 2010 e documentação e seus arquivos

shutil.rmtree(arq2010)
shutil.rmtree(docs)
print('ação 6 execudata!')

# 7 compacte o diretorio inteiro, para um arquivo chamado  backup arquivos python.zip
shutil.make_archive('backup_arquivos_python.zip', 'zip', os.getcwd())
print('ação 7 execudata!')
print('todas as ações concluidas!')