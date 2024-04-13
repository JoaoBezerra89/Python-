"""
FUNÇÔES
Uma forma de organizar o código e garantir que ele 
possa ser reutilizado. Ideal que cada função seja 
responsável por uma tarefa...



>>>Sintaxe:
def nome_da_funcao(parametros):
    # Corpo da função
    # Instruções a serem executadas
    return valor_retornod
"""

# def: Palavra-chave usada para definir uma função.
 # nome_da_funcao: Nome dado à função para chamá-la posteriormente.
# parametros: Argumentos que a função pode receber (opcionais).
# return: Palavra-chave usada para retornar um valor da função (opcional).
    
    
    
'''    
# Função diz oi
def  diz_oi():
    print('Oi usário')
diz_oi()'''


'''
# Função canta parabéns
def cantar_parabens():
    print('Parabéns para você\nNessa data queria\nMuitas felicidades\nMuitos anos de vida')
cantar_parabens()
'''




'''  
# Função soma 2 valores
def soma():
    a = int(input('Digite o número 1'))
    b = int(input('Digite o número 2'))
    calc = a + b
    print(calc)
soma()
'''

'''1 -Exercicio : Média :Crie uma Função que Peça para o Usuario Entrar com 4 Notas, Se for >=7 aprovado Se não Reprovado'''

'''
def media():
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))
    nota4 = float(input('Digite a nota 4: '))

    calc_media = (nota1 + nota2 + nota3 + nota4) / 4
    print(calc_media)

    if calc_media >=7:
        print('Aprovado')
    else:
        print('Reprovado')

media()
'''




'''2-Exercicio:IMMC: Crie a entrada do usuário com Peso e Altura , faça o calculo do IMMC e mostre o resultado '''

'''
def imc():
    peso = float(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    calc_imc = peso/altura**2
   
    print(f'Seu IMC é {calc_imc}')

    if calc_imc < 18.5:
        print('Abaixo do peso')
    elif calc_imc >=18.5 and calc_imc <= 24.9:
        print ('Peso normal')
    elif calc_imc >=25.0 and calc_imc <=29.9:
        print ('Acima do peso')
    elif calc_imc >=30.0 and calc_imc <= 34.9:
        print('Obesidade classe I')
    elif calc_imc >=35.0 and calc_imc <=39.9:
        print('Obesidade classe II')
    else:
        print('Obesidade classe III')

imc()
'''

