#grafico de linhas

import matplotlib.pyplot as plt

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
valores = [4444, 3452, 23456, 3428, 8940, 7645]

plt.plot(meses, valores)
plt.xlabel('Meses')
plt.ylabel('Valores')
plt.title('Valor de vendas ao longo do tempo')

plt.show()