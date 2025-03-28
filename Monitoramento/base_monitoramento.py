from pickle import NEWFALSE
from watchfiles import watch
import os


# Qual o diretorio eu quero monitorar
diretorio = os.getcwd()

NEW_FILE = 1
MODIFIED = 2
DELETE = 3

for mudanca in watch(diretorio):
    for operacao in mudanca:
        tipo_operacao = operacao[0]
        arquivo = operacao[1]

        if tipo_operacao == NEW_FILE:
            print(f'Arquivo criado {arquivo}' )
        
        if tipo_operacao == MODIFIED:
            print(f'Arquivo MODIFICADO {arquivo}' )
        
        if tipo_operacao == DELETE:
            print(f'Arquivo EXCLUIDO {arquivo}' )