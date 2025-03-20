'''
workbook = planilha
sheet = pagina
'''

import openpyxl
import openpyxl.workbook

# criação de planilha
workbook = openpyxl.Workbook()

# mostrar sheets existentes
print(workbook.sheetnames)

# para criar novas sheets
workbook.create_sheet('Planilha 1')
workbook.create_sheet('Planilha 2')
workbook.create_sheet('Planilha 3')

# salvar modificações
#Criando o nome da planilha
workbook.save('endereços.xlsx')

# alterando o nome do sheet
workbook['Planilha 1'].title = 'Planilha 01'
workbook.save('endereços.xlsx')

# apagando um sheet
del workbook['Sheet']

print(workbook.sheetnames)
workbook.save('endereços.xlsx')
