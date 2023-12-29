notas = {
    # Curso 1
    'curso 1': {
        'hector': 7,
        'benjamin': 6,
        'agustina': 5,
        'jeshu': 7,
        'elias': 6
    },
    # Curso 2
    'curso 2': {
        'pedro': 7,
        'laura': 5,
        'roberto': 6,
        'sofia': 7,
        'javier': 5
    },
    # Curso 3
    'curso 3': {
        'isabel': 6,
        'daniel': 5,
        'natalia': 7,
        'andres': 6,
        'patricia': 5
    },
    # Curso 4
    'curso 4': {
        'ricardo': 7,
        'julia': 5,
        'eduardo': 6,
        'valentina': 7,
        'diego': 5
    },
    # Curso 5
    'curso 5': {
        'luis': 6,
        'ana': 5,
        'miguel': 7,
        'clara': 6,
        'sergio': 5
    },
    # Curso 6
    'curso 6': {
        'diana': 7,
        'felipe': 5,
        'veronica': 6,
        'rodrigo': 7,
        'carmen': 5
    }
}

for curso, estudiante in notas.items():
    print(f'{curso}:')
    print('Estudiantes y notas:')
    for nombre, nota in estudiante.items():
        print(f'{nombre}:{nota}')
    promedio = sum(estudiante.values()) / len(estudiante)
    print(f'promedio del {curso} es {promedio}')
    print('\n')
