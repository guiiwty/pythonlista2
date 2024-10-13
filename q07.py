def lanchonete():
    cardapio = {
        100: {"nome": "Cachorro Quente", "preco": 1.20},
        101: {"nome": "Bauru Simples", "preco": 1.30},
        102: {"nome": "Bauru com Ovo", "preco": 1.50},
        103: {"nome": "Hambúrguer", "preco": 1.20},
        104: {"nome": "Cheeseburguer", "preco": 1.30},
        105: {"nome": "Refrigerante", "preco": 1.00}
    }

    total_geral = 0.0

    while True:
        print("\nCardápio:")
        for codigo, item in cardapio.items():
            print(f"{item['nome']} (Código: {codigo}) - R$ {item['preco']:.2f}")

        try:
            codigo = int(input("\nDigite o código do item (ou 0 para encerrar o pedido): "))
            if codigo == 0:
                break

            if codigo not in cardapio:
                print("Erro: Código inválido. Tente novamente.")
                continue

            quantidade = int(input(f"Digite a quantidade de {cardapio[codigo]['nome']}: "))
            if quantidade <= 0:
                print("Erro: A quantidade deve ser maior que zero.")
                continue

            valor_item = cardapio[codigo]["preco"] * quantidade
            total_geral += valor_item
            print(f"{quantidade}x {cardapio[codigo]['nome']} - Total: R$ {valor_item:.2f}")

        except ValueError:
            print("Erro: Entrada inválida. Digite números válidos.")

    print(f"\nTotal geral do pedido: R$ {total_geral:.2f}")
    print("Pedido encerrado. Obrigado!")

lanchonete()