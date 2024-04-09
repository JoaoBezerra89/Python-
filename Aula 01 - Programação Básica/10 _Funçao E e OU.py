
# E - condição lógica
# Para retornar o resultado verdadeiro, todo o teste lógico deve ser verdadeiro
# V V = V
# V F = F
# F V = F
# F F = F

"""Função And(E)"""

"""Situação
Se a média for Maior e igual a 7 E média Menor e igual 10
"Aluno Aprovado"

Se a media for Maior e Igual a 5 E media menor que 7
"Aluno de Recuperação"

se a media for maior e igual que 0 e media < 5
"aluno reprovado"

senão "Média invalida"

"""
# nome=str(input('Digite o nome do aluno:')).capitalize()
# matricula=int(input('Digite a matricula'))
# nota1=float(input('Digite a primeira nota'))
# nota2=float(input('Digite a segunda nota'))
# nota3=float(input('Digite a terceira nota'))
# media= (nota1+ nota2 + nota3) / 3

# if media >=7 and media <10:
#     print(f'Aluno Aprovado {media}')
# elif media >=5 and media <7:
#     print(f'Aluno em Recupração {media}')
# elif media >=0 and media <5:
#     print(f'Aluno Reprovado {media}')
# else:
#     print (f'Média invalida {media}')
# print(f'Media final do aluno - {nome} {matricula}: {media}')



# OU
# V V = V
# V F = V
# F V = V
# F F = F

""" Usando o Comando OR (ou)"""

""" 
lucas = 21
carolina=18

se idade de Lucas for >=18 ou idade carolina for >=18
então "Pelo menos um dos dois são de maior Idade"

"""
lucas=21
carolina=18

if lucas >=18 or carolina>=18:
    print('Pelo menos um dos dois indivíduos é de Maior')
else:
    print('Menor idade')
