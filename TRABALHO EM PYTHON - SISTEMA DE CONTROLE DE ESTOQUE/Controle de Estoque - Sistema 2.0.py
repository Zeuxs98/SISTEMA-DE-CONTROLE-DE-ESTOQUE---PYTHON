# Sistema de Controle de Estoque
# Trabalho de Coding - Python


def mostrar_menu():
    print()
    print("=" * 40)
    print("      CONTROLE DE ESTOQUE")
    print("=" * 40)
    print("1 - Cadastrar produto")
    print("2 - Listar estoque atual")
    print("3 - Registrar entrada de produto")
    print("4 - Registrar saída de produto")
    print("5 - Buscar produto pelo nome")
    print("6 - Ver valor total do estoque")
    print("0 - Sair")
    print("=" * 40)
    opcao = input("Escolha uma opção: ")
    return opcao


def ler_numero(mensagem):
    while True:
        texto = input(mensagem)
        try:
            numero = float(texto)
            if numero > 0:
                return numero
            else:
                print("Valor inválido! Digite um número maior que zero.")
        except ValueError:
            print("Valor inválido! Digite apenas números (use ponto, ex: 2.50).")


def ler_quantidade(mensagem):
    while True:
        texto = input(mensagem)
        try:
            quantidade = int(texto)
            if quantidade > 0:
                return quantidade
            else:
                print("Quantidade inválida! Digite um número maior que zero.")
        except ValueError:
            print("Quantidade inválida! Digite um número inteiro.")


def buscar_posicao(lista_produtos, nome):
    posicao = 0
    for p in lista_produtos:
        if p["nome"] == nome:
            return posicao
        posicao += 1
    return -1


def cadastrar_produto(lista_produtos):
    print()
    print("--- Cadastrar Produto ---")

    nome = input("Nome do produto: ")
    while nome == "":
        print("O nome não pode ficar vazio!")
        nome = input("Nome do produto: ")

   
    if buscar_posicao(lista_produtos, nome) != -1:
        print("Esse produto já está cadastrado!")
        return

    preco = ler_numero("Preço unitário (R$): ")
    quantidade = ler_quantidade("Quantidade inicial: ")

   
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
    }

    lista_produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def listar_estoque(lista_produtos):
    print()
    print("--- Estoque Atual ---")

    if len(lista_produtos) == 0:
        print("O estoque está vazio.")
    else:
        numero = 1
        for p in lista_produtos:
            print(f"{numero}. {p['nome']} | Preço: R$ {p['preco']:.2f} | "
                  f"Quantidade: {p['quantidade']}")
            if p["quantidade"] <= 5:
                print("   Atenção: estoque baixo!")
            numero += 1


def registrar_entrada(lista_produtos):
    print()
    print("--- Registrar Entrada ---")

    if len(lista_produtos) == 0:
        print("O estoque está vazio. Cadastre um produto primeiro.")
        return

    nome = input("Nome do produto: ")
    posicao = buscar_posicao(lista_produtos, nome)

    if posicao == -1:
        print("Produto não encontrado.")
    else:
        quantidade = ler_quantidade("Quantidade que entrou: ")
        lista_produtos[posicao]["quantidade"] += quantidade
        print("Entrada registrada! Novo estoque:",
              lista_produtos[posicao]["quantidade"])


def registrar_saida(lista_produtos):
    print()
    print("--- Registrar Saída ---")

    if len(lista_produtos) == 0:
        print("O estoque está vazio. Não há o que retirar.")
        return

    nome = input("Nome do produto: ")
    posicao = buscar_posicao(lista_produtos, nome)

    if posicao == -1:
        print("Produto não encontrado.")
    else:
        disponivel = lista_produtos[posicao]["quantidade"]
        quantidade = ler_quantidade("Quantidade que saiu: ")

        if quantidade > disponivel:
            print("Não é possível retirar", quantidade, "unidades.")
            print("Só existem", disponivel, "no estoque.")
        else:
            lista_produtos[posicao]["quantidade"] -= quantidade
            print("Saída registrada! Novo estoque:",
                  lista_produtos[posicao]["quantidade"])


def buscar_produto(lista_produtos):
    print()
    print("--- Buscar Produto ---")

    if len(lista_produtos) == 0:
        print("O estoque está vazio.")
        return

    nome = input("Digite o nome do produto: ")
    posicao = buscar_posicao(lista_produtos, nome)

    if posicao == -1:
        print("Produto não encontrado.")
    else:
        p = lista_produtos[posicao]
        print("Produto encontrado!")
        print("Nome:", p["nome"])
        print(f"Preço: R$ {p['preco']:.2f}")
        print("Quantidade:", p["quantidade"])


def calcular_valor_total(lista_produtos):
    total = 0
    for p in lista_produtos:
        total += p["preco"] * p["quantidade"]
    return total


def mostrar_valor_total(lista_produtos):
    print()
    print("--- Valor Total do Estoque ---")

    if len(lista_produtos) == 0:
        print("O estoque está vazio.")
    else:
        total = calcular_valor_total(lista_produtos)
        print("Produtos cadastrados:", len(lista_produtos))
        print(f"Valor total em estoque: R$ {total:.2f}")


def main():
    produtos = []  
    opcao = ""

    print("Bem-vindo ao Sistema de Controle de Estoque!")

    while opcao != "0":
        opcao = mostrar_menu()

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            listar_estoque(produtos)
        elif opcao == "3":
            registrar_entrada(produtos)
        elif opcao == "4":
            registrar_saida(produtos)
        elif opcao == "5":
            buscar_produto(produtos)
        elif opcao == "6":
            mostrar_valor_total(produtos)
        elif opcao == "0":
            print("Saindo do programa... Até a próxima!")
        else:
            print("Opção inválida! Escolha um número do menu.")


main()
