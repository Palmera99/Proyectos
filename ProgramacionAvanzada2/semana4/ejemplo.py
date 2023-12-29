import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Función para manejar el botón "Enviar"


def enviar():
    nombre = entry_nombre.get()
    email = entry_email.get()

    # Validar que ambos campos estén completos
    if nombre == '' or email == '':
        messagebox.showerror('Error', 'Por favor, complete todos los campos.')
    else:
        messagebox.showinfo(
            '¡Éxito!', f'¡Hola {nombre}!\nTu correo es {email}.')


# Crear una ventana de tkinter
ventana = tk.Tk()
ventana.title('Formulario')
ventana.geometry('600x500')

# Crear etiquetas y campos de entrada
label_nombre = ttk.Label(ventana, text='Nombre:').pack()

entry_nombre = ttk.Entry(ventana).pack()


label_email = ttk.Label(ventana, text='Email:')
label_email.pack()
entry_email = ttk.Entry(ventana)
entry_email.pack()

# Botón para enviar el formulario
boton_enviar = ttk.Button(ventana, text='Enviar', command=enviar)
boton_enviar.pack()

# Ejecutar la aplicación
ventana.mainloop()
