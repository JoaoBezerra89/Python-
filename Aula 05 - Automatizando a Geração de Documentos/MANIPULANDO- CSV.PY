#ARQUIVO CSS
'''
import csv
dados = [
['Maria', 'Maria@exemplo.com'],
['Joana', 'Joana@exemplo.com'],
['Pedro', 'Pedro@exemoplo.com']
]

with open('contatos.csv', 'w', newline='') as arquivo:
    escrever = csv.writer(arquivo)
    for linha in dados:
        escrever.writerow(linha)

'''

        
#Este código irá abrir o arquivo, ler cada linha e, 
#em seguida, imprimir cada linha para o console.

import csv

with open('contatos.csv', 'r') as arquivo:
    lendo = csv.reader(arquivo)
    for linha in lendo:
        print(linha[1])  #mudando o número dentro do [] as informações que retornam mudam, 0 - trás o primeiro nome, 1, 
                         #trás somente o email


