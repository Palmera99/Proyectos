import pandas as pd

data = {'nombre': ['Hector', 'Maria', 'Benjamin', 'Agustina', 'Elias', 'Rene', 'Karen'],
        'apellido': ['Diaz', 'Mena', 'Contreras', 'Mena', 'Contreras', 'Muñoz', 'Bravo'],
        'rut': [200497287, 167133738, 206473934, 226876543, 178326989, 137648765, 108765098],
        'sexo': ['M', 'F', 'M', 'F', 'M', 'M', 'F'],
        'direccion': ['Calle 123', 'Av. Principal', 'Calle 456', 'Av. Secundaria', 'Calle 789', 'Pasaje 32', 'Londres 38'],
        'edad': [24, 35, 20, 18, 33, 59, 45]}

df = pd.DataFrame(data)

Masculino = df[df['sexo'] == 'M']
print('Genero Masculino:')
print(Masculino)

Femenino = df[df['sexo'] == 'F']
print('Genero Femenino:')
print(Femenino)

Conjunto = pd.concat([Masculino, Femenino], ignore_index=True)
print(Conjunto)
