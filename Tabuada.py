def gerar_tabuada():
    numero = int(input("Digite um número: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

gerar_tabuada()
