# Definimos la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto"""
        self.__id = id_producto  # ID único del producto
        self.__nombre = nombre   # Nombre del producto
        self.__cantidad = cantidad  # Cantidad disponible
        self.__precio = precio  # Precio del producto

    # Métodos Getters (para obtener los valores de los atributos privados)
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Métodos Setters (para modificar los valores de los atributos privados)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        """Método especial para representar el producto como una cadena de texto"""
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"
