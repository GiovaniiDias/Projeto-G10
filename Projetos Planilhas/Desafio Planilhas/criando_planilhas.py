import openpyxl
import openpyxl.workbook

worbook = openpyxl.Workbook()

# deletando a sheet padrao
del worbook['Sheet']

# nome da planilha deve ser passado somente depois de criar as primeiras sheets
#worbook.save('computadores.xlsx')

#Criando a sheet 1
worbook.create_sheet('Produtos')

produtos = worbook['Produtos']

# cabeçalho
produtos.append(['computador', 'ano','preço'])
worbook.save('computadores.xlsx')

# adicionando linhas e dados nas linhas
produtos.append(['Computador 1', '2001' , 500])
produtos.append(['Computador 2', '2002' , 1000])
produtos.append(['Computador 3', '2003' , 1500])
produtos.append(['Computador 4', '2004' , 2500])
produtos.append(['Computador 5', '2005' , 3000])
worbook.save('computadores.xlsx')

