import numpy as np
import matplotlib.pyplot as plt

c1 = np.random.normal(200, 10, 500)
c2 = np.random.normal(100, 5, 500)
c3 = np.random.normal(400, 12, 500)
c4 = np.random.normal(500, 3, 500)
datos = [c1, c2, c3, c4]
plt.boxplot(datos)
plt.title('Diagrama de boxplot')
plt.xlabel('etiqueta x')
plt.ylabel('etiqueta y')
plt.savefig('grafico2.png')
plt.show()
