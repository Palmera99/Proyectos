import numpy as np
import matplotlib.pyplot as plt

x = range(400)
y = range(400)+np.random.randint(0, 20, 400)

plt.scatter(x, y)
plt.title('Diagrama de Dispersion')
plt.xlabel('Etiqueta X')
plt.ylabel('Etiqueta Y')
plt.savefig('tarea3.png')
plt.show()
