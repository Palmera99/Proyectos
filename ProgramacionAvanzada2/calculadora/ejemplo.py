import tkinter as tk
from tkinter import messagebox


def abrir_archivo():
    # Lógica para abrir un archivo
    pass


def guardar_archivo():
    # Lógica para guardar un archivo
    pass


def mostrar_acerca_de():
    messagebox.showinfo("Acerca de", "Esta es mi aplicación tkinter")


root = tk.Tk()
root.title("Mi Aplicación")

# Crear un objeto Menu
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# Menú Archivo
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

# Menú Ver
menu_ver = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ver", menu=menu_ver)
menu_ver.add_command(label="Ver Opción 1")
menu_ver.add_command(label="Ver Opción 2")

# Menú Ayuda (Acerca de)
hector = tk.Label(text='lolol')
hector.pack()
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=mostrar_acerca_de)

root.mainloop()
