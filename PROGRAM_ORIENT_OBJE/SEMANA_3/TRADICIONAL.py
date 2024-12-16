# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    # Creamos una lista vacía donde vamos a guardar las temperaturas
    temperaturas = []
    # Utilizamos un bucle para pedir las temperaturas de los 7 días de la semana
    for i in range(7):
        # Solicitamos al usuario que ingrese la temperatura del día actual
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        # Guardamos la temperatura ingresada en nuestra lista
        temperaturas.append(temp)
    # Devolvemos la lista completa con las temperaturas
    return temperaturas

# Función para calcular el promedio de las temperaturas semanales
def calcular_promedio(temperaturas):
    # Sumamos todas las temperaturas y las dividimos por la cantidad de días (7)
    return sum(temperaturas) / len(temperaturas)

# Función principal del programa
def main():
    # Mensaje inicial que explica el propósito del programa
    print("Promedio semanal del clima - Programación Tradicional")
    # Llamamos a la función para ingresar las temperaturas
    temperaturas = ingresar_temperaturas()
    # Calculamos el promedio de las temperaturas ingresadas
    promedio = calcular_promedio(temperaturas)
    # Mostramos el promedio semanal con dos decimales
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Este bloque asegura que el programa solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    main()
