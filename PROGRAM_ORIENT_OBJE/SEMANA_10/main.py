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
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.añadir_producto(id_producto, nombre, cantidad, precio)
            elif opcion == "2":
                inventario.eliminar_producto(input("ID del producto: "))
            elif opcion == "3":
                inventario.actualizar_producto(input("ID del producto: "), int(input("Cantidad: ")), float(input("Precio: ")))
            elif opcion == "4":
                inventario.buscar_producto(input("Nombre: "))
            elif opcion == "5":
                inventario.mostrar_inventario()
            elif opcion == "6":
                print("Saliendo...")
                break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
