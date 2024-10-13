def validar_nome():
    while True:
        nome = input("Digite seu nome: ")
        if len(nome) > 3:
            return nome
        else:
            print("Erro: O nome deve ter mais de 3 caracteres.")

def validar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if 0 <= idade <= 150:
                return idade
            else:
                print("Erro: A idade deve estar entre 0 e 150.")
        except ValueError:
            print("Erro: Digite um número válido para a idade.")

def validar_salario():
    while True:
        try:
            salario = float(input("Digite seu salário: "))
            if salario > 0:
                return salario
            else:
                print("Erro: O salário deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um número válido para o salário.")

def validar_sexo():
    while True:
        sexo = input("Digite seu sexo (f/m): ").lower()
        if sexo in ['f', 'm']:
            return sexo
        else:
            print("Erro: Sexo deve ser 'f' para feminino ou 'm' para masculino.")

def validar_estado_civil():
    while True:
        estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        else:
            print("Erro: Estado civil deve ser 's' (solteiro), 'c' (casado), 'v' (viúvo) ou 'd' (divorciado).")
def main():
    nome = validar_nome()
    idade = validar_idade()
    salario = validar_salario()
    sexo = validar_sexo()
    estado_civil = validar_estado_civil()

    print("\nInformações validadas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")
if __name__ == "__main__":
    main()
