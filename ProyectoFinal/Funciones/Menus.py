from visualizacion import visualizar_elementos
from Agregar import agregado
from os import system               #Importamos del modulo os la funcion system("cls") para poder borrar la consola
from time import sleep              #Importamos del modulo time la funcion sleep() que nos permite realizar un retraso en el sistema
from Modificar import modificacion
from users import *                 #Importamos del modulo users sus clases y sus funciones
from Login import *




def ingreso():
    op_menu=99
    print("-----------------------------------")
    print('            IPET N° 251            ')
    print("-----------------------------------")
    print('1. Ingresar al sistema')
    print('2. Crear Usuario.')
    print('3. Modificar Usuario.')
    print('4. Eliminar Usuario.')
    print('5. Mostrar listado de usuarios.')
    print('0. Salir')
    try:
        op_menu = int(input("Por favor, Ingrese el número de la opción deseada: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        sleep(1)
        system("cls")
    # Volver al inicio del bucle para solicitar la opción de nuevo

    system("cls")  # Limpiamos la pantalla entre opciones

    match op_menu:
        case 1:
            if login():
                menu_principal()
            else:
                system("cls")
                print("Usuario o contraseña incorrecta")
                sleep(1)
                ingreso()
        case 2:
            system("cls")
            print("Crear un nuevo Usuario")
            id_usuario, username, password, email = solicitar_datos()
            usuario_nuevo = Usuario(id_usuario, username, password, email)
            agregar_usuario(usuario_nuevo)
            print("Usuario agregado exitosamente")
            sleep(1)
            system("cls")
            ingreso()
        case 3:
            system("cls")
            print("Modificar un Usuario")
            id_usuario = int(input("Ingrese el DNI del Usuario que desea modificar: "))
            actualizar_usuario(id_usuario)
            sleep(1)
            system("cls")
            ingreso()
        case 4:
            system("cls")
            print("Eliminar un Usuario")
            id_usuario = int(input("Ingrese el ID del Usuario que desea eliminar: "))
            eliminar_usuario(id_usuario)
            sleep(1)
            system("cls")
            ingreso()
        case 5:
            system("cls")
            print("Mostrar todos los usuarios")
            mostrar_usuarios()
            sleep(3)
            ingreso()
            
        case 0:
            exit
        case _:
            print("Opcion Incorrecta")
            sleep(1)
            system("cls")
            ingreso()


def menu_principal():
    op_menu=99
    print("-----------------------------------")
    print('          Menú Principal          ')
    print("-----------------------------------")
    print('1. Visualizar Elementos de Su laboratorio.')
    print('2. Agregar Elementos a su laboratorio.')
    print('3. Modificar Elementos de su laboratorio.')
    print('0. Salir')
    try:
        op_menu = int(input("Por favor, Ingrese el número de la opción deseada: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        sleep(1)
        system("cls")
    # Volver al inicio del bucle para solicitar la opción de nuevo

    system("cls")  # Limpiamos la pantalla entre opciones

    match op_menu:
        case 1:
            visualizar_elementos()
        case 2:
            agregado()
        case 3:
            modificacion()
        case 0:
            exit
        case _:
            print("Opcion Incorrecta")
            sleep(1)
            system("cls")
            menu_principal()



    
    
    

