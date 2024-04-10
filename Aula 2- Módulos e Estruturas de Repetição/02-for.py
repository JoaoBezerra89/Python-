# """
# For >>> Utilizada quando se sabe a quantidade de repetições,
# de forma que é obrigatório determinar o final da execução do laço.

# Sintaxe:
# for item (variável) in iteravel:
#     bloco que será executado

# * Range -> inicio, fim, passo
# """
# sintaxe
# for contagem in range (2,10,2):
    #print(contagem)


   
    


# Crie um sistema que receba 4 notas 
# usar uma variavel soma para acumula as notas e 
# calcule a média, ao fim apresente a média e situção
# do aluno, sendo:
# > 7 aprovado, > 5 em recuperação e < 5 reprovado.


soma=0 # variavel que vai armazenar o acumulo do loop
for n in range (1,5):
    nota=float(input(f'Digite a {n}º nota:'))
    soma += nota     # += para incrementar +1
media=(soma/n)
if media >=7:
    print(f'Aprovado {media}')
elif media==5
print(f'Recuperação, {media}')
else:
    print(f'Reprovado')

print(f'Nota final é {media}')
