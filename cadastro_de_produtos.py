produtos = []  # Lista para armazenar os produtos


def cadastrar_produto():
    # Coletando informações do produto
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    
    # Validação do valor do produto
    while True:
        valor = input("Valor do produto: ")
        try:
            valor = float(valor)  # Tenta converter o valor para número
            break  # Se for válido, sai do loop
        except ValueError:
            print("Erro: Digite um valor numérico válido.")
    # Solicita se o produto está disponível e valida a resposta
    while True:
        disponivel = input("Disponível para venda? (sim/não): ").lower()
        if disponivel in ['sim', 'não']:
            break
        else:
            print("Erro: Responda apenas com 'sim' ou 'não'.")

    # Adicionando o produto à lista
    produtos.append((nome, descricao, float(valor), disponivel))

    # Confirmação do cadastro
    print(f"\nProduto '{nome}' cadastrado com sucesso!")


def listar_produtos():
    if not produtos:
        print("\nNenhum produto cadastrado ainda.")
    else:
        # Ordenando produtos pelo valor (do menor para o maior)
        produtos_ordenados = sorted(produtos, key=lambda p: p[2])

        print("\nListagem de Produtos (ordenados por valor):")
        for produto in produtos_ordenados:
            print(f"Nome: {produto[0]}, Valor: R${produto[2]:.2f}")


while True:
    print("\n1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")