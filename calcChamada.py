def calculadora():
    while True:
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = int(input("Digite o número para a operação correspondente: "))

        if operacao == 0:
            print("Saindo da calculadora.")
            break
        elif operacao in [1, 2, 3, 4]:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

            if operacao == 1:
                resultado = num1 + num2
            elif operacao == 2:
                resultado = num1 - num2
            elif operacao == 3:
                resultado = num1 * num2
            elif operacao == 4:
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Erro: Divisão por zero"

            print("O resultado da operação é:", resultado)
        else:
            print("Essa opção não existe. Por favor, escolha uma opção válida.")

# Chamada da função
calculadora()
