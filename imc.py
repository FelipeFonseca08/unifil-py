def calcular_imc(peso, altura):
    return peso / (altura*altura)

def ClassificarImc(imc):
    if imc < 18.5:
        return "Subpeso"
    elif imc < 24.9:
        return "Peso Normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade Classe I"
    elif imc < 39.9:
        return "Obesidade Classe II"
    else:
        return "Obesidade Classe III"
    
peso = 70
altura = 1.70


imc = calcular_imc(peso, altura)
classificacaoImc = ClassificarImc(imc)
print("\nIMC:", round (imc, 2))
print("Classificação do meu IMC:", classificacaoImc, "\n")
    