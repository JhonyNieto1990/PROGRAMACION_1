import json
from producto import Producto


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        """Inicializa el inventario cargando los productos desde el archivo"""
        self.productos = []
        self.cargar_desde_archivo()

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        """Añadir un producto asegurando que el ID sea único y guardarlo en archivo"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                print("Error: Ya existe un producto con este ID.")
                return

        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_en_archivo()
        print("Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        """Eliminar un producto según su ID y actualizar el archivo"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualizar cantidad o precio de un producto según su ID y guardar cambios"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Buscar productos por nombre"""
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

    def guardar_en_archivo(self):
        """Guardar el inventario en un archivo de texto (JSON)"""
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as archivo:
                json.dump([p.to_dict() for p in self.productos], archivo, indent=4)
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    def cargar_desde_archivo(self):
        """Cargar el inventario desde un archivo"""
        try:
            with open(self.ARCHIVO_INVENTARIO, "r") as archivo:
                data = json.load(archivo)
                self.productos = [Producto.from_dict(item) for item in data]
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario. Puede estar corrupto.")
        except Exception as e:
            print(f"Error inesperado al cargar el archivo: {e}")
