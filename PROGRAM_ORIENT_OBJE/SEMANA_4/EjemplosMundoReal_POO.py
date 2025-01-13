# Importamos la librería datetime para trabajar con fechas
from datetime import date

# Definimos la clase Libro para representar un libro en la biblioteca
class Libro:
    # Método constructor: inicializa los atributos de la clase
    def __init__(self, titulo, autor):
        self.titulo = titulo  # Título del libro
        self.autor = autor    # Autor del libro
        self.disponible = True  # Indica si el libro está disponible (por defecto, sí)

    # Método para devolver una representación en texto del objeto Libro
    def __str__(self):
        # Devuelve el título, autor y si está disponible
        return f"'{self.titulo}' por {self.autor} ({'Disponible' if self.disponible else 'No Disponible'})"

# Definimos la clase Usuario para representar a los usuarios de la biblioteca
class Usuario:
    # Método constructor: inicializa los atributos de la clase
    def __init__(self, nombre, user_id):
        self.nombre = nombre  # Nombre del usuario
        self.user_id = user_id  # ID único del usuario

    # Método para devolver una representación en texto del objeto Usuario
    def __str__(self):
        # Devuelve el nombre del usuario y su ID
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

# Definimos la clase Reserva para gestionar las reservas de libros
class Reserva:
    # Método constructor: inicializa los atributos de la reserva
    def __init__(self, usuario, libro):
        self.usuario = usuario  # Usuario que realiza la reserva
        self.libro = libro      # Libro que se está reservando
        self.fecha_reserva = date.today()  # Fecha en que se realiza la reserva (hoy)

    # Método para realizar la reserva de un libro
    def realizar_reserva(self):
        # Verificamos si el libro está disponible
        if self.libro.disponible:
            self.libro.disponible = False  # Marcamos el libro como no disponible
            # Mostramos un mensaje confirmando la reserva
            print(f"Reserva realizada: {self.usuario.nombre} reservó '{self.libro.titulo}' el {self.fecha_reserva}.")
        else:
            # Mostramos un mensaje si el libro no está disponible
            print(f"Lo sentimos, '{self.libro.titulo}' no está disponible.")

    # Método para devolver una representación en texto del objeto Reserva
    def __str__(self):
        # Devuelve información sobre la reserva: libro, usuario y fecha
        return f"Reserva de '{self.libro.titulo}' por {self.usuario.nombre} el {self.fecha_reserva}."

# Creamos una instancia de la clase Libro
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")

# Creamos una instancia de la clase Usuario
usuario1 = Usuario("Juan Pérez", 1)

# Mostramos los datos del libro
print(libro1)

# Creamos una instancia de la clase Reserva para el usuario y el libro
reserva1 = Reserva(usuario1, libro1)

# Realizamos la reserva del libro
reserva1.realizar_reserva()

# Mostramos el estado del libro después de la reserva
print(libro1)

