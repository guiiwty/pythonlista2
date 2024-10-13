def temperaturas_anuais():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    temperaturas = []

    for i in range(12):
        while True:
            try:
                temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Erro: Digite um valor numérico válido.")

    media_anual = sum(temperaturas) / 12
    print(f"\nMédia anual das temperaturas: {media_anual:.2f}°C")

    print("\nMeses com temperaturas acima da média anual:")
    for i in range(12):
        if temperaturas[i] > media_anual:
            print(f"{i + 1} - {meses[i]}: {temperaturas[i]:.2f}°C")

temperaturas_anuais()
