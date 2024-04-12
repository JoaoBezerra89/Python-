#CADASTRO DE IMMC

usuarios = []

#Loop do menu principal

while True:
    print('\nMenu')
    print('1 - Inserir novo usuário')
    print('2 - Exibir dados dos usuários')
    print('3 - Exibir o IMC dos Usuários')
    print('4 - Deletar usuários')
    print('5 - Sair')

    opção=input('Escolha uma opção:')


#checagem das opções do menu
    if opção == '1':
        nome=input('Digite o nome do usuário: ')
        idade=int(input('Digite a idade do usuário: '))
        peso=float(input('Digite o peso do usuário: '))
        altura=float(input('Digite a altura do usuário: '))
        usuarios.append((nome, idade, peso, altura))
        print('Usuários adicionados com sucesso!')
    
    #opção da checagem numero 2 para a exibição do cadastro
        
    elif opção == '2':
        if usuarios:
            print('\nDados do usuário')
            for usuario in usuarios:
                nome, idade, peso, altura = usuario  #iteração
                print(f'Nome: {nome}, Idade: {idade}, Peso: {peso}, Altura: {altura}')

        else:
            print('Não há usuários cadastrados')

    elif opção == '3':
        if usuarios:
            print('\n IMC dos usuários')
            for usuario in usuarios:
                nome, idade, peso, altura=usuario
                imc=peso/(altura**2)
                print(f'{nome}: {imc:.2f}')

                if imc < 18.5:
                    print('IMC abaixo do peso')
                elif 18.5 <= imc <24.5:
                    print('IMC saudável')
                elif 24.5 <= imc <29.9:
                    print('IMC sobre peso')
                elif 29.9 <= imc <34.9:
                    print('IMC obesidade Grau I')
                elif 34.9 <= imc < 39.9:
                    print('IMC Obesidade Grau II')
                else:
                    print('IMC Obesidade Mórbida')

        else:
            print('Não há usuários cadastrados')

    elif opção == '4':
        if usuarios:
            #deletar usuários do cadastro IMMC
            nome_deletar=input('Digite o nome do usuário que deseja deletar: ')
            for usuario in usuarios:
                if usuario[0] == nome_deletar:
                    usuarios.remove(usuario)
                    print(f'Usuário {nome_deletar} deletado com sucesso')
                    break
            else:
                print(f'Usuário {nome_deletar} não encocntrado')

        else:
            print ('Não há usuários cadastrados')

    elif opção == '5':
        print('Encerrar o programa')
        break
    
    else:
        print('Opção inválida, por favor, escolha uma opção de 1 a 5')
        