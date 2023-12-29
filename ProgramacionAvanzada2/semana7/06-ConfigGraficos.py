import matplotlib.pyplot as plt
# Se define la entrada de datos, color, marcador y tipo de linea
plt.plot([1, 2, 3, 4], [1, 2, 0, 0.5], color='brown',
         marker='*', linestyle='dashed')
plt.title('Diagrama de líneas')  # Colocación del título del gráfico
plt.xlabel('Unidad de tiempo')  # Etiqueta del eje X
plt.ylabel('Valor de la variable')  # Etiqueta del eje Y
plt.legend(loc='upper right')  # Leyenda del gráfico
# Se define la rejilla sobre el eje y
plt.grid(axis='y', color='black', linestyle='dashed')
plt.show()
