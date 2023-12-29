import numpy as np
import matplotlib.pyplot as plt

serie1 = np.random.normal(150, 50, 400)
serie2 = np.random.normal(90, 20, 400)
serie3 = np.random.normal(100, 40, 400)

series = [serie1, serie2, serie3]
plt.boxplot(series)
plt.title('Diagrama de boxplot')
plt.xlabel('Etiqueta X')
plt.ylabel('Etiqueta Y')
plt.savefig('Tarea2.png')
plt.show()
