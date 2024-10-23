
from os import system               #Importamos del modulo os la funcion system("cls") para poder borrar la consola
from time import sleep              #Importamos del modulo time la funcion sleep() que nos permite realizar un retraso en el sistema
from users import *                 #Importamos del modulo users sus clases y sus funciones

def solicitar_datos():
    id_usuario = int(input("Ingrese el ID del Usuario: "))
    username = input("Ingrese el Nombre de Usuario: ")
    password = input("Ingrese la Contraseña: ")
    email = input("Ingrese el Correo Electrónico: ")
    return id_usuario, username, password, email
def retornar():
    sleep(1)
    system("cls")
    menu_principal()


def menu_principal():
    system("cls")
    op_menu=99
    print("-----------------------------------")
    print('          Menú Principal          ')
    print("-----------------------------------")
    print('1. Crear Usuario.')
    print('2. Ingresar.')
    print('3. Modificar Usuario.')
    print('4. Eliminar Usuario.')
    print('5. Buscar Usuario.')
    print('6. Mostrar todos los usuarios.')
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
            system("cls")
            print("Crear un nuevo Usuario")
            id_usuario, username, password, email = solicitar_datos()
            usuario_nuevo = Usuario(id_usuario, username, password, email)
            agregar_usuario(usuario_nuevo)
            print("Usuario agregado exitosamente")
            retornar()
        case 2:
            system("cls")
            print("Ingreso exitoso")
            print("En prueba")
            retornar()
        case 3:
            system("cls")
            print("Modificar un Usuario")
            id_usuario = int(input("Ingrese el ID del Usuario que desea modificar: "))
            actualizar_usuario(id_usuario)
            retornar()
        case 4:
            # Eliminar un usuario
            system("cls")
            print("Eliminar un Usuario")
            id_usuario = int(input("Ingrese el ID del Usuario que desea eliminar: "))
            eliminar_usuario(id_usuario)
            retornar()
        case 5:
            # Buscar un usuario por ID
            system("cls")
            print("Buscar un Usuario")
            id_usuario = int(input("Ingrese el ID del Usuario que desea buscar: "))
            usuario = buscar_usuario(id_usuario)
            if usuario:
                print(f"Usuario encontrado: {usuario}")
            else:
                print("Usuario no encontrado.")
            sleep(1)
        case 6:
            # Mostrar todos los usuarios almacenados en el archivo
            system("cls")
            print("Mostrar todos los usuarios")
            mostrar_usuarios()
            sleep(3)
            retornar()
        case 0:
            exit
        case _:
            system("cls")
            print("Opcion Incorrecta")
            retornar()    


menu_principal()