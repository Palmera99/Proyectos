import numpy as np
import matplotlib.pyplot as plt

x = range(100)
y = range(100) + np.random.randint(0, 30, 100)
plt.scatter(x, y)
plt.title('Diagrama de Dispersion')
plt.xlabel('Etiqueta X')
plt.ylabel('Etiqueta Y')
plt.savefig('grafico3.png')
plt.show()
