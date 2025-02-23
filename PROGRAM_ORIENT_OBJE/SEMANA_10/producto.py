# Definimos la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto"""
        self.__id = id_producto  # ID único del producto
        self.__nombre = nombre  # Nombre del producto
        self.__cantidad = 0  # Inicialización antes de usar set_cantidad()
        self.__precio = 0.0  # Inicialización antes de usar set_precio()

        self.set_cantidad(cantidad)  # Validación de cantidad
        self.set_precio(precio)  # Validación de precio

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
        """Validación para evitar cantidades negativas"""
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.__cantidad = cantidad

    def set_precio(self, precio):
        """Validación para evitar precios negativos"""
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = precio

    def to_dict(self):
        """Convierte el objeto a un diccionario para guardarlo en un archivo"""
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto desde un diccionario"""
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        """Método especial para representar el producto como una cadena de texto"""
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"
