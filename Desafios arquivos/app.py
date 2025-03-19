import os

# exibir os arquivos da pasta desafio arquivos

print(os.listdir())

# monte e exiba o caminho(path) absoluto dos 3 arquivos da pasta atual(pasta desafio arquivos)

print(os.path.join(os.getcwd() + os.sep + 'relatorio.pdf' ))
print(os.path.join(os.getcwd() + os.sep + 'precos.txt' ))
print(os.path.join(os.getcwd() + os.sep + 'data_aniversario.xlsx' ))

# monte e exiba o caminho (path) dos arquivos que estão dentro da sub-pasta(desafio texto)

os.chdir('desafios texto')
print(os.getcwd())
print(os.path.join(os.getcwd() + os.sep + 'desafio_texto1.txt' ))
print(os.path.join(os.getcwd() + os.sep + 'desafio_texto2.txt' ))
print(os.path.join(os.getcwd() + os.sep + 'desafio_texto3.txt' ))

# navegue de volta para as 3 seguintes pastas, usando o os.chdir()

os.chdir(os.pardir)
print(os.getcwd())

 # 1 . navegue até a pasta desafio texto

os.chdir('desafios texto')
print(os.getcwd())  

 # 2. navegue de volta para a pasta desafio arquivos

os.chdir(os.pardir)
print(os.getcwd())       
    

    
 # 3. navegue para o diretorio pai da pasta desafio arquivos

os.chdir(os.pardir)
print(os.getcwd())

print('*'*5 + 'Desafio concluido com sucesso' +'*'*5)