import numpy as np

# Definir los parámetros de la matriz
ciudades = ['Quito', 'Cuenca', 'Guayaquil']  # Ciudades
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']  # Días de la semana
semanas = 4  # Número de semanas

# Crear una matriz 3D para almacenar las temperaturas (ciudades x días de la semana x semanas)
temperaturas = np.random.randint(15, 35, size=(len(ciudades), len(dias), semanas))

# Mostrar la matriz de temperaturas generadas
print("Matriz de temperaturas (Ciudades x Días x Semanas):")
print(temperaturas)

# Calcular el promedio de temperatura para cada ciudad por cada semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperatura para {ciudad}:")
    for semana in range(semanas):
        promedio_semana = np.mean(temperaturas[i, :, semana])
        print(f"  Semana {semana + 1}: {promedio_semana:.2f}°C")

# Mostrar el promedio de temperatura para cada ciudad y semana en la pantalla




