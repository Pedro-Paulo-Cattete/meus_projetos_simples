def contar_vogais():
    texto = input("Digite uma palavra ou frase: ").lower()
    vogais = "aeiou"
    contador = sum(1 for char in texto if char in vogais)
    print(f"Total de vogais: {contador}")

contar_vogais()