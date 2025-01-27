class Producto:
    # Constructor (__init__)
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        print(f"Producto '{self.nombre}' creado con precio ${self.precio}")

    # Destructor (__del__)
    def __del__(self):
        print(f"Producto '{self.nombre}' eliminado de la memoria")

# Crear objetos de la clase Producto
producto1 = Producto("Laptop", 750)
producto2 = Producto("Smartphone", 500)

# Eliminar manualmente un objeto (para activar el destructor)
del producto1

# Mostrar que aún se puede trabajar con el otro objeto
print(f"El producto restante es: {producto2.nombre}")
