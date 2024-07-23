def calcular_utilidades(P, U, GT):
    return P * U - GT

def calcular_razon_utilidades(Uactuales, Uanteriores):
    if Uanteriores == 0:
        return "No se puede calcular la razón con utilidades anteriores de 0."
    return Uactuales / Uanteriores

def main():
    try:
        P = float(input("Ingrese el precio de suscripción: "))
        U = int(input("Ingrese el número de usuarios: "))
        GT = float(input("Ingrese los gastos totales: "))
        Uanteriores = float(input("Ingrese las utilidades del año anterior: "))
        
        Uactuales = calcular_utilidades(P, U, GT)
        razon = calcular_razon_utilidades(Uactuales, Uanteriores)
        
        if isinstance(razon, str):
            print(razon)
        else:
            print(f"Las utilidades del proyecto son {Uactuales:.2f}")
            print(f"La razón entre las utilidades actuales y las del año anterior es {razon:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
