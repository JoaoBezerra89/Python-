"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}


Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""
'''
compras = {'Alface': 0.45,
           'Batata':1.20,
           'Cenoura':8.00,
           'Ovo':10.00}

print(compras.keys()) #pode ser na mesma linha tbm print(compras.keys(), compras.values())
print(compras.values())
'''


# dados_cliente = {
#     'Nome' : 'Renan',
#     'Endereço' : 'Rua Cruzeido do Sul',
#     'Telefone' : '95654-2356'
#     }

# #inserir chave e valor no dicionário
# dados_cliente ['idade'] = 40
# print(dados_cliente)


#REMVENDO ITEM COM O POP
# dados_cliente = {
#     'Nome' : 'Renan',
#     'Endereço' : 'Rua Cruzeido do Sul',
#     'Telefone' : '95654-2356'
#     }

# dados_cliente.pop('Telefone')
# print(dados_cliente)


# compras = {'Alface': 0.45,
#            'Batata':1.20,
#            'Cenoura':8.00,
#            'Ovo':10.00}

# while True:
#     produdo = input('Digite o nome do produto, "fim" para terminar ').capitalize()
#     if produdo == 'fim':
#         break
#     if produdo in compras:
#         print(f'Preço {compras[produdo]:.2f}')
#     else:
#         print('Produto não encontrado')


#com outros ajustes
compras = {'Alface': 0.45,
           'Batata':1.20,
           'Cenoura':8.00,
           'Ovo':10.00}

while True:
    produdo = input('Digite o nome do produto, "fim" para terminar ').capitalize()
    if produdo == 'fim':
        break
    if produdo in compras:
        print(f'Produto: {produdo}, Preço R${compras[produdo]:.2f}')
    else:
        print('Produto não encontrado')

