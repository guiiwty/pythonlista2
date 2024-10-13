def caixa_registradora():
    while True:
        print("\nLojas Tabajara")
        total = 0.0
        contador_produto = 1

        while True:
            try:
                preco = float(input(f"Produto {contador_produto}: R$ "))
                if preco < 0:
                    print("Erro: O preço não pode ser negativo.")
                    continue
                elif preco == 0:
                    break
                total += preco
                contador_produto += 1
            except ValueError:
                print("Erro: Digite um valor válido para o preço.")

        print(f"Total: R$ {total:.2f}")

        while True:
            try:
                dinheiro = float(input("Dinheiro: R$ "))
                if dinheiro >= total:
                    troco = dinheiro - total
                    print(f"Troco: R$ {troco:.2f}")
                    break
                else:
                    print("Erro: O valor fornecido é menor que o total da compra.")
            except ValueError:
                print("Erro: Digite um valor válido para o dinheiro.")

        nova_compra = input("\nDeseja registrar uma nova compra? (s/n): ").lower()
        if nova_compra != 's':
            print("Encerrando o programa...")
            break

caixa_registradora()