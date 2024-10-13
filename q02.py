def gerar_tabuada():
    while True:
        try:
            numero = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))
            if 1 <= numero <= 10:
                print(f"\nTabuada de {numero}:")
                for i in range(1, 11):
                    print(f"{numero} X {i} = {numero * i}")
                break
            else:
                print("Erro: O número deve estar entre 1 e 10.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

gerar_tabuada()