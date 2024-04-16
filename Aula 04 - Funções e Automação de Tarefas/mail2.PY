#Enviando email

import smtplib  #Biblioteca para enviar email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass  #Biblioteca para esconder senha do usuário

smpt_server = 'smtp-mail.outlook.com'
port = 587

username = 'joao.araujo.bezerra@outlook.com'
senha = getpass.getpass('Digite sua senha para continuar')

server = smtplib.SMTP(smpt_server)
server.starttls()
server.login(username,senha)

mensagem = MIMEMultipart()
mensagem ['From'] = 'joao.araujo.bezerra@outlook.com'
mensagem['To'] = 'joao.araujo.bezerra@outlook.com, joaobosco.arabez@gmail.com'
mensagem['Subject'] = 'Aula de Email Python'
corpo = 'O seu email foi enviado e recebido com sucesso!'
mensagem.attach(MIMEText(corpo,'plain'))
server.sendmail('joao.araujo.bezerra@outlook.com', 'joaobosco.arabez@gmail.com',mensagem.as_string())
server.quit()