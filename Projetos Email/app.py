import smtplib
from email.message import EmailMessage


# configurações de login
EMAIL_ADDRESS = 'giovani.eb3@gmail.com'
EMAIL_PASSWORD ='cwsn sypq romc wmwr'

# criar e enviar email

mail = EmailMessage()
mail['Subject'] = 'Confirmação de email'
mensagem = '''
Me confirma que recebeu esse email. Cutuque o coleguinha do lado e informe o recebimento.
'''

mail['From'] =  EMAIL_ADDRESS
mail['To'] = 'alana.ambos@gmail.com'
mail.add_header('Content-Type','text/html')
mail.set_payload(mensagem.encode('utf-8'))
# servidor smtp + nome do provedor (outlook, gmail, yahoo)
# enviar email
with smtplib.SMTP_SSL('smtp.gmail.com',465) as email:
    email.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    email.send_message(mail)