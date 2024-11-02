import mysql.connector

def conexion():
    try:
        conexion = mysql.connector.connect(
            user = "root",
            host = "localhost",
            port = "3306",
            password = "aA134679",
            database = "inventario_ipet251",
        )
        print("Conexion exitosa")
        return conexion
    except mysql.connector.Error as e:
        print(f"Error {e}")
        return conexion
    
    
