# Conversor de temperatura em Python
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade de temperatura (C para Celsius, F para Fahrenheit): ")

if unidade.upper() == "C":
    fahrenheit = celsius_para_fahrenheit(temperatura)
    print("{:.2f} graus Celsius equivalem a {:.2f} graus Fahrenheit.".format(temperatura, fahrenheit))
elif unidade.upper() == "F":
    celsius = fahrenheit_para_celsius(temperatura)
    print("{:.2f} graus Fahrenheit equivalem a {:.2f} graus Celsius.".format(temperatura, celsius))
else:
    print("Unidade de temperatura inválida. Digite C ou F.")
