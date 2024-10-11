def romano_para_inteiro(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0

    for char in romano[::-1]:
        atual = valores[char]
        if atual < prev:
            total -= atual
        else:
            total += atual
        prev = atual

    print(f"Valor em decimal: {total}")

romano = input("Digite um número romano: ").upper()
romano_para_inteiro(romano)
