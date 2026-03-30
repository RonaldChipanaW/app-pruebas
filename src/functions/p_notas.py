def calcular_promedio(lista_notas):
    if len(lista_notas) == 0:
        return 0  # Evita división por cero
    return sum(lista_notas) / len(lista_notas)