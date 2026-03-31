def bolivianos_a_dolares(monto):
    """
    Convierte una cantidad de bolivianos a dólares estadounidenses.
    
    Args:
        monto (float): Cantidad en bolivianos a convertir
        
    Returns:
        float: Cantidad equivalente en dólares
    """
    tipo_cambio = 6.96  # 1 USD = 6.96 BOB
    dolares = monto / tipo_cambio
    return dolares

def main():
    """
    Función principal que ejecuta el conversor de divisas en consola.
    """
    print("=" * 40)
    print("   CONVERSOR DE BOLIVIANOS A DÓLARES")
    print("=" * 40)
    print(f"Tipo de cambio: 1 USD = 6.96 BOB")
    print("-" * 40)
    
    try:
        # Solicitar la cantidad al usuario
        monto_bolivianos = float(input("Ingrese la cantidad en bolivianos (Bs): "))
        
        # Validar que el monto no sea negativo
        if monto_bolivianos < 0:
            print("\n❌ Error: El monto no puede ser negativo.")
            return
        
        # Realizar la conversión
        dolares = bolivianos_a_dolares(monto_bolivianos)
        
        # Mostrar el resultado
        print("-" * 40)
        print(f"📊 Resultado de la conversión:")
        print(f"   {monto_bolivianos:.2f} Bolivianos = ${dolares:.2f} Dólares")
        print("-" * 40)
        
        # Mostrar información adicional
        print(f"💡 Para convertir {monto_bolivianos:.2f} BOB a USD:")
        print(f"   {monto_bolivianos:.2f} ÷ 6.96 = ${dolares:.2f}")
        
    except ValueError:
        print("\n❌ Error: Por favor, ingrese un número válido.")
        print("   Ejemplo: 100, 50.5, 1000")

# Ejecutar el programa
if __name__ == "__main__":
    main()