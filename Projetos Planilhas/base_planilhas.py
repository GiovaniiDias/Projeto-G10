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


# colocaando cabeçalho
# criando uma variavel com o nome da sheet, para facilitar a chamada
sheet_planilha01 = workbook['Planilha 01']
#cabeçlho
sheet_planilha01.append(['rua','cep','casa'])
workbook.save('endereços.xlsx')

# adicionar dados na linha
sheet_planilha01.append(['endereço 1','numero cep 1', 'casa 1'])
sheet_planilha01.append(['endereço 2','numero cep 2', 'casa 2'])
sheet_planilha01.append(['endereço 3','numero cep 3', 'casa 3'])
sheet_planilha01.append(['endereço 4','numero cep 4', 'casa 4'])
workbook.save('endereços.xlsx')

# adicionando dados pelo endereço da cedula
sheet_planilha01['A6'].value = 'endereço 5'
sheet_planilha01['B6'].value = 'numero cep 5'
sheet_planilha01['C6'].value = 'casa 5'