#Enviando email

import smtplib  #Biblioteca para enviar email
import getpass  #Biblioteca para esconder senha do usuário

meu_email = 'joao.araujo.bezerra@outlook.com'
senha_email = getpass.getpass('Digitar sua senha para continuar')

#Lista de destinatário do email
lista_destinatario = ['joao.araujo.bezerra@outlook.com, joao.araujo.bezerra@outlook.com']

for destinatario in lista_destinatario:
    smtp = smtplib.SMTP('smtp-mail.outlook.com',587)
    smtp.ehlo() #Verificarçaõ da conexão do emaul
    smtp.starttls() #Verifica a criptografia do email
    smtp.ehlo() #fecha a conexão
    smtp.login(meu_email,senha_email)


    #Criar mensagem

    assunto = 'Curso de Python'
    conteudo = 'Email enviado com o código Python'
    mensagem = f'Subject: {assunto}\n\n\n{conteudo}'
    
    #envia email
    smtp.sendmail(meu_email, destinatario, mensagem)
    smtp.close()