def calcular_medias():
    medias = []
    alunos_acima_sete = 0

    for aluno in range(1, 11):
        print(f"\nAluno {aluno}:")
        notas = []
        for i in range(1, 5):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Erro: A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Erro: Digite um número válido para a nota.")

        media = sum(notas) / 4
        medias.append(media)

        if media >= 7.0:
            alunos_acima_sete += 1

    print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_acima_sete}")

calcular_medias()