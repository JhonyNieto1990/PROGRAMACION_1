# Programa: Cálculo del Área de un Rectángulo
# Descripción: Este programa calcula el área de un rectángulo con base y altura dadas por el usuario.
# Incluye diferentes tipos de datos y sigue las buenas prácticas de programación en Python.

# Definimos una función para calcular el área del rectángulo
def calcular_area_rectangulo(base, altura):
    """
    Función que calcula el área de un rectángulo.
    :param base: (float) Base del rectángulo en metros
    :param altura: (float) Altura del rectángulo en metros
    :return: (float) El área del rectángulo en metros cuadrados
    """
    return base * altura  # Multiplicamos base por altura para obtener el área

# Esta parte indica que el programa debe ejecutarse directamente, no importado como módulo
if __name__ == "__main__":
    # Mostramos un mensaje de bienvenida al usuario
    print("Bienvenido al programa para calcular el área de un rectángulo.")

    # Solicitamos al usuario que ingrese la base del rectángulo
    # Usamos float para asegurarnos de que se pueda introducir un número decimal
    base_rectangulo = float(input("Por favor, ingresa la base del rectángulo en metros: "))

    # Solicitamos al usuario que ingrese la altura del rectángulo
    altura_rectangulo = float(input("Por favor, ingresa la altura del rectángulo en metros: "))

    # Llamamos a la función para calcular el área usando los valores ingresados
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

    # Mostramos el resultado al usuario usando una f-string para formatear el texto
    print(f"\nEl área del rectángulo con base {base_rectangulo} m y altura {altura_rectangulo} m es: {area_rectangulo:.2f} metros cuadrados.")

    # Evaluamos si el área es mayor a 50 metros cuadrados (esto usa un booleano)
    es_grande = area_rectangulo > 50  # Comparamos si el área es mayor a 50
    # Mostramos el resultado de la evaluación
    print(f"¿El área del rectángulo es mayor a 50 m²?: {'Sí' if es_grande else 'No'}")
