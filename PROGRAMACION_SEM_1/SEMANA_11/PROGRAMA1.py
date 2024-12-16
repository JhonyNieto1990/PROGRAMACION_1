# MATRIZ BIDEMENSIONAL 3X3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Búsqueda de un valor específico en la matriz
valor_buscar = 8
if any(valor_buscar in fila for fila in matriz):
    print(f"Se encontró {valor_buscar} en la matriz.")
else:
    print(f"{valor_buscar} no se encontró en la matriz.")