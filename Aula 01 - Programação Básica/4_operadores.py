"""
Operadores Aritméticos e lógicos:

+  Adição           *  Multiplicação
-  Subtração        ** Exponenciação

/  Divisão
// Retorna o valor inteiro da divisão
%  Retorna o resto da divisão

>   Maior           ==  Igual
<   Menor           !=  Diferente

>=  Maior ou igual
<=  Menor ou igual
=   Atribuição
"""

a = 2
b = 3

print(a + b)   # adição
print(a - b)   # subtrair

print(a * b)   # multiplicar
print(a ** b)  # exp

print(a / b)   # divisão
print(a // b)  # divisão com valor inteiro
print(a % b)   # resto da divisão

print(a > b)   # [a] é maior que [b]?
print(a <= b)  # [a] é menor ou igual [b]?
print(a == b)  # [a] é igual [b]?
print(a != b)  # [a] é diferente de [b]?


#Criar uma soma com dois Valores exibir para o usuario  
numero1=100
numero2=50
resultado=numero1 + numero2
print(f'O resultado é {resultado}')



#Cálculo de Media com duas notas exibir para o usuario o resultado da média
nota1 = 10
nota2 = 8
media = (nota1 + nota2) / 2
print(f'Sua média é {media:.2f}') #:.xf sendo x o número de casas decimais que vc quer que apareça




# – Cálculo de aumento de salário
salario= 7000
reajuste = 0.1
aumento=salario+salario*reajuste
print(f'Seu aumento salarial é de {aumento}')