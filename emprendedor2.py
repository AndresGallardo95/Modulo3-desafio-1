def calcular_utilidades(P, Unormal, Upremium, GT):
    P_premium = P * 1.5
    return (P * Unormal) + (P_premium * Upremium) - GT

def main():
    try:
        P = float(input("Ingrese el precio de suscripción para usuarios normales: "))
        Unormal = int(input("Ingrese el número de usuarios normales: "))
        Upremium = int(input("Ingrese el número de usuarios premium: "))
        GT = float(input("Ingrese los gastos totales: "))
        utilidades = calcular_utilidades(P, Unormal, Upremium, GT)
        print(f"Las utilidades del proyecto son {utilidades:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
