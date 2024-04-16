#Módulo GetPass serve para ocultar uma senha, e é muito usado para login 

import getpass
username = input('Digite seu nome de usuário: ')
password = getpass.getpass('Digite sua senha: ')

print(f'Usuário: {username}\nSenha: {password}')
