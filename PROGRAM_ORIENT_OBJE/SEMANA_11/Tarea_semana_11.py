import json  # Importamos la librería json para guardar y cargar datos en un archivo


# Definimos la clase Producto para representar un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible del producto
        self.precio = precio  # Precio del producto

    # Método para actualizar la cantidad del producto
    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    # Método para actualizar el precio del producto
    def actualizar_precio(self, precio):
        self.precio = precio

    # Método para convertir el objeto en un diccionario, útil para guardar en JSON
    def to_dict(self):
        return {"id": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}


# Definimos la clase Inventario para gestionar los productos
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos usando su ID como clave
        self.cargar_desde_archivo()  # Cargamos los productos almacenados en el archivo JSON

    # Método para agregar un nuevo producto al inventario
    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto  # Se guarda el producto en el diccionario
        self.guardar_en_archivo()  # Se actualiza el archivo JSON

    # Método para eliminar un producto del inventario por su ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:  # Verificamos si el producto existe
            del self.productos[id_producto]  # Eliminamos el producto del diccionario
            self.guardar_en_archivo()  # Guardamos los cambios en el archivo
        else:
            print("Producto no encontrado.")  # Mensaje si el producto no existe

    # Método para actualizar un producto existente
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:  # Verificamos si el producto existe
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)  # Actualizamos la cantidad
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)  # Actualizamos el precio
            self.guardar_en_archivo()  # Guardamos los cambios en el archivo
        else:
            print("Producto no encontrado.")  # Mensaje si el producto no existe

    # Método para buscar productos por nombre
    def buscar_producto(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    # Método para mostrar todos los productos en el inventario
    def mostrar_productos(self):
        for p in self.productos.values():
            print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

    # Método para guardar los productos en un archivo JSON
    def guardar_en_archivo(self):
        with open("inventario.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.productos.items()}, f)

    # Método para cargar los productos desde un archivo JSON al iniciar el programa
    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as f:
                datos = json.load(f)  # Cargamos los datos desde el archivo
                self.productos = {k: Producto(v['id'], v['nombre'], v['cantidad'], v['precio']) for k, v in
                                  datos.items()}  # Convertimos los datos en objetos Producto
        except FileNotFoundError:
            self.productos = {}  # Si el archivo no existe, se inicia con un inventario vacío


# Función principal que muestra el menú en consola
if __name__ == "__main__":
    inventario = Inventario()  # Creamos un objeto de la clase Inventario
    while True:
        # Mostramos el menú de opciones
        print(
            "\n1. Añadir producto\n2. Eliminar producto\n3. Actualizar producto\n4. Buscar producto\n5. Mostrar productos\n6. Salir")
        opcion = input("Seleccione una opción: ")  # Solicitamos al usuario que seleccione una opción

        if opcion == "1":  # Opción para añadir un producto
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":  # Opción para eliminar un producto
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":  # Opción para actualizar un producto
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":  # Opción para buscar un producto por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            for p in resultados:
                print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        elif opcion == "5":  # Opción para mostrar todos los productos
            inventario.mostrar_productos()
        elif opcion == "6":  # Opción para salir del programa
            break
        else:
            print("Opción no válida.")  # Mensaje si el usuario ingresa una opción incorrecta
