def calcular_divida():
    try:
        divida_inicial = float(input("Digite o valor da dívida: R$ "))
        if divida_inicial <= 0:
            print("Erro: O valor da dívida deve ser maior que zero.")
            return
        
        tabela_juros = {
            1: 0,
            3: 10,
            6: 15,
            9: 20,
            12: 25
        }

        print(f"\n{'Valor da Dívida':<15} {'Valor dos Juros':<15} {'Parcelas':<15} {'Valor da Parcela':<15}")

        for parcelas, juros in tabela_juros.items():
            valor_juros = divida_inicial * (juros / 100)
            valor_divida = divida_inicial + valor_juros
            valor_parcela = valor_divida / parcelas
            print(f"R$ {valor_divida:,.2f} {'R$':<3}{valor_juros:,.2f} {parcelas:<15} R$ {valor_parcela:,.2f}")

    except ValueError:
        print("Erro: Digite um valor válido para a dívida.")

calcular_divida()