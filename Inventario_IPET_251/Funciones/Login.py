from users import *
from os import system               #Importamos del modulo os la funcion system("cls") para poder borrar la consola
from time import sleep              #Importamos del modulo time la funcion sleep() que nos permite realizar un retraso en el sistema
from Bienvenida import bienvenida_prof

def solicitar_datos():
    id_usuario = int(input("Ingrese el DNI del Usuario: "))
    username = input("Ingrese el Nombre de Usuario: ")
    password = input("Ingrese la Contraseña: ")
    email = input("Ingrese el Correo Electrónico: ")
    return id_usuario, username, password, email

    

def login():
    system("cls")
    print("Ingrese sus credenciales para acceder al sistema.")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    try:
        usuarios_lista = leer_usuarios("usuarios.ispc")
    except FileNotFoundError:
        system("cls")
        print("No se encontraron usuarios registrados.")
        return False
    for usuario in usuarios_lista:
        if usuario.getUsername() == username and usuario.getPassword() == password:
            system("cls")
            bienvenida_prof(username)
            sleep(1)
            system("cls")
            return True,username

    print("Credenciales incorrectas. Acceso denegado.")
    return False