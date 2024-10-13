def calcular_media():
    try:
        n = int(input("Quantas notas você quer inserir? "))
        if n <= 0:
            print("Erro: O número de notas deve ser maior que zero.")
            return

        notas = []
        for i in range(n):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i + 1}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Erro: A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Erro: Digite um número válido para a nota.")

        media = sum(notas) / n
        print(f"\nA média aritmética das {n} notas é: {media:.2f}")
        
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

calcular_media()
