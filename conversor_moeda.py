def conversor_moeda():
    reais = float(input("Digite o valor em reais: R$ "))
    taxa = float(input("Digite a taxa de câmbio (R$/USD): "))
    dolares = reais / taxa
    print(f"Valor em dólares: ${dolares:.2f}")

conversor_moeda()