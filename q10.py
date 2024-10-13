def processar_notas():
    notas = []

    while True:
        try:
            nota = float(input("Digite uma nota (ou -1 para encerrar): "))
            if nota == -1:
                break
            if nota < 0 or nota > 10:
                print("Erro: A nota deve estar entre 0 e 10, ou -1 para encerrar.")
                continue
            notas.append(nota)
        except ValueError:
            print("Erro: Digite um valor válido.")

    if not notas:
        print("Nenhuma nota foi digitada.")
        return

    quantidade_notas = len(notas)
    print(f"\nQuantidade de valores lidos: {quantidade_notas}")

    print("\nValores na ordem informada:", end=" ")
    for nota in notas:
        print(f"{nota:.2f}", end=" ")

    print("\n\nValores na ordem inversa:")
    for nota in reversed(notas):
        print(f"{nota:.2f}")

    soma = sum(notas)
    print(f"\nSoma dos valores: {soma:.2f}")

    media = soma / quantidade_notas
    print(f"Média dos valores: {media:.2f}")

    acima_media = sum(1 for nota in notas if nota > media)
    print(f"Quantidade de valores acima da média: {acima_media}")

    abaixo_sete = sum(1 for nota in notas if nota < 7)
    print(f"Quantidade de valores abaixo de 7: {abaixo_sete}")

    print("\nPrograma encerrado. Obrigado!")

processar_notas()
