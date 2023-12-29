from tkinter import *

def mostrar_seleccion():
    seleccion = var.get()
    resultado.config(text=f"Opción seleccionada: {seleccion}")

# Crear una ventana
ventana = Tk()
ventana.title("Botones de Radio")

# Variable para almacenar la selección
var = StringVar()

# Crear botones de radio
opcion1 = Radiobutton(ventana, text="Opción 1", variable=var, value="Opción 1")
opcion2 = Radiobutton(ventana, text="Opción 2", variable=var, value="Opción 2")
opcion3 = Radiobutton(ventana, text="Opción 3", variable=var, value="Opción 3")

# Botón para mostrar la selección
boton_mostrar = Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)

# Etiqueta para mostrar el resultado
resultado = Label(ventana, text="Opción seleccionada: ")

# Colocar los widgets en la ventana
opcion1.pack()
opcion2.pack()
opcion3.pack()
boton_mostrar.pack()
resultado.pack()

ventana.mainloop()
