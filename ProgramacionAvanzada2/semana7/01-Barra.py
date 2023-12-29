import matplotlib.pyplot as plt

data = [2344, 4561, 7631, 8423, 4573, 3453]
indice = ('2017', '2018', '2019', '2020', '2021', '2022')
plt.bar(indice, data)
plt.title('Registro de nacimientos por dia')
plt.xlabel('Años')
plt.ylabel('Nacimientos')
plt.savefig('grafico1.png')
plt.show()
