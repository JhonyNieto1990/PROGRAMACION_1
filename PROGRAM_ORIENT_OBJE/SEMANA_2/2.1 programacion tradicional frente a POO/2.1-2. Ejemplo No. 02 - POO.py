# Programación Orientada a Objetos
# Ejemplo: Gestión de inventario de una tienda

class Inventory:
    def __init__(self, price_per_item=10):
        self.stock = 0
        self.price_per_item = price_per_item

    def add_stock(self, amount):
        self.stock += amount

    def sell_items(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print("No hay suficiente stock disponible.")

    def calculate_income(self, quantity_sold):
        return quantity_sold * self.price_per_item

# Crear una instancia de la clase Inventory
store_inventory = Inventory()

# Uso de los métodos
store_inventory.add_stock(50)  # Agregamos 50 unidades al stock
store_inventory.sell_items(20)  # Vendemos 20 unidades
income = store_inventory.calculate_income(20)  # Calculamos los ingresos

# Imprimimos resultados
print("Stock final (OOP):", store_inventory.stock)
print("Ingresos generados:", income)
