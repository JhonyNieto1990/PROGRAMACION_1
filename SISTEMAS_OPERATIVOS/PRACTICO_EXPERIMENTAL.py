import random
import time

# Archivo donde se guardará la salida
archivo_salida = open("salida_memoria.txt", "w")

# Simulación de memoria con bloques fijos
class Memoria:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.memoria = [None] * tamanio

    def asignar(self, proceso, tamanio_requerido):
        for i in range(self.tamanio - tamanio_requerido + 1):
            if all(self.memoria[i + j] is None for j in range(tamanio_requerido)):
                for j in range(tamanio_requerido):
                    self.memoria[i + j] = proceso
                mensaje = f"Proceso {proceso} asignó {tamanio_requerido} bloques de memoria."
                print(mensaje)
                archivo_salida.write(mensaje + "\n")
                return True
        mensaje = f"Proceso {proceso} no pudo asignar memoria. No hay suficiente espacio contiguo."
        print(mensaje)
        archivo_salida.write(mensaje + "\n")
        return False

    def liberar(self, proceso):
        for i in range(self.tamanio):
            if self.memoria[i] == proceso:
                self.memoria[i] = None
        mensaje = f"Proceso {proceso} ha liberado su memoria."
        print(mensaje)
        archivo_salida.write(mensaje + "\n")

    def mostrar_memoria(self):
        mensaje = "Estado actual de la memoria:\n" + str(self.memoria)
        print(mensaje)
        archivo_salida.write(mensaje + "\n")

def proceso(nombre, memoria):
    tamanio_requerido = random.randint(1, 5)
    mensaje = f"{nombre} está pidiendo {tamanio_requerido} bloques de memoria."
    print(mensaje)
    archivo_salida.write(mensaje + "\n")

    if memoria.asignar(nombre, tamanio_requerido):
        time.sleep(1)  # Simular tarea del proceso
        memoria.liberar(nombre)
        time.sleep(1)

def gestionar_memoria():
    memoria = Memoria(10)
    procesos = ['Proceso-A', 'Proceso-B', 'Proceso-C', 'Proceso-D', 'Proceso-E']

    for _ in range(5):
        proceso_nombre = random.choice(procesos)
        proceso(proceso_nombre, memoria)

    memoria.mostrar_memoria()

if __name__ == "__main__":
    gestionar_memoria()
    archivo_salida.close()
