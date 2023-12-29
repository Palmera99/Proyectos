import archivos

condicion = True
while condicion == True:
    eleccion = input('Escoje una opcion = Escribir, Leer, salir: ')
    if eleccion == 'escribir':
        archivos.Escribirarchivo()
    elif eleccion == 'leer':
        archivos.Leerarchivo()
    elif eleccion == 'salir':
        print('FIN')
        condicion = False
    else:
        print('Opcion no valida')
