import matplotlib.pyplot as plt

cantidad = [145, 698, 590, 390, 278]
nombres = ['Analfabeta', 'Primaria', 'Secundaria',
           'Tecnico Superior', 'Universitario']
colores = ['red', 'blue', 'green', 'yellow', 'purple']

plt.pie(cantidad, labels=nombres, colors=colores)
plt.title('Nivel educativo')
plt.savefig('tarea1.png')
plt.show()
