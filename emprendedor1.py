def calcular_utilidades(P, U, GT):
    return P * U - GT

def main():
    try:
        P = float(input("Ingrese el precio de suscripción: "))
        U = int(input("Ingrese el número de usuarios: "))
        GT = float(input("Ingrese los gastos totales: "))
        utilidades = calcular_utilidades(P, U, GT)
        print(f"Las utilidades del proyecto son {utilidades:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
