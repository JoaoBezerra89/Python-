estoque = []

estoque = []

while True:
    menu = int(input('''
    ---------MENU--------
    [1] Cadastrar Produto
    [2] Atualizar Produto
    [3] Remover Produto
    [4] Mostrar Estoque
    [5] Realizar Venda
    [6] Sair

                                                       
    Opção: ''' ))

    if menu == 1:
        produto = dict(
            nome = str(input('\nNome do Produto: ')).title(),
            quantidade = int(input('Quantidade em estoque: ')),
            preco = float(input('Preço Unitário: '))
        )

        estoque.append(produto)
        print('\nProduto cadastrado com sucesso!\n')

    elif menu == 2:
        nome = str(input('\nNome do produto: ')).title()
        for produto in estoque:
            if produto['nome'] == nome:
                produto['qtd'] = int(input('Nova quantidade: '))
                produto['preco'] = float(input('Novo preço: '))

                print('\nProduto atualizado com sucesso!\n')
                break
        else:
            print('\nProduto não cadastrado.\n')
    elif menu == 3:
        nome = str(input('\nNome do produto para remover: ')).title()
        for produto in estoque:
            if produto['nome'] == nome:
                estoque.remove(produto)
                print('\nProduto removido com sucesso!\n')
                break
        else:
            print('\nProduto não encontrado.\n')

    elif menu == 4:
        print('\nEstoque de Produtos: ')
        for produto in estoque:
            print('Nome:', produto['nome'])
            print('Quantidade:', produto['quantidade'])
            print('Preço:', produto['preco'])
            print('----------------------------')

    elif menu == 5:
        nome = str(input('\nNome do produto vendido: ')).title()
        quantidade_vendida = int(input('Quantidade Vendida: '))
        for produto in estoque:
            if produto['nome'] == nome:
                if quantidade_vendida <= produto['quantidade']:
                    produto['qtd'] -= quantidade_vendida
                    total_venda = quantidade_vendida * produto['preco']
                    print(f'\nTotal da venda: R${round(total_venda, )}')
                else:
                    print('\nQuantidade insuficiente em estoque.\n')
                break
        else:
            print('\nProduto não encontrado.\n')

    elif menu == 6:
        print('\nSaindo do sistema.\n')
        break

    else:
        print('\nOpção inválida!\n')