def calculadora():
    while True:
        print("\n1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Escolha a operação: ")

        if escolha == '5':
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {num1 + num2}")
        elif escolha == '2':
            print(f"Resultado: {num1 - num2}")
        elif escolha == '3':
            print(f"Resultado: {num1 * num2}")
        elif escolha == '4':
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro: Divisão por zero não permitida.")
        else:
            print("Opção inválida.")

calculadora()
