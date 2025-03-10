import json  # Importamos la librería json para guardar y cargar datos en un archivo


# Clase que representa un libro con título, autor, categoría e ISBN
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Usamos una tupla porque título y autor no cambian
        self.categoria = categoria
        self.isbn = isbn

    def to_dict(self):
        return {"titulo": self.datos[0], "autor": self.datos[1], "categoria": self.categoria, "isbn": self.isbn}


# Clase que representa un usuario con nombre e ID único
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario  # Identificador único
        self.nombre = nombre
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, isbn):
        self.libros_prestados.append(isbn)

    def devolver_libro(self, isbn):
        if isbn in self.libros_prestados:
            self.libros_prestados.remove(isbn)

    def to_dict(self):
        return {"id_usuario": self.id_usuario, "nombre": self.nombre, "libros_prestados": self.libros_prestados}


# Clase que gestiona la biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objetos Libro como valores
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objetos Usuario como valores
        self.cargar_desde_archivo()

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_en_archivo()

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_en_archivo()
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario
        self.guardar_en_archivo()

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.guardar_en_archivo()
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            self.usuarios[id_usuario].prestar_libro(isbn)
            self.guardar_en_archivo()
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            self.usuarios[id_usuario].devolver_libro(isbn)
            self.guardar_en_archivo()

    def buscar_libros(self, criterio):
        return [libro for libro in self.libros.values() if
                criterio.lower() in libro.datos[0].lower() or criterio.lower() in libro.datos[
                    1].lower() or criterio.lower() in libro.categoria.lower()]

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            return self.usuarios[id_usuario].libros_prestados
        return []

    def guardar_en_archivo(self):
        with open("biblioteca.json", "w") as f:
            json.dump({"libros": {isbn: libro.to_dict() for isbn, libro in self.libros.items()},
                       "usuarios": {id_usuario: usuario.to_dict() for id_usuario, usuario in self.usuarios.items()}}, f)

    def cargar_desde_archivo(self):
        try:
            with open("biblioteca.json", "r") as f:
                datos = json.load(f)
                self.libros = {isbn: Libro(v['titulo'], v['autor'], v['categoria'], v['isbn']) for isbn, v in
                               datos.get("libros", {}).items()}
                self.usuarios = {id_usuario: Usuario(v['id_usuario'], v['nombre']) for id_usuario, v in
                                 datos.get("usuarios", {}).items()}
        except FileNotFoundError:
            self.libros = {}
            self.usuarios = {}


if __name__ == "__main__":
    biblioteca = Biblioteca()
    while True:
        print(
            "\n1. Añadir libro\n2. Eliminar libro\n3. Registrar usuario\n4. Eliminar usuario\n5. Prestar libro\n6. Devolver libro\n7. Buscar libros\n8. Listar libros prestados\n9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))
        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)
        elif opcion == "3":
            id_usuario = input("ID de usuario: ")
            nombre = input("Nombre: ")
            biblioteca.registrar_usuario(Usuario(id_usuario, nombre))
        elif opcion == "4":
            id_usuario = input("ID del usuario a eliminar: ")
            biblioteca.eliminar_usuario(id_usuario)
        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)
        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)
        elif opcion == "7":
            criterio = input("Ingrese título, autor o categoría para buscar: ")
            resultados = biblioteca.buscar_libros(criterio)
            for libro in resultados:
                print(
                    f"Título: {libro.datos[0]}, Autor: {libro.datos[1]}, Categoría: {libro.categoria}, ISBN: {libro.isbn}")
        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            print("Libros prestados:", libros_prestados)
        elif opcion == "9":
            break
        else:
            print("Opción no válida.")
