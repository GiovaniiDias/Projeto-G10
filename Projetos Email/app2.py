from modulo_envio_de_email import Emailer


email = Emailer('email_do_usuario@email.com')


lista_contatos = ['wmail1@email.com', 'wmail4@email.com', 'wmail3@email.com', 'wmail2@email.com',]


mensagem = '''
mensagema  ser definada pelo usuario !
'''

email.definir_conteudo(topico='topico do email!', email_remetente='email_do_usuario@email.com',
lista_contatos = lista_contatos, conteudo_email = mensagem)


imagens = ['nome_img.jpg','nome_img2.jpg']
email.anexar_imagem(imagens)


arquivos = ['nome_dos_arquivos.jpg','nome_arquivo2.jpg']
email.anexar_arquivos(arquivos)
email.enviar_email(intervalo_em_segundos=24)

