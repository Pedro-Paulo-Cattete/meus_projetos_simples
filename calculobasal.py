# Fazer o Cálculo Basal para Homens e Mulheres


gender = (input('Você é homem ou mulher?(H/M) '))
if gender == "H" or "M":
    peso_ok = False
    altura_ok = False
    idade_ok = False
    
    while peso_ok == False: 
        peso = (input("Qual seu peso? Digitar apenas número e ponto: "))
        try:
            peso_float = float(peso)
            print('')
            peso_ok = True
        except:
            print("Por favor digite um peso válido. Lembre-se de usar apenas números e ponto. ")
    
    while altura_ok == False:
        altura = (input("Qual sua altura? Digitar apenas número e ponto. "))
        try:
            altura_float = float(altura)
            print('')
            altura_ok = True
        except:
            print("Por favor digite uma altura válida. Lembre-se de usar apenas números e ponto. ")
    
    while idade_ok == False:
        idade = (input("Qual sua idade? "))
        try:
            idade_float = float(idade)
            print('')
            idade_ok = True
        except:
            print("Por favor digite uma idade válida. Lembre-se de usar apenas números")

    print("Resultado do seu Cálculo Basal para os seguintes dados:")
    print(f"Peso: {peso_float} Kgs")
    print(f"Altura: {altura_float} m")
    print(f"Idade: {idade_float}")
    print("Resultado:")
    if gender == "H":
        print(f"{65 + (13.75 * peso_float) + (5.003 * (altura_float * 100)) - (6.75 * idade_float)}")
    elif gender == "M":
        print(f"{655 + (9.6 * peso_float) + (1.8 * (altura_float * 100)) - (4.7 * idade_float)}")
    else:
        print("Por favor Responda com H ou M")
else:
    print("Por favor Responda com H ou M")
