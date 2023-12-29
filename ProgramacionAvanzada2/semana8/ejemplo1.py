from tkinter import *
from tkinter import ttk


def calculo():  # función que ejecuta el cálculo del monto total a pagar
    precio = float(monto_e.get())  # monto de la compra
    impuesto = precio*0.16
    calcu = precio + impuesto  # valor que contienen el monto total a pagar
    return vari.set(calcu)


ventana = Tk()
vari = StringVar()
ventana.title('Comercio la Esperanza')
ventana.geometry('500x400')
ventana.configure(background='Yellow')
ventana.resizable(False, False)
principal_label = Label(text='Factura de compra', font=('Cambria', 14, 'bold'), bg='Blue', justify='left',
                        fg='White', width=50, height=1)
# Coloca la etiqueta o caja de texto en la posición X, Y, introducida
principal_label.place(x=0, y=0)
# ETIQUETAS DE LOS DATOS REQUERIDOS
nombre_t = Label(text='Nombre y Apellidos', font=('Cambria', 14, 'bold'), justify='left', bg='Yellow',
                 fg='Black')
nombre_t.place(x=0, y=100)
dire_t = Label(text='Dirección', font=('Cambria', 14, 'bold'),
               justify='left', bg='Yellow', fg='Black')
dire_t.place(x=0, y=150)
rut_t = Label(text='RUT', font=('Cambria', 14, 'bold'),
              justify='left', bg='Yellow', fg='Black')
rut_t.place(x=0, y=200)
monto_t = Label(text='Monto Compra', font=('Cambria', 14, 'bold'),
                justify='left', bg='Yellow', fg='Black')
monto_t.place(x=0, y=250)
montot_t = Label(text='Monto a Pagar', font=(
    'Cambria', 14, 'bold'), justify='left', bg='Yellow', fg='Black')
montot_t.place(x=0, y=300)
# CAMPOS DE ENTRADA
nombre_e = StringVar()  # Se crea el objeto definido como una cadena de caracteres
dire_e = StringVar()
rut_e = StringVar()
monto_e = float()
montot_e = StringVar()
# Se crea el campo para introducir el dato nombre
nombre_e = Entry(width=20, textvariable=nombre_e)
nombre_e.place(x=200, y=105)
# Se crea el campo para introducir el dato nombre
dire_e = Entry(width=20, textvariable=dire_e)
dire_e.place(x=200, y=155)
# Se crea el campo para introducir el dato nombre
rut_e = Entry(width=20, textvariable=rut_e)
rut_e.place(x=200, y=205)
monto_e = (Entry(width=20))  # Se crea el campo para introducir el dato nombre
monto_e.place(x=200, y=255)
boton = Button(text='Calcular Pago', font=(
    'Cambria', 14, 'bold'), justify='left', command=calculo)
boton.place(x=100, y=350)
calcu = Label(width=20, textvariable=vari)
calcu.place(x=200, y=300)
mainloop()
