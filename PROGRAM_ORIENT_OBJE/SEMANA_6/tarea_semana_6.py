# Definimos la clase base llamada Transaccion
class Transaccion:
    def __init__(self, descripcion, monto):
        # Guardamos la descripción de la transacción como un atributo público
        self.descripcion = descripcion
        # Guardamos el monto de la transacción como un atributo privado (solo accesible dentro de la clase)
        self.__monto = monto

    # Este método muestra la información de la transacción
    def mostrar_info(self):
        return f"Descripción: {self.descripcion}, Monto: ${self.__monto:.2f}"

    # Este método permite cambiar el monto de la transacción, pero solo si es un número positivo
    def modificar_monto(self, nuevo_monto):
        if nuevo_monto >= 0:
            self.__monto = nuevo_monto
        else:
            print("El monto no puede ser negativo")  # Mostramos un mensaje si el monto no es válido

# Definimos la clase derivada llamada TransaccionIVA que hereda de Transaccion
class TransaccionIVA(Transaccion):
    def __init__(self, descripcion, monto, iva):
        # Usamos super() para inicializar los atributos heredados de la clase base
        super().__init__(descripcion, monto)
        # Agregamos un nuevo atributo para guardar el porcentaje de IVA
        self.iva = iva

    # Sobreescribimos el método mostrar_info para incluir el cálculo del IVA
    def mostrar_info(self):
        monto_con_iva = self.calcular_total()  # Calculamos el monto total con IVA
        return f"Descripción: {self.descripcion}, Monto: ${monto_con_iva:.2f} (Incluye IVA)"

    # Este método calcula el monto total incluyendo el IVA
    def calcular_total(self):
        return self._Transaccion__monto * (1 + self.iva / 100)

# Creamos una transacción normal
transaccion = Transaccion("Compra de suministros", 500)
# Creamos una transacción con IVA
transaccion_iva = TransaccionIVA("Venta de producto", 1000, 12)

# Mostramos la información de la transacción normal
print(transaccion.mostrar_info())
# Mostramos la información de la transacción con IVA
print(transaccion_iva.mostrar_info())

# Modificamos el monto de la transacción normal
transaccion.modificar_monto(550)
# Mostramos nuevamente la información para ver los cambios
print(transaccion.mostrar_info())

# Mostramos la información de la transacción con IVA para confirmar el cálculo
print(transaccion_iva.mostrar_info())
