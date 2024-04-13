


# Com retorno







# com mais de 1 retorno

#calculadora
def soma():
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    return n1 + n2

def subtracao():
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    return n1 - n2

def multiplicacao():
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    return n1 * n2

def divisao():
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    return n1 / n2


while True:
    escolha = int(input(f'Digite:\n[1] Somar\n[2] Subtrair\n[3] Multiplicação\n[4] Divisão\n'))
    if escolha == 1:
        print(f'O total da soma é: {soma():.2f}')
    elif escolha == 2:
        print(f'O total da subtração é: {subtracao():.2f}')
    elif escolha == 3:
        print(f'O total da multiplicação é: {multiplicacao():.2f}')
    elif escolha == 4:
        print(divisao())
    else:
        print('Opção Inválida')



  
    
    
  
        
        


    
    