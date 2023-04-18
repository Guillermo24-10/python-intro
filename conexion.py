import sqlite3

conexion = sqlite3.connect("DB_py.db")
cursor = conexion.cursor()

def obtener_clientes():
    sql = "SELECT * FROM ROLES"
    cursor.execute(sql)
    
    clientes = cursor.fetchall()
    print(clientes)

obtener_clientes()    