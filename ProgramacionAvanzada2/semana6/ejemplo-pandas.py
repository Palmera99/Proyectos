import pandas as pd

serie_listas = pd.Series(["hola", "mundo", "adios"], dtype="string")
print(serie_listas)

data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'Edad': [25, 30, 35, 40],
    'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print(df)


# Read the CSV file into a DataFrame
dataframe = pd.read_csv(
    "C:/xampp/htdocs/Proyectos/Programacion Avanzada 2/semana6/Libro1.csv")

# Select the first column
data1 = dataframe.iloc[:, 0]
print(data1)

# Select the first three columns
data2 = dataframe.iloc[:, 0:3]
print(data2)

# Create a DataFrame containing the first, third, and fourth columns
data3 = dataframe.iloc[:,  [0, 1, 2]]
print("concatenacion de dataframes")
# Concatenate data2 and data3 vertically
dataF = pd.concat([data2, data3])

# Print the concatenated DataFrame
print(dataF)
