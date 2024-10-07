import random

def gerador_aleatorio():
    inicio = int(input("Digite o valor inicial: "))
    fim = int(input("Digite o valor final: "))
    print(f"Número aleatório: {random.randint(inicio, fim)}")

gerador_aleatorio()