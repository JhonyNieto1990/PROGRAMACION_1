# Datos de temperaturas actualizados
temperaturas = [
    # Ciudad Quito
    [
        [10, 12, 14],  # Semana 1 - Temperaturas en Quito
        [15, 14, 16],  # Semana 2 - Temperaturas en Quito
        [11, 10, 12],  # Semana 3 - Temperaturas en Quito
        [16, 18, 19]   # Semana 4 - Temperaturas en Quito
    ],
    # Ciudad Ambato
    [
        [8, 7, 9],     # Semana 1 - Temperaturas en Ambato
        [6, 5, 7],     # Semana 2 - Temperaturas en Ambato
        [12, 13, 15],  # Semana 3 - Temperaturas en Ambato
        [9, 10, 8]     # Semana 4 - Temperaturas en Ambato
    ]
]

# Función para calcular el promedio de temperatura
# Esta función recibe los datos de las temperaturas, la ciudad y la semana y calcula el promedio
def promedio_temperatura(datos_temperaturas, ciudad, semana):
    acumulador = 0  # Inicializamos el acumulador en 0 para sumar las temperaturas
    # repetimos la lista de temperaturas de la semana y ciudad seleccionada
    for temp in range(len(datos_temperaturas[ciudad][semana])):
        # Sumar cada temperatura al acumulador
        acumulador += datos_temperaturas[ciudad][semana][temp]
    # Calcular el promedio dividiendo el acumulador entre la cantidad de días (3 en este caso)
    promedio = acumulador / len(datos_temperaturas[ciudad][semana])
    return promedio  # Retorna el promedio calculado

# base para mapear el input de ciudad con su índice
# Quito está en la posición 0 y Ambato en la posición 1 en la lista de temperaturas
ciudades = {
    "Quito": 0,
    "Ambato": 1
}

# Solicitar al usuario la ciudad y la semana
# Pedimos al usuario que ingrese el nombre de la ciudad y lo guardamos en ciudad_input
ciudad_input = input("Ingrese la ciudad (Quito o Ambato): ")

# Pedimos al usuario que ingrese la semana y restamos 1 porque el índice de la lista comienza en 0
semana_input = int(input("Ingrese el número de la semana (1-4): ")) - 1

# Verificar que la ciudad ingresada sea válida
# Si la ciudad ingresada está en la bse, procedemos
if ciudad_input in ciudades:
    # Obtenemos el indice de la ciudad a partir de ls base
    ciudad_index = ciudades[ciudad_input]
    # Llamamos a la función para obtener el promedio de temperatura
    promedio = promedio_temperatura(temperaturas, ciudad_index, semana_input)
    # Mostramos el promedio de temperatura
    print(f"El promedio de temperatura en {ciudad_input} para la semana {semana_input + 1} es: {promedio}""°")
else:
    # Si la ciudad ingresada no es válida, mostramos un mensaje de error y se debe correr nuevamente
    print("La ciudad ingresada no es válida.")


