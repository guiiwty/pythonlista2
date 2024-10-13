def calcular_media_idades():
    try:
        n = int(input("Quantas pessoas há na turma? "))
        if n <= 0:
            print("Erro: O número de pessoas deve ser maior que zero.")
            return

        idades = []
        for i in range(n):
            while True:
                try:
                    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
                    if idade >= 0:
                        idades.append(idade)
                        break
                    else:
                        print("Erro: A idade não pode ser negativa.")
                except ValueError:
                    print("Erro: Digite um número válido para a idade.")

        media = sum(idades) / n
        print(f"\nA média de idade da turma é: {media:.2f}")
        if 0 <= media <= 25:
            print("A turma é jovem.")
        elif 26 <= media <= 60:
            print("A turma é adulta.")
        else:
            print("A turma é idosa.")
            
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

calcular_media_idades()