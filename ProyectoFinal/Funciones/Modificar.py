import mysql
from Menus import *
from os import system
from time import sleep
from Conector import conexion 

def modificacion():
    system("cls")
    print("-----------------------------------")
    print('     MODIFICACION DE INVENTARIO    ')
    print("-----------------------------------")
    print("                                   ")
    print("        Que desea Modificar        ")
    print("-----------------------------------")
    print("                                   ")
    print('1. Recursos Informaticos')
    print('2. Herramental')
    print('3. Equipamiento')
    print('4. Insumos')
    print('0. Menu Principal')
    print("                                   ")
    op_mo = int(input(": "))
    match op_mo:
        case 1:
            consulta("informaticos")  # Nombre de la tabla en la base de datos
        case 2:
            consulta("herramental")
        case 3:
            consulta("equipamiento")
        case 4:
            consulta("insumos")
        case 0:
            system("cls")
            menu_principal()
        case _:
            print("Opcion Incorrecta")
            modificacion()

def consulta(tabla):
    system("cls")
    id_recurso = int(input("Ingrese el ID del recurso: "))
    
    # Consultar el recurso en la base de datos
    try:
        conec = conexion()
        cursor = conec.cursor()
        cursor.execute(f"SELECT * FROM {tabla} WHERE id = %s;", (id_recurso,))
        recurso = cursor.fetchone()
        
        if recurso:
            print(f"Recurso encontrado: {recurso}")
        else:
            print("Recurso no encontrado.")
            sleep(2)
            modificacion()
            return
        
        print("-------------------------")
        print("Que desea realizar: ")
        print("-------------------------")
        print("1. Modificar")
        print("2. Eliminar")
        print("0. Volver atras")
        i = int(input(": "))
        match i:
            case 1:
                modificar_recurso(tabla, id_recurso)
            case 2:
                confirmar_eliminacion(tabla, id_recurso)
            case 0:
                modificacion()
            case _:
                print("Valor invalido")
                consulta(tabla)
        conec.close()
    except mysql.connector.Error as e:
        print(f"Error {e}")
    
def modificar_recurso(tabla, id_recurso):
    
    print("Modificación de recurso:")
    columna = input("Ingrese el nombre de la columna a modificar: ")
    nuevo_valor = input("Ingrese el nuevo valor: ")
    
    try:
        conec = conexion()
        cursor = conec.cursor()
        sql = f"UPDATE {tabla} SET {columna} = %s WHERE id = %s;"
        cursor.execute(sql, (nuevo_valor, id_recurso))
        conec.commit()
        
        if cursor.rowcount > 0:
            print("Recurso actualizado correctamente.")
        else:
            print("No se realizó ninguna modificación.")
        conec.close()
    except mysql.connector.Error as e:
        print(f"Error {e}")
    sleep(2)
    modificacion()

def confirmar_eliminacion(tabla, id_recurso):
    print("¿ESTA TOTALMENTE SEGURO DE ELIMINAR EL RECURSO?")
    sup = int(input("---1:SI----2:NO---"))
    if sup == 1:
        eliminar_recurso(tabla, id_recurso)
    else:
        modificacion()

def eliminar_recurso(tabla, id_recurso):
    try:
        conec = conexion()
        cursor = conec.cursor()
        sql = f"DELETE FROM {tabla} WHERE id = %s;"
        cursor.execute(sql, (id_recurso,))
        conec.commit()
        
        if cursor.rowcount > 0:
            print("Recurso eliminado del inventario.")
        else:
            print("Recurso no encontrado o no eliminado.")
        conec.close()
    except mysql.connector.Error as e:
        print(f"Error {e}")
    sleep(2)
    modificacion()