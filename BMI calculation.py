# Cálculo de IMC em Python
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = calcular_imc(peso, altura)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está com o peso ideal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
elif imc >= 30 and imc < 35:
    print("Você está com obesidade grau I.")
elif imc >= 35 and imc < 40:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade grau III.")
