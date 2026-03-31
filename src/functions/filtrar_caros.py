def filtrar_caros(precios, limite):
    resultado = []
    for precio in precios:
        if precio > limite:
            resultado.append(precio)
    return resultado


entrada = input("Ingresa los precios separados por coma: ")
precios = [float(x) for x in entrada.split(",")]

limite = float(input("Ingresa el límite: "))

print(filtrar_caros(precios, limite))
