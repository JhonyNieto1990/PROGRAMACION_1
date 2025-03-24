import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación GUI Básica")

        # Etiqueta de instrucciones
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=5)

        # Campo de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Botón Agregar
        self.btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.btn_agregar.pack(pady=5)

        # Lista para mostrar los datos ingresados
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=5)

        # Botón Limpiar
        self.btn_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_lista)
        self.btn_limpiar.pack(pady=5)

    def agregar_dato(self):
        """Añade el texto ingresado en el campo de texto a la lista."""
        dato = self.entry.get().strip()
        if dato:
            self.listbox.insert(tk.END, dato)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregarlo.")

    def limpiar_lista(self):
        """Elimina todos los datos ingresados en la lista."""
        self.listbox.delete(0, tk.END)

# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
