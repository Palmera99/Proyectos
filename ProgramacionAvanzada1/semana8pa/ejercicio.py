def notasalumnos():
    alumnos = int(input('ingrese la cantidad de estudiantes: '))
    aprobados = 0
    reprobados = 0
    for i in range(alumnos):
        calificaciones = float(input('Ingrese la calificacion: '))
        if calificaciones >= 4:
            aprobados += 1
        else:
            reprobados += 1

    print(f"la cantidad de aprobados es: {aprobados}")
    print(f'la cantidad de reprobados en: {reprobados}')


notasalumnos()
