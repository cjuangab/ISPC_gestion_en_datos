
from os import system               #Importamos del modulo os la funcion system("cls") para poder borrar la consola
from time import sleep              #Importamos del modulo time la funcion sleep() que nos permite realizar un retraso en el sistema

def menu_principal():
    op_menu=99
    print("-----------------------------------")
    print('          Menú Principal          ')
    print("-----------------------------------")
    print('1. Crear Usuario.')
    print('2. Modificar Usuario.')
    print('3. Eliminar Usuario.')
    print('4. Buscar Usuario.')
    print('0. Salir')
    op_menu=int(input("Por Favor, Ingrese el número de la opción deseada: "))
    match op_menu:
        case 1:
            print('3. Eliminar Usuario.')
        case 2:
            print('3. Eliminar Usuario.')
        case 3:
            print('3. Eliminar Usuario.')
        case 0:
            exit
        case _:
            print("Opcion Incorrecta")
            sleep(1)
            system("cls")
            menu_principal()

menu_principal()