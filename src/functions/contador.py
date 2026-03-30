def contar_vocales(texto):
    vocales = "aeiou"
    contador = 0
    for letra in texto.lower():  # convierte todo a minúsculas
        if letra in vocales:
            contador += 1
    return contador