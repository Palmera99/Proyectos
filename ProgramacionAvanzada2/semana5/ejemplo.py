import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user='root', password='lollol', db='instituto')

if conn:
    print('exito en la conexion')
else:
    print('Problemas de conexion')

cursor = conn.cursor()
try:
    sql1 = 'select * from curso where edad = 20'
    cursor.execute(sql1)
    for lista in cursor:
        print(lista)

    print('Ejecutado con exito')

except Exception as e:
    print(e)
