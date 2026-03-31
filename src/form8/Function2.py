def bolivianos_a_dolares(monto):
    """
    Convierte una cantidad de dinero de bolivianos a dólares.
    
    Args:
        monto (float): Cantidad en bolivianos
    
    Returns:
        float: Cantidad equivalente en dólares estadounidenses
    """
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")
    
    tipo_cambio = 6.96  # 1 USD = 6.96 BOB
    dolares = monto / tipo_cambio
    return dolares

def dolares_a_bolivianos(monto):
    """
    Convierte una cantidad de dinero de dólares a bolivianos.
    
    Args:
        monto (float): Cantidad en dólares estadounidenses
    
    Returns:
        float: Cantidad equivalente en bolivianos
    """
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")
    
    tipo_cambio = 6.96  # 1 USD = 6.96 BOB
    bolivianos = monto * tipo_cambio
    return bolivianos

# Ejemplo de uso
if __name__ == "__main__":
    print("--- Conversor de Divisas ---")
    print("Tipo de cambio: 1 USD = 6.96 BOB")
    print()
    
    try:
        print("1. Bolivianos a Dólares")
        monto_bob = float(input("Ingrese el monto en bolivianos: "))
        dolares = bolivianos_a_dolares(monto_bob)
        print(f"{monto_bob:.2f} BOB = {dolares:.2f} USD")
        print()
        
        print("2. Dólares a Bolivianos")
        monto_usd = float(input("Ingrese el monto en dólares: "))
        bolivianos = dolares_a_bolivianos(monto_usd)
        print(f"{monto_usd:.2f} USD = {bolivianos:.2f} BOB")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
