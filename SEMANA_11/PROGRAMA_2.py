# Crear una matriz bidimensional (3x3) con valores numéricos
matriz = [
    [3, 2, 1],
    [9, 8, 7],
    [6, 5, 4]
]

# Definir una función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila_index):
    fila = matriz[fila_index]
    n = len(fila)
    # Algoritmo de Bubble Sort
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    matriz[fila_index] = fila

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
ordenar_fila(matriz, 1)

# Mostrar la matriz con la fila ordenada
print("\nMatriz después de ordenar la fila 2 (índice 1):")
for fila in matriz:
    print(fila)