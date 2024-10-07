import time

def contagem_regressiva():
    numero = int(input("Digite um número para a contagem regressiva: "))
    for i in range(numero, 0, -1):
        print(i)
        time.sleep(1)
    print("Tempo esgotado!")

contagem_regressiva()