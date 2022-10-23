def imc():
    IMC = peso / (altura*altura)

    if IMC<18.5:
        return "Bajo Peso"
    elif IMC>=18.5 and IMC<=25:
        return "Peso Saludable"
    elif IMC>=30:
        return "Obesidad"
    return "Sobrepeso"
    
print("Vamos a calcular tu índice de masa corporal. ")
peso = int(input("introduce tu peso en kilogramos: "))
altura = round(float(input("introduce tu altura: ")), 2)
print(imc())