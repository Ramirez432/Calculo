import numpy as np
import matplotlib.pyplot as plt


def main():
    print("Calculadora de Valor Futuro de Inversiones")
    inversion = float(input("Ingrese la inversión inicial: "))
    tasa = float(input("Ingrese la tasa de interés anual (en porcentaje): ")) / 100.0
    tiempo = int(input("Ingrese el número de años: "))

    ganancia = calcular_ganancia(inversion, tasa, tiempo)

    print(f"La ganancia final es de: ${ganancia:.2f}")

    # Calcular las ganancias año por año
    ganancias_anuales = []
    for año in range(1, tiempo + 1):
        ganancia_anual = calcular_ganancia(inversion, tasa, año)  # Ganancia acumulada hasta el año actual
        ganancias_anuales.append(ganancia_anual)

    # Graficar las ganancias año por año
    plt.plot(range(1, tiempo + 1), ganancias_anuales)
    plt.xlabel("Años")
    plt.ylabel("Ganancia acumulada")
    plt.title("Ganancias Año por Año")
    plt.grid(True)
    plt.show()


def calcular_ganancia(inversion, tasa, tiempo):
    uno = 1 + (tasa / 12)
    dos = 12 * tiempo
    valor_final = inversion * (uno ** dos)
    valor_final -= inversion
    return valor_final


if __name__ == "__main__":
    main()
