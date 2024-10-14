import random

def par_ou_impar():
    escolha = input("Escolha Par ou Ímpar (P/I): ").lower()
    numero_usuario = int(input("Digite um número de 0 a 10: "))
    numero_computador = random.randint(0, 10)
    soma = numero_usuario + numero_computador

    resultado = "par" if soma % 2 == 0 else "ímpar"
    print(f"Você jogou {numero_usuario}, o computador jogou {numero_computador}. A soma é {soma} ({resultado}).")

    if (resultado == "par" and escolha == 'p') or (resultado == "ímpar" and escolha == 'i'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

par_ou_impar()