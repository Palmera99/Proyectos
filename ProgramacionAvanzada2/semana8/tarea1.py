from tkinter import *
import pandas as pd

# Función para calcular el promedio


def Calcular():
    suma = 0.0
    Notas = [float(nota1_entry.get()), float(
        nota2_entry.get()), float(nota3_entry.get())]
    for nota in Notas:
        suma += nota
    promedio = round(suma / 3)
    promedios.set(promedio)


def Exportar():
    c1 = nombre_entry.get()
    c2 = apellido_entry.get()
    c3 = rut_entry.get()
    c4 = sexo_radio.get()
    c5 = nota1_entry.get()
    c6 = nota2_entry.get()
    c7 = nota3_entry.get()
    c8 = promedios.get()
    registro = [{'Nombre': c1, 'Apellido': c2, 'Rut': c3, 'Sexo': c4,
                'Nota P1': c5, 'Nota P2': c6, 'Nota P3': c7, 'Promedio': c8}]
    registro = pd.DataFrame(registro)
    # El registro se guarda con el apellido del alumno
    registro.to_csv(f'registro_alumno_{c2}.csv')


# Crear la ventana
ventana = Tk()
ventana.title('Formulario Colegio')
ventana.configure(background='Gray')
ventana.geometry('500x600')
ventana.resizable(False, False)

# Labels
Titulo = Label(text='Formulario de Estudiantes', justify='center',
               bg='Blue', fg='White', width=70, height=1)
Titulo.place(x=0, y=0)
nombre_label = Label(text='Nombre', font=(
    'Cambria', 14, 'bold'), justify='left', bg='Yellow', fg='Black')
nombre_label.place(x=0, y=100)
apellido_label = Label(text='Apellido', font=(
    'Cambria', 14, 'bold'), justify='left', bg='Yellow', fg='Black')
apellido_label.place(x=0, y=150)
rut_label = Label(text='Rut', font=('Cambria', 14, 'bold'),
                  justify='left', bg='Yellow', fg='Black')
rut_label.place(x=0, y=200)
sexo_label = Label(text='Sexo', font=('Cambria', 14, 'bold'),
                   justify='left', bg='Yellow', fg='Black')
sexo_label.place(x=0, y=250)
nota1_label = Label(text='Nota p1', font=(
    'Cambria', 14, 'bold'), justify='left', bg='Yellow', fg='Black')
nota1_label.place(x=0, y=300)
nota2_label = Label(text='Nota p2', font=(
    'Cambria', 14, 'bold'), justify='left', bg='Yellow', fg='Black')
nota2_label.place(x=0, y=350)
nota3_label = Label(text='Nota p3', font=(
    'Cambria', 14, 'bold'), justify='left', bg='Yellow', fg='Black')
nota3_label.place(x=0, y=400)
notaf = Label(text='Promedio', font=('Cambria', 14, 'bold'),
              justify='left', bg='Yellow', fg='Black')
notaf.place(x=0, y=450)

# Campos de entrada
nombre_entry = StringVar()
apellido_entry = StringVar()
rut_entry = StringVar()
sexo_radio = StringVar()
nota1_entry = DoubleVar()
nota2_entry = DoubleVar()
nota3_entry = DoubleVar()
promedios = StringVar()

# Campos rellenables
nombre_entry = Entry(width=20, textvariable=nombre_entry)
nombre_entry.place(x=200, y=105)

apellido_entry = Entry(width=20, textvariable=apellido_entry)
apellido_entry.place(x=200, y=155)

rut_entry = Entry(width=20, textvariable=rut_entry)
rut_entry.place(x=200, y=205)

sexo_radio.set('Masculino')
masculino = Radiobutton(ventana, text='Masculino',
                        variable=sexo_radio, value='Masculino')
masculino.place(x=200, y=255)
femenino = Radiobutton(ventana, text='Femenino',
                       variable=sexo_radio, value='Femenino')
femenino.place(x=300, y=255)

nota1_entry = Entry(width=20, textvariable=nota1_entry)
nota1_entry.place(x=200, y=305)

nota2_entry = Entry(width=20, textvariable=nota2_entry)
nota2_entry.place(x=200, y=355)

nota3_entry = Entry(width=20, textvariable=nota3_entry)
nota3_entry.place(x=200, y=405)

notafinal = Label(width=20, textvariable=promedios)
notafinal.place(x=200, y=455)

boton_promedio = Button(text='Calcular Promedio', font=(
    'Cambria', 14, 'bold'), justify='left', command=Calcular, bg='green yellow')
boton_promedio.place(x=25, y=500)

boton_exportar = Button(text='Exportar a CSV', font=(
    'Cambria', 14, 'bold'), justify='left', command=Exportar, bg='Cyan')
boton_exportar.place(x=250, y=500)

mainloop()
