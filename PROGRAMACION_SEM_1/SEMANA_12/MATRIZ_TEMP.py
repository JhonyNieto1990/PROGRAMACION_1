# ciudad, día, temperatura

# Matriz que contiene las temperaturas de 4 semanas para las 3 ciudades: Quito, Guayaquil y Cuenca
arreglo_temperaturas = [
    [   # Quito
        [23, 15, 12, 30, 56, 24, 23],  # semana 1 - temperaturas diarias
        [15, 20, 40, 10, 13, 15, 15],  # semana 2 - temperaturas diarias
        [22, 18, 25, 30, 20, 24, 28],  # semana 3 - temperaturas diarias
        [30, 28, 25, 35, 33, 29, 27]   # semana 4 - temperaturas diarias
    ],  # Quito
    [   # Guayaquil
        [17, 22, 19, 20, 25, 23, 24],  # semana 1 - temperaturas diarias
        [25, 28, 24, 22, 20, 26, 30],  # semana 2 - temperaturas diarias
        [29, 31, 32, 30, 33, 35, 37],  # semana 3 - temperaturas diarias
        [21, 19, 23, 25, 22, 18, 20]   # semana 4 - temperaturas diarias
    ],  # Guayaquil
    [   # Cuenca
        [30, 35, 32, 31, 34, 33, 36],  # semana 1 - temperaturas diarias
        [28, 27, 29, 30, 26, 31, 25],  # semana 2 - temperaturas diarias
        [24, 22, 23, 25, 27, 26, 28],  # semana 3 - temperaturas diarias
        [19, 18, 20, 21, 22, 24, 23]   # semana 4 - temperaturas diarias
    ]   # Cuenca
]

# Lista con los nombres de las 3 ciudades
nombres_ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Bucle para recorrer cada ciudad
for ciudad in range(len(arreglo_temperaturas)):  # ciudades

    # Bucle interno para recorrer cada semana de la ciudad actual
    for semana in range(len(arreglo_temperaturas[ciudad])):  # semanas

        # Inicializa el acumulador en 0 para sumar las temperaturas de la semana
        acumulador = 0

        # Bucle que recorre cada temperatura del arreglo de temperaturas por semana
        for temperatura in arreglo_temperaturas[ciudad][semana]:  # temperaturas por semana
            # Suma la temperatura actual al acumulador
            acumulador += temperatura

        # Calcula el promedio de temperaturas de la semana (redondeado al entero más cercano)
        promedio = round(acumulador / len(arreglo_temperaturas[ciudad][semana]))

        # Imprime el nombre de la ciudad, el número de semana y el promedio de temperaturas en grados
        print(f"{nombres_ciudades[ciudad]}, Semana {semana+1}, Promedio: {promedio} grados")


