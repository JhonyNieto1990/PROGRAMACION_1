# Nombre: Jhony Nieto
# Fecha: 08/06/2025


import math

# Clase que representa un Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio  # Atributo tipo float (dato primitivo)

    def calcular_area(self):
        """Calcula el área del círculo"""
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        """Calcula el perímetro (circunferencia) del círculo"""
        return 2 * math.pi * self.radio


# Clase que representa un Cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado  # Atributo tipo float (dato primitivo)

    def calcular_area(self):
        """Calcula el área del cuadrado"""
        return self.lado ** 2

    def calcular_perimetro(self):
        """Calcula el perímetro del cuadrado"""
        return 4 * self.lado


# Bloque principal del programa
if __name__ == "__main__":
    # Crear un círculo con radio 5
    circulo = Circulo(5)
    # Crear un cuadrado con lado 4
    cuadrado = Cuadrado(4)

    # Mostrar resultados en pantalla
    print("Área del círculo:", circulo.calcular_area())
    print("Perímetro del círculo:", circulo.calcular_perimetro())
    print("Área del cuadrado:", cuadrado.calcular_area())
    print("Perímetro del cuadrado:", cuadrado.calcular_perimetro())
