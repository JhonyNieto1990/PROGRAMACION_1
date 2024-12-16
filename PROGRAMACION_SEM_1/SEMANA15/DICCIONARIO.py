# INGRESO DATOS LIBRO
nombre = input("Ingrese el nombre del libro: ")
categoria = input("Ingrese la categoría del libro: ")
año_publicacion = input("Ingrese el año de publicación del libro: ")
numero_hojas = input("Ingrese el número de hojas del libro: ")
autor = input("Ingrese el autor del libro: ")

# DICCIONARIO
libro = {
    "Nombre": nombre,
    "Categoría": categoria,
    "Año de Publicación": año_publicacion,
    "Número de Hojas": numero_hojas,
    "Autor": autor
}

# IMPRESION DE LOS DATOS
print("Datos del libro ingresado:")
print(f"Nombre: {libro['Nombre']}")
print(f"Categoría: {libro['Categoría']}")
print(f"Año de Publicación: {libro['Año de Publicación']}")
print(f"Número de Hojas: {libro['Número de Hojas']}")
print(f"Autor: {libro['Autor']}")