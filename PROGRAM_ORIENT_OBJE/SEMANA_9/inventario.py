# Importamos la clase Producto desde producto.py
from producto import Producto

# Definimos la clase Inventario
class Inventario:
    def __init__(self):
        """Inicializa un inventario vacío"""
        self.productos = []  # Lista para almacenar los productos

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        """Añadir un producto asegurando que el ID sea único"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                print("Error: Ya existe un producto con este ID.")
                return
        # Creamos un nuevo producto y lo añadimos al inventario
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        """Eliminar un producto según su ID"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualizar la cantidad o el precio de un producto según su ID"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Buscar productos por nombre (puede haber múltiples coincidencias)"""
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("Productos encontrados:")
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Mostrar todos los productos en el inventario"""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for producto in self.productos:
                print(producto)
