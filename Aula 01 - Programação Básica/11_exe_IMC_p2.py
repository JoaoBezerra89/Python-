"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:


| Menor que 18.5      | Abaixo do peso       |
| >=18.5  E <= 24.9   | Peso Normal          |
| >= 25.0 E <= 29.9   | Excesso de peso      |
| >=30.0  E  <=34.9   | Obesidade classe I   |
| >=35.0  E  <=39.9   | Obesidade classe II  |
|caso contrário sera  | Obesidade classe III |

"""

nome=str(input("Digite o seu nome"))
idade=int(input("Digite sua idade"))
peso=float(input("Digite o seu peso"))
altura=float(input("Digite sua altura"))
IMC = peso/altura**2

print(f'Seu IMC é {IMC}')

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >=18.5 and IMC <= 24.9:
    print ('Peso normal')
elif IMC >=25.0 and IMC <=29.9:
    print ('Acima do peso')
elif IMC >=30.0 and IMC <= 34.9:
    print('Obesidade classe I')
elif IMC >=35.0 and IMC <=39.9:
    print('Obesidade classe II')
else:
    print('Obesidade classe III')



