# Definimos una clase llamada Clima para manejar la información de las temperaturas
class Clima:
    # Constructor de la clase: se utiliza para inicializar los atributos de la clase
    def __init__(self):
        # Creamos un atributo privado (una lista) para guardar las temperaturas
        self.__temperaturas = []

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        # Utilizamos un bucle para pedir las temperaturas de los 7 días de la semana
        for i in range(7):
            # Solicitamos al usuario que ingrese la temperatura del día actual
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            # Guardamos la temperatura ingresada en nuestra lista privada
            self.__temperaturas.append(temp)

    # Método para calcular el promedio semanal de las temperaturas
    def calcular_promedio(self):
        # Si no hay temperaturas ingresadas, devolvemos 0 para evitar errores
        if len(self.__temperaturas) == 0:
            return 0
        # Sumamos todas las temperaturas y las dividimos por la cantidad de días (7)
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Función principal del programa
def main():
    # Mensaje inicial que explica el propósito del programa
    print("Promedio semanal del clima - Programación Orientada a Objetos")
    # Creamos un objeto de la clase Clima
    clima = Clima()
    # Llamamos al método para ingresar las temperaturas
    clima.ingresar_temperaturas()
    # Llamamos al método para calcular el promedio semanal
    promedio = clima.calcular_promedio()
    # Mostramos el promedio semanal con dos decimales
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Este bloque asegura que el programa solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    main()
