from docx import Document

documento = Document()

# Adicionando um titulo
documento.add_heading('Titulo do Documento', 0)
documento.save('demo.docx')

#add paragrafo
paragrafo = documento.add_paragraph('Um paragrafo simples ')

# add uma nova frase e destacando em 'bold' negrito
paragrafo.add_run('e super importante ').bold = True

# add uma nova frase
paragrafo.add_run('do autor ')

# add uma nova frase e destacando em italico
paragrafo.add_run('Giovani').italic = True

documento.save('demo.docx')
