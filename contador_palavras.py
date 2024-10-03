def contar_palavras():
    frase = input("Digite uma frase: ")
    palavras = frase.split()
    print(f"Total de palavras: {len(palavras)}")

contar_palavras()