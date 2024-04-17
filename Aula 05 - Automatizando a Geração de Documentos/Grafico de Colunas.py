#grafico de colunas
import matplotlib.pyplot as plt

categorias = ['janeiro', 'fevereiro', 'março', 'abril']
valores = [20, 30, 60, 80]

#criar o gráfico de colunas
bars =plt.bar(categorias, valores)

#adicionar os rótulos dos valores
plt.bar_label(bars,labels=valores,label_type='edge')

#adicionar rotulos de categoria
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Valores de Vendas')

#mostrar o gráfico
plt.show()