'''
monte um programa que cria a planilha com a estrutura abaixo e permuita que o usuario adicione dados a essa planilha
*Empresa
*Vaga
*data de aplicação
*Retorno
Nome da planilha "Acompanhamento de Vagas"
Nome do sheet "Vagas"

'''
import openpyxl
import openpyxl.workbook


workbook = openpyxl.Workbook()
del workbook['Sheet']

workbook.create_sheet('Vagas')
vagas = workbook['Vagas']

vagas.append(['Empresa','Vaga','Data de Aplicação','Retorno'])
workbook.save('Acompanhamento de Vagas.xlsx')

continuar = 's'
while continuar == 's':
    empresa = input('Empresa: ')
    vaga = input('Vaga: ')
    data_aplic = input('Data de Aplicação: ')
    retorno = input('Retorno: ')
    vagas.append([empresa,vaga,data_aplic,retorno])
    continuar = input('Adicionar outra vaga? (s/n)')
workbook.save('Acompanhamento de Vagas.xlsx')