# Importamos la clase Inventario desde inventario.py
from inventario import Inventario


def mostrar_menu():
    """Muestra las opciones disponibles en el sistema"""
    print("\n=== Sistema de Gestión de Inventarios ===")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    """Función principal para ejecutar el menú interactivo"""
    inventario = Inventario()  # Creamos una instancia de Inventario

    while True:
        mostrar_menu()  # Mostramos el menú
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Pedimos los datos del nuevo producto
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(id_producto, nombre, cantidad, precio)

        elif opcion == "2":
            # Pedimos el ID del producto a eliminar
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Pedimos los datos a actualizar
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (dejar vacío para no modificar): ")
            nuevo_precio = input("Nuevo precio (dejar vacío para no modificar): ")

            # Convertimos las entradas si el usuario proporcionó un valor
            cantidad = int(nueva_cantidad) if nueva_cantidad else None
            precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            # Buscar producto por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            # Mostrar el inventario completo
            inventario.mostrar_inventario()

        elif opcion == "6":
            # Salir del programa
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Verificamos que el script se está ejecutando directamente
if __name__ == "__main__":
    main()
