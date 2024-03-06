# Na chamada solicita ao usuário que insira nome, quantidade e valor unitário do produto,
# e caso os campos estejam preenchidos corretamente calcula o valor total do produto com base na quantidade e
# valor unitário e adiciona a lista_de_compras. Caso o produto já exista na lista soma as quantidades e valor total.
def adicionar_produto(lista_de_compras):
    while True:
        try:
            nome_do_produto = str(input("Insira o Nome do Produto: ")).strip().lower()
            quantidade_do_produto = int(input("Insira a Quantidade do Produto: "))
            valor_unitario_do_produto = float(input("Insira o Valor do Produto: "))
            if not (nome_do_produto and valor_unitario_do_produto):
                raise ValueError("Por Favor, Preencha Todos os Campos.")
            valor_total_do_produto = round(quantidade_do_produto * valor_unitario_do_produto, 2)

            for produto in lista_de_compras:
                if produto['Nome'] == nome_do_produto:
                    produto['Quantidade'] += quantidade_do_produto
                    produto['Valor Total'] += valor_total_do_produto
                    break
            else:
                informacoes_produto = {'Nome': nome_do_produto, 'Quantidade': quantidade_do_produto,
                                       'Valor Unitário': valor_unitario_do_produto,
                                       'Valor Total': valor_total_do_produto}
                lista_de_compras.append(informacoes_produto)
            print("Produto Adicionado com Sucesso!\n")
        except ValueError as e:
            print("Erro:", e)
            print("Por Favor, Preencha todos os campos Corretamente.\n")
        else:
            break


# Na chamada mostra os itens contidos na lista e o valor total de todos os produtos.
# Caso não haja itens cadastrados exibe uma mensagem.
def mostrar_produtos(lista_de_compras):
    if not lista_de_compras:
        print("Nenhum Item Cadastrado\n")
    else:
        valor_total_da_lista = 0
        for produto in lista_de_compras:
            valor_total_da_lista += produto['Quantidade'] * produto['Valor Unitário']

        for produto in lista_de_compras:
            print(f"""            Nome do Produto: {produto['Nome']}
            Quantidade: {produto['Quantidade']} 
            Valor Unitário: R${produto['Valor Unitário']} 
            Valor Total: R${produto['Valor Total']}\n""")
        print(f"Valor Total: {valor_total_da_lista}\n")


def remover_produto(lista_de_compras):
    nome_do_produto = str(input("Insira o Nome do Produto Que Deseja Remover: ")).strip().lower()
    for produto in lista_de_compras:
        if produto['Nome'] == nome_do_produto:
            quantidade_disponivel_do_produto = produto['Quantidade']
            print(f"Produto Encontrado: {produto['Nome']}")
            print(f"Quantidade Disponível: {quantidade_disponivel_do_produto}")

            try:
                quantidade_a_remover_do_produto = int(
                    input("Insira a Quantidade a Ser Removida ou '0' para Remover Todos os Itens: "))
                if quantidade_a_remover_do_produto < 0:
                    raise ValueError("A Quantidade a Ser Removida Não Pode Ser Negativa")
                if quantidade_a_remover_do_produto == 0:
                    lista_de_compras.remove(produto)
                    print("Todos os itens foram removidos com sucesso.")
                elif quantidade_a_remover_do_produto <= quantidade_disponivel_do_produto:
                    produto['Quantidade'] -= quantidade_a_remover_do_produto
                    produto['Valor Total'] -= produto['Valor Unitário'] * quantidade_a_remover_do_produto
                    print(f"{quantidade_a_remover_do_produto} item(s) removido(s) com sucesso.")
                else:
                    print("Quantidade a ser removida excede a quantidade disponível.")
            except ValueError as e:
                print("Erro:", e)
                print("Por favor, insira um valor inteiro maior ou igual a zero.\n")
            return

    print(f"Produto Não Encontrado\n")