def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).
    
    Args:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
    
    Returns:
        float: Valor del IMC calculado
    """
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero")
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que cero")
    
    imc = peso / (altura ** 2)
    return imc

# Función para mostrar el resultado con categoría
def interpretar_imc(imc):
    """
    Interpreta el valor del IMC según la clasificación de la OMS.
    
    Args:
        imc (float): Valor del IMC
    
    Returns:
        str: Categoría del IMC
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Ejemplo de uso
if __name__ == "__main__":
    try:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        
        imc = calcular_imc(peso, altura)
        categoria = interpretar_imc(imc)
        
        print(f"Su IMC es: {imc:.2f}")
        print(f"Categoría: {categoria}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
