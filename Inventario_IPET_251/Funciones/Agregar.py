from os import system
from time import sleep
import Menus
from Conector import *

def agregado():
    system("cls")
    print("-----------------------------------")
    print('          ALTA DE RECURSOS         ')
    print("-----------------------------------")
    print("                                   ")
    print("         Que desea agregar         ")
    print("-----------------------------------")
    print("                                   ")
    print('1. Recursos Informaticos')
    print('2. Herramental')
    print('3. Equipamiento')
    print('4. Insumos')
    print('0. Menu Principal')
    print("                                   ")
    op_ag = int(input(": "))
    match op_ag:
        case 1:
            ag_info()
            
        case 2:
            ag_herr()

        case 3:
            ag_eq()

        case 4:
            ag_ins()

        case 0:
            system("cls")
            Menus.menu_principal()
        case _:
            print("Opcion Incorrecta")
            agregado()



def ag_info():
    a = input("Tipo: ")
    b = input("Marca: ")
    c = input("Número de serie: ")
    d = input("Modelo: ") 
    e = input("Número de serie secundario: ")
    f = input("Origen: ")
    g = input("Estado: ")
    

    try:
        conec = conexion()
        cursor = conec.cursor()
        sql = """
        INSERT INTO informaticos (tipo, marca, modelo, n_serie, n_serie_sec, origen, estado, Laboratorio_idlaboratorio) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        valores = (a, b, d, c, e, f, g, 1)
        cursor.execute(sql, valores)
        conec.commit()
        print(cursor.rowcount, "Registro ingresado")
        conec.close()
    except mysql.connector.Error as e:
        print(f"Error {e}")
    sleep(1)
    agregado() 

def ag_herr():                              # Función en construcción, vinculación con BDD
    a = input("Tipo de Herramienta: ")
    b = input("Marca: ")
    c = input("Número de serie: ")
    g = "0" 
    
    try:
        conec = conexion()
        cursor = conec.cursor()
        sql = "INSERT INTO herramental (tipo, marca, modelo, num_serie, uso, estado, Laboratorio_idlaboratorio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (a, b, g, c, g, g, 1)
        cursor.execute(sql, valores)
        conec.commit()
        print(cursor.rowcount, "Registro ingresado")
        conec.close()
    except mysql.connector.Error as e:
        # Mostrar mensaje de error
        print(f"Error {e}")


    sleep(5)
    agregado() 

def ag_eq():  # Función en construcción, vinculación con BDD
    a = input("Tipo de elemento: ")
    b = input("Marca: ")
    c = input("Numero de serie: ")
    g = "0"
    
    try:
        conec = conexion()
        cursor = conec.cursor()
        
        sql = "INSERT INTO equipamiento (tipo, uso, marca, num_serie, fecha_calibracion, Laboratorio_idlaboratorio) VALUES (%s, %s, %s, %s, %s, %s);"

        
        # Proporcionar los valores correspondientes a las columnas especificadas
        valores = (a, g, b, c,'2099-12-31', 1)
        
        cursor.execute(sql, valores)
        conec.commit()
        
        print(cursor.rowcount, "Registro ingresado")
        conec.close()
        
    except mysql.connector.Error as e:
        print(f"Error {e}")
    
    sleep(3)
    agregado()


def ag_ins():                              #Funcion en construccion, vinculacion con BDD
    a = input("Tipo de elemento: ")
    b = input("Marca: ")
    c = int(input("Cantidad de insumos: "))
    d = input("Unidad: ")
    
    try:
        conec = conexion()
        cursor = conec.cursor()
        sql = "INSERT INTO insumos (tipo, marca, cantidad, unidad, vencimiento, estado, Laboratorio_idlaboratorio) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        valores = (a, b, c, d, '2099-12-31', "servicio", 1)
        cursor.execute(sql,valores)
        conec.commit()
        print(cursor.rowcount,"Registro ingresado")
    except mysql.connector.Error as e:
        print(f"Error {e}")
    sleep(3)
    agregado() 
    
#agregado()

        