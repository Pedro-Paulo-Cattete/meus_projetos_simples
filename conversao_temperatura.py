def conversor_temperatura():
    while True:
        print("\n1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Sair")

        escolha = input("Escolha a conversão: ")

        if escolha == '3':
            break

        temp = float(input("Digite a temperatura: "))

        if escolha == '1':
            print(f"{temp}°C é {temp * 9/5 + 32}°F")
        elif escolha == '2':
            print(f"{temp}°F é {(temp - 32) * 5/9}°C")
        else:
            print("Opção inválida.")

conversor_temperatura()
