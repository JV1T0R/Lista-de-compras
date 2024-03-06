import functions

lista_de_compras = []

while True:
    print('''    [1] Adicionar Produtos a Lista
    [2] Ver Lista de Produtos
    [3] Atualizar Produtos da LIsta
    [4] Remover Produto da Lista
    [5] Sair''')
    opcao = int(input("insira o número da opção para executa-la: "))
    print()

    if opcao == 1:
        functions.adicionar_produto(lista_de_compras)

    elif opcao == 2:
        functions.mostrar_produtos(lista_de_compras)

    elif opcao == 4:
        functions.remover_produto(lista_de_compras)

    elif opcao == 5:
        print("Progrma Encerrado")
        break

    else:
        print("Opção Inválida\n")