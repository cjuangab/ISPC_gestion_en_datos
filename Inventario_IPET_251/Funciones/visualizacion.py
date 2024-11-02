import mysql
from Menus import *
from random import randint          #Importamos del modulo random la funcion randint para poder obtener numeros aleatorios
from os import system               #Importamos del modulo os la funcion system("cls") para poder borrar la consola
from Conector import conexion       # Importamos la función de conexión a la BDD

def visualizar_elementos(profesor):         #Def de func principal del modulo, sub menu principal de visualizacion
    system("cls")
    print("-----------------------------------")
    print('     VISUALIZACION DE RECURSOS     ')
    print("-----------------------------------")
    print("                                   ")
    print("        Que desea visualizar       ")
    print("-----------------------------------")
    print("                                   ")
    print('1. Recursos Informaticos')
    print('2. Herramental')
    print('3. Equipamiento')
    print('4. Insumos')
    print('0. Menu Principal')
    print("                                   ")
    op_vi = int(input(": "))
    match op_vi:
        case 1:
            visualizar_info("Recursos Informaticos")
        case 2:
            visualizar_info("Herramental")
        case 3:
            visualizar_info("Equipamiento")
        case 4:
            visualizar_info("Insumos")
        case 0:
            system("cls")
            menu_principal(profesor)
        case _:
            print("Opcion Incorrecta")
            visualizar_elementos()


def visualizar_info(tabla):  # Submenú para visualizar elementos por tabla
    system("cls")
    print("-----------------------------------")
    print("        Como desea visualizar      ")
    print(f"              {tabla.capitalize()}              ")
    print("-----------------------------------")
    print("                                   ")
    print('1. Listado completo')
    print('2. Elemento unico')
    print('3. Volver atras')
    print("                                   ")
    vi = int(input(": "))
    match vi:
        case 1:
            listado_completo(tabla)
            delay()
        case 2:
            i = int(input("Ingrese ID de elemento: "))
            elemento_unico(tabla, i)  # Nueva función para mostrar un único elemento
            delay()
        case 3:
            visualizar_elementos()
        case _:
            print("Opcion Incorrecta")
            visualizar_info(tabla)
    visualizar_elementos()

def listado_completo(tabla):  # Consulta a la base de datos para obtener todos los registros
    print(f"Listado completo de {tabla.capitalize()}")
    try:
        conec = conexion()
        cursor = conec.cursor()
        cursor.execute(f"SELECT * FROM {tabla};")  # Consultamos todos los elementos de la tabla
        registros = cursor.fetchall()
        
        # Mostramos los registros obtenidos
        for registro in registros:
            print(registro)  # Aquí puedes formatear los registros según necesites
        conec.close()
    except mysql.connector.Error as e:
        print(f"Error {e}")

def elemento_unico(tabla, id_elemento):  # Consulta a la base de datos para obtener un único registro
    print(f"Detalle del elemento ID {id_elemento} en {tabla.capitalize()}")
    try:
        conec = conexion()
        cursor = conec.cursor()
        cursor.execute(f"SELECT * FROM {tabla} WHERE id = %s;", (id_elemento,))  # id puede ser específico para cada tabla
        registro = cursor.fetchone()
        
        if registro:
            print(registro)  # Aquí puedes formatear los detalles del elemento
        else:
            print("Elemento no encontrado")
        conec.close()
    except mysql.connector.Error as e:
        print(f"Error {e}")

def delay():  # Espera para continuar
    input("Presione ENTER para continuar ")
 
        
#visualizar_elementos()