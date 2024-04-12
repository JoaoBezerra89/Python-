"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

"""

#*Criar uma lista de Produtos*
'''
produtos = ['Bacon',10.0, 'Ovos',12.0, 'Manteiga',8.50, 'Pão',10.50]
print(produtos)

#Acesso ao elementos da lista
print(f'O produto é {produtos[0]} e custa R$ {produtos[1]}')
'''

"""Fatiamento de itens da Lista"""
'''
#obter os dois primeiro elementos da lista [: indice]

produtos = ['Bacon',10.0, 'Ovos',12.0, 'Manteiga',8.50, 'Pão',10.50]
print(produtos[:2]) #ex se :2 vai pegar os elementos 0 e 1 do lado esquerdo (se os : estiver depois do 2 - no exemplo - será os dois ultimos valores da direita p esquerda)



#obter os elementos após o segundo elemento [indice :]
print(produtos[2:])


#Obter Trechos de uma Lista [indice inicial :indice final]
print(produtos[2:6])
print(produtos[-6 : -4]) #se colocar o sinal de ( - ) antes do  número do indice, ele vai fazer a busca invertida - de tras pra frente
'''

"""acessar os elementos de uma  lista usando indice negativo """

'''

#APPEND >>> Atribui a lista, um elemento por vez (no final da lista)
nomes=['Joana', 'Juliana', 'Pedro', 'Hendrique']
nomes.append('Ana') 
print(nomes)


#INSERT >>> Atribui vários elementos, integrando à lista original.
nomes.insert(1,'Katia')
print(nomes)


#POP >>> Remove um valor da lista por índice.

nomes.pop(2)
print(nomes)

#REMOVE >>> Remove um valor da lista por valor.

nomes.remove('Joana')
print(nomes)

#CLEAR >>> Limpa a lista.

nomes.clear()
print(nomes)
'''



#SORT >>> Ordena os dados de uma lista.

# nomes.sort()
# print(nomes)

nomes=['Joana', 'Juliana', 'Pedro', 'Hendrique']
nomes.sort 
print(nomes)


'''
#REVERSE >>> Inverte a lista.

nomes.reverse()
print(nomes)
'''

#Interar os itens de uma lista (vertical)
'''
cliente = ['Renan', 'Pedro', 'Lucas', 'Joana', 'Luan']
cliente.sort()
for nome in cliente:
    print(nome)
'''
# #INTERANDO EM UMA LISTA E ADICIONANDO ITENS NO FINAL DA LISTA   
# nomes=[]
# for nome in range(5): #"nome" porque as variáveis não podem ter o mesmo nome
#     nomes.append(str(input('Digite o nome do cliente')))
#     print(nomes)


'''
#Funções (Sum,Max,Min,Len,Count,Sort, Reverse)
numeros = [10,20,30,40,40,50,60,70,80]
print(sum(numeros)) #soma
print(max(numeros)) #maior valor
print(min(numeros)) #menor valor
print(len(numeros)) #quantidade de elementos da lista 


print(numeros.count(40)) #conta itens específicos da lista

numeros.sort() #ordena crescente
print(numeros)

numeros.reverse() #inverte a ordem da lista
print(numeros)
'''
'''
#VÁRIAS LISTAR
produto1 = ['Maçã', 2.50,'Pera',5.00]
produto2 = ['Uva',10,'Morango',2.00]
produto3 = ['Pão',10,'Leite',5.0]

compras=[produto1,produto2,produto3]
print(compras)

#concatenar listas

compras2 = produto1+produto2
print(compras2)
'''


#Lista usando estrutura com IF

# marcas_carro=['Audi','BMW','Mercedes'] #FAZENDO ITERAÇÃO SEMPRE USA FOR
# for item in marcas_carro:
#     print(item)
#     if(item=='BMW'):
#         break