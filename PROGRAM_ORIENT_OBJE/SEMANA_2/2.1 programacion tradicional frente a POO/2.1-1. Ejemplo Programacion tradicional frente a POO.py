# Programación Tradicional
# Gestión de estudiantes: almacenamiento y visualización de datos

# Variables globales para almacenar información
students = []
grades = []

# Función para agregar un estudiante
def add_student(name, grade):
    students.append(name)
    grades.append(grade)

# Función para mostrar la lista de estudiantes y calificaciones
def display_students():
    print("Lista de Estudiantes:")
    for i in range(len(students)):
        print(f"{students[i]} - Nota: {grades[i]}")

# Función para calcular el promedio de calificaciones
def calculate_average():
    total = sum(grades)
    return total / len(grades) if grades else 0

# Uso de funciones
add_student("Ana", 90)
add_student("Luis", 80)
add_student("Carlos", 85)

display_students()
print("Promedio de Notas:", calculate_average())
