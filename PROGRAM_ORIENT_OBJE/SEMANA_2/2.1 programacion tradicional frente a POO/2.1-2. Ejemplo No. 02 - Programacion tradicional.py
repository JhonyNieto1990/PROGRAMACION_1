# Programación Tradicional
# Ejemplo: Gestión de inventario de una tienda

# Variables globales
stock = 0
price_per_item = 10

# Función para agregar stock
def add_stock(amount):
    global stock
    stock += amount

# Función para vender productos
def sell_items(quantity):
    global stock
    if quantity <= stock:
        stock -= quantity
    else:
        print("No hay suficiente stock disponible.")

# Función para calcular ingresos
def calculate_income(quantity_sold):
    global price_per_item
    return quantity_sold * price_per_item

# Uso de las funciones
add_stock(50)  # Agregamos 50 unidades al stock
sell_items(20)  # Vendemos 20 unidades
income = calculate_income(20)  # Calculamos los ingresos

# Imprimimos resultados
print("Stock final (Traditional):", stock)
print("Ingresos generados:", income)
