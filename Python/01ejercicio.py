def Eliminar():
    print(tareas)
    eliminar = input('Escribe la key del diccionario: ')
    tareas.pop(eliminar)
    print(f'asi queda el diccionario: {tareas}')


def Modificar():
    print(tareas)
    kmodificar = input('Escribe la key del diccionario: ')
    vmodificar = input('Escribe el valor del diccionario: ')
    tareas[kmodificar] = vmodificar
    print(f'asi queda la modificacion del diccionario {tareas}')


def Listar():
    print(tareas)


numero_tareas = int(input('Ingrese la cantidad de tareas: '))
tareas = {}

for i in range(numero_tareas):
    nombre_tarea = input('Ingrese el nombre de una tarea: ')
    descripcion_tarea = input('Ingrese la descripción de la tarea: ')

    tareas[nombre_tarea] = descripcion_tarea

condicion = True
while condicion == True:
    eleccion = input(
        'Elige una opcion = Eliminar, Modificar, Listar o Salir: ')
    if eleccion == 'eliminar':
        Eliminar()
    elif eleccion == 'modificar':
        Modificar()
    elif eleccion == 'listar':
        Listar()
    elif eleccion == 'salir':
        print('ejercicio terminado')
        condicion = False
    else:
        print('Opcion no valida')
