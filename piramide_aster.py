def piramide():
    linhas = int(input("Digite o número de linhas: "))
    for i in range(1, linhas + 1):
        print(' ' * (linhas - i) + '*' * (2 * i - 1))

piramide()