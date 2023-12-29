from tkinter import *
from tkinter import messagebox
import mysql.connector


def conexionsql():
    conn = mysql.connector.connect(
        host='localhost', user='root', password='lollol', db='jugueteria')
    if conn:
        return conn
    else:
        return print('ERROR DE CONEXION')


class Jugueteria():
    def __init__(self, Id, nombre, fabricante, genero, edad, tipo):
        self.Id = Id
        self.nombre = nombre
        self.fabricante = fabricante
        self.genero = genero
        self.edad = edad
        self.tipo = tipo


def Insercion():
    conexion = conexionsql()
    Id = id_entry.get()
    nombre = nombre_entry.get()
    fabricante = fabricante_entry.get()
    genero = genero_entry.get()
    edad = edad_entry.get()
    tipo = tipo_entry.get()
    Juguete = Jugueteria(Id, nombre, fabricante, genero, edad, tipo)
    cursor = conexion.cursor()
    try:
        sql = "INSERT INTO juguetes (Id, nombre, fabricante, genero, edad, tipo) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (Juguete.Id, Juguete.nombre, Juguete.fabricante,
                             Juguete.genero, Juguete.edad, Juguete.tipo))

        conexion.commit()
        messagebox.showinfo(title='Éxito', message='Insertado Correctamente')
    except Exception as e:
        messagebox.showerror(title='Error', message=f'{e}')
        print(e)


def actualizar():
    conexion = conexionsql()
    Id = id_entry.get()
    nombre = nombre_entry.get()
    fabricante = fabricante_entry.get()
    genero = genero_entry.get()
    edad = edad_entry.get()
    tipo = tipo_entry.get()
    Juguete = Jugueteria(Id, nombre, fabricante, genero, edad, tipo)
    cursor = conexion.cursor()
    try:
        # Sentencia SQL para actualizar un registro en la tabla juguetes
        sql = "UPDATE juguetes SET nombre = %s, fabricante = %s, genero = %s, edad = %s, tipo = %s WHERE Id = %s"
        cursor.execute(sql, (Juguete.nombre, Juguete.fabricante,
                       Juguete.genero, Juguete.edad, Juguete.tipo, Juguete.Id))

        conexion.commit()
        messagebox.showinfo(title='Éxito', message='Actualizado Correctamente')
    except Exception as e:
        messagebox.showerror(title='Error', message=f'{e}')
        print(e)


def eliminar():
    conexion = conexionsql()
    Id = id_entry.get()
    nombre = nombre_entry.get()
    fabricante = fabricante_entry.get()
    genero = genero_entry.get()
    edad = edad_entry.get()
    tipo = tipo_entry.get()
    Juguete = Jugueteria(Id, nombre, fabricante, genero, edad, tipo)
    cursor = conexion.cursor()
    try:
        sql = "delete from juguetes where id = %s"
        cursor.execute(sql, (Juguete.Id,))
        conexion.commit()
        messagebox.showinfo(title='Éxito', message='Eliminado Correctamente')
    except Exception as e:
        messagebox.showerror(title='Error', message=f'{e}')
        print(e)


ventana = Tk()
ventana.geometry('600x425')
ventana.title('Jugueteria')
Titulo = Label(text='Selecciona las siguientes opciones',
               justify='center', bg='blue', fg='white', width=85)
Titulo.place(x=0, y=0)
# variables
nombre_entry = StringVar()
fabricante_entry = StringVar()
genero_entry = StringVar()
edad_entry = StringVar()
tipo_entry = StringVar()
id_entry = StringVar()
# campos para el ingreso
ingresar_label = Label(text='''Ingresa los Datos''', bg='Yellow')
ingresar_label.place(x=19, y=25)
# ID
id_label = Label(text='Ingresa ID')
id_label.place(x=10, y=50)
id_entry = Entry(width=20, textvariable=id_entry)
id_entry.place(x=10, y=75)
# Nombre
nombre_label = Label(text='Nombre del Juguete')
nombre_label.place(x=10, y=100)
nombre_entry = Entry(width=20, textvariable=nombre_entry)
nombre_entry.place(x=10, y=125)
# fabricante
fabricante_label = Label(text="Fabricante Del Juguete")
fabricante_label.place(x=10, y=150)
fabricante_entry = Entry(width=20, textvariable=fabricante_entry)
fabricante_entry.place(x=10, y=175)
# genero
genero_label = Label(text="Género del Juguete")
genero_label.place(x=10, y=200)
genero_entry = Entry(width=20, textvariable=genero_entry)
genero_entry.place(x=10, y=225)
# edad
edad_label = Label(text="Edad (solo numeros)")
edad_label.place(x=10, y=250)
edad_entry = Entry(width=20, textvariable=edad_entry)
edad_entry.place(x=10, y=275)
# tipo
tipo_label = Label(text="Tipo de Juguete")
tipo_label.place(x=10, y=300)
tipo_entry = Entry(width=20, textvariable=tipo_entry)
tipo_entry.place(x=10, y=325)
# boton de ingresar
boton_ingresar = Button(text='Ingresar Datos', command=Insercion, bg='green')
boton_ingresar.place(x=10, y=350)
# boton de actualizar
actualizar_label = Label(
    text='''En esta seccion solo tienes
 que  rellenar el cuadro 
de al lado con la "id"
del juguete a modificar''')
actualizar_label.place(x=180, y=150)
boton_actualizar = Button(text='Actualizar Datos',
                          command=actualizar, bg='yellow')
boton_actualizar.place(x=200, y=350)
# boton de eliminar
eliminar_label = Label(text='''Para la eliminacion de 
los datos solo la id y 
tocar el boton de abajo 
para eliminar''')
eliminar_label.place(x=400, y=150)
boton_eliminar = Button(text='Eliminar Datos', command=eliminar, bg='red')
boton_eliminar.place(x=400, y=350)
boton_cerrar = Button(text='Cerrar', command=ventana.destroy)
boton_cerrar.place(x=450, y=400)
mainloop()
