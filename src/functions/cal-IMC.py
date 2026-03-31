def calcular_imc(peso, altura):
    return peso / (altura ** 2)

print("--- BIENVENIDO A LA CALCULADORA DE IMC ---")

try:
    peso_usuario = float(input("Introduce tu peso en kg (ej. 75.5): "))
    altura_usuario = float(input("Introduce tu altura en metros (ej. 1.75): "))

    resultado_imc = calcular_imc(peso_usuario, altura_usuario)

    print(f"\nTu Índice de Masa Corporal es: {resultado_imc:.2f}")

except ValueError:
    print("Error: Por favor, introduce solo valores numéricos usando el punto (.) para decimales.")