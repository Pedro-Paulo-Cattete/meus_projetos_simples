def conversor_horas():
    horas = float(input("Digite o valor em horas: "))
    minutos = horas * 60
    segundos = horas * 3600
    print(f"{horas} horas são {minutos:.0f} minutos ou {segundos:.0f} segundos.")

conversor_horas()