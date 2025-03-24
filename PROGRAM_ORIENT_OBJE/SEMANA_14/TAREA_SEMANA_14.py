# Importamos las librerías necesarias
import tkinter as tk  # Librería para crear la interfaz gráfica
from tkinter import ttk, messagebox  # Para usar el Treeview y mensajes emergentes
from datetime import datetime  # Para validar la fecha y hora

# Creamos la clase principal de la aplicación
class AgendaPersonal:
    def __init__(self, root):
        self.root = root  # Ventana principal
        self.root.title("Agenda Personal")  # Título de la ventana

        # ----------- Área de entrada de datos -----------
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)  # Agrega espacio vertical

        # Etiqueta y campo para ingresar la fecha
        tk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5)
        self.entry_fecha = tk.Entry(frame_entrada)
        self.entry_fecha.grid(row=0, column=1, padx=5)

        # Etiqueta y campo para ingresar la hora
        tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, padx=5)
        self.entry_hora = tk.Entry(frame_entrada)
        self.entry_hora.grid(row=1, column=1, padx=5)

        # Etiqueta y campo para ingresar la descripción del evento
        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5)
        self.entry_desc = tk.Entry(frame_entrada, width=40)
        self.entry_desc.grid(row=2, column=1, padx=5)

        # ----------- Botones de acción -----------
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        # Botón para agregar evento
        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.grid(row=0, column=0, padx=10)

        # Botón para eliminar evento seleccionado
        btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.grid(row=0, column=1, padx=10)

        # Botón para salir de la aplicación
        btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
        btn_salir.grid(row=0, column=2, padx=10)

        # ----------- Lista de eventos usando TreeView -----------
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        # Creamos la tabla con 3 columnas: Fecha, Hora y Descripción
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

    # Función para agregar un evento
    def agregar_evento(self):
        fecha = self.entry_fecha.get()  # Obtener el texto ingresado en el campo de fecha
        hora = self.entry_hora.get()  # Obtener la hora ingresada
        descripcion = self.entry_desc.get()  # Obtener la descripción

        # Validamos que el formato de fecha y hora sea correcto
        try:
            datetime.strptime(fecha, '%Y-%m-%d')  # Validar la fecha
            datetime.strptime(hora, '%H:%M')  # Validar la hora
        except ValueError:
            # Si hay error, mostramos un mensaje
            messagebox.showerror("Error", "Formato de fecha u hora inválido.")
            return

        # Verificamos que haya una descripción
        if descripcion.strip() == "":
            messagebox.showwarning("Atención", "Ingrese una descripción.")
            return

        # Insertamos los datos en el TreeView
        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))

        # Limpiamos los campos de entrada
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    # Función para eliminar el evento seleccionado
    def eliminar_evento(self):
        selected = self.tree.selection()  # Obtener el evento seleccionado
        if selected:
            # Preguntar al usuario si está seguro
            confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
            if confirm:
                for item in selected:
                    self.tree.delete(item)  # Eliminar el evento
        else:
            # Si no hay nada seleccionado, mostrar mensaje
            messagebox.showinfo("Información", "Seleccione un evento para eliminar.")

# Código principal que inicia la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = AgendaPersonal(root)  # Crear una instancia de la clase
    root.mainloop()  # Mostrar la ventana
