# Creamos una clase llamada Personaje que será la base para otros personajes
class Personaje:

    # Constructor: permite asignar valores a los atributos cuando se crea un personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre  # Nombre del personaje
        self.fuerza = fuerza  # Nivel de fuerza del personaje
        self.inteligencia = inteligencia  # Nivel de inteligencia
        self.defensa = defensa  # Nivel de defensa
        self.vida = vida  # Puntos de vida (HP)

    # Función para mostrar los atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")  # Muestra el nombre del personaje
        print("·Fuerza:", self.fuerza)  # Muestra la fuerza
        print("·Inteligencia:", self.inteligencia)  # Muestra la inteligencia
        print("·Defensa:", self.defensa)  # Muestra la defensa
        print("·Vida:", self.vida)  # Muestra los puntos de vida

    # Esta función permite subir los atributos del personaje (nivel)
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza  # Suma fuerza
        self.inteligencia = self.inteligencia + inteligencia  # Suma inteligencia
        self.defensa = self.defensa + defensa  # Suma defensa

    # Esta función verifica si el personaje aún está vivo
    def esta_vivo(self):
        return self.vida > 0  # El personaje está vivo si su vida es mayor a 0

    # Esta función hace que el personaje "muera"
    def morir(self):
        self.vida = 0  # Establece la vida en 0
        print(self.nombre, "ha muerto")  # Mensaje cuando el personaje muere

    # Calcula el daño que el personaje hace a un enemigo
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa  # El daño es la fuerza menos la defensa del enemigo

    # El personaje ataca a otro personaje
    def atacar(self, enemigo):
        daño = self.daño(enemigo)  # Calculamos el daño
        enemigo.vida = enemigo.vida - daño  # Restamos el daño a la vida del enemigo
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():  # Verificamos si el enemigo sigue vivo
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()  # Si no está vivo, se ejecuta la función "morir"

# Guerrero hereda todo lo de la clase Personaje
class Guerrero(Personaje):

    # Constructor especial para el Guerrero, incluye el atributo "espada"
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)  # Llama al constructor de Personaje
        self.espada = espada  # Daño extra del arma espada

    # Función para cambiar de arma (espada)
    def cambiar_arma(self):
        # El usuario elige entre dos armas
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8  # Cambia el daño de la espada
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")  # Mensaje si elige una opción no válida

    # Muestra los atributos del Guerrero, incluyendo la espada
    def atributos(self):
        super().atributos()  # Muestra los atributos de la clase padre
        print("·Espada:", self.espada)  # Agrega el daño de la espada

    # El daño del Guerrero se calcula tomando en cuenta la espada
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

# Mago hereda todo lo de la clase Personaje
class Mago(Personaje):

    # Constructor especial para el Mago, incluye el atributo "libro"
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)  # Llama al constructor de Personaje
        self.libro = libro  # Daño extra del libro de hechizos

    # Muestra los atributos del Mago, incluyendo el libro
    def atributos(self):
        super().atributos()  # Muestra los atributos de la clase padre
        print("·Libro:", self.libro)  # Agrega el daño del libro de hechizos

    # El daño del Mago se calcula tomando en cuenta la inteligencia y el libro
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

# Función para realizar un combate entre dos personajes
def combate(jugador_1, jugador_2):
    turno = 0  # Empezamos en el turno 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():  # El combate continúa mientras los dos estén vivos
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)  # El primer jugador ataca al segundo
        if jugador_2.esta_vivo():  # Verifica si el segundo jugador sigue vivo antes de contraatacar
            print(">>> Acción de ", jugador_2.nombre, ":", sep="")
            jugador_2.atacar(jugador_1)  # El segundo jugador ataca al primero
        turno = turno + 1  # Aumentamos el turno
    if jugador_1.esta_vivo():  # Verificamos quién ganó
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

# Creamos dos personajes: un Guerrero y un Mago
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)  # Guerrero con espada
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)  # Mago con libro de hechizos

# Mostramos los atributos de ambos personajes
personaje_1.atributos()
personaje_2.atributos()

# Realizamos un combate entre el Guerrero y el Mago
combate(personaje_1, personaje_2)
