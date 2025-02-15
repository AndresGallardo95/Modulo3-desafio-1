def calcular_velocidad_escape(g, r):
    return (2 * g * r) ** 0.5

def main():
    try:
        r = float(input("Ingrese el radio en kilómetros (km): ")) * 1000  # Convertimos a metros
        g = float(input("Ingrese la constante g en (m/s^2): "))
        velocidad_escape = calcular_velocidad_escape(g, r)
        print(f"La velocidad de escape es {velocidad_escape:.2f} (m/s)")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
