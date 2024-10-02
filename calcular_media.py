def calcular_media():
    numeros = input("Digite os números separados por espaço: ").split()
    numeros = [float(n) for n in numeros]
    media = sum(numeros) / len(numeros)
    print(f"A média dos números é: {media:.2f}")

calcular_media()