from users import *
from os import system               #Importamos del modulo os la funcion system("cls") para poder borrar la consola
from time import sleep              #Importamos del modulo time la funcion sleep() que nos permite realizar un retraso en el sistema
from Bienvenida import bienvenida_prof
from datetime import datetime
import pickle



def solicitar_datos():
    id_usuario = int(input("Ingrese el DNI del Usuario: "))
    username = input("Ingrese el Nombre de Usuario: ")
    password = input("Ingrese la Contraseña: ")
    email = input("Ingrese el Correo Electrónico: ")
    return id_usuario, username, password, email

def registrar_intento_fallido(username):
    with open("logs.txt", "a") as log_file:
        log_file.write(f"Intento fallido de usuario: {username} - Fecha y hora: {datetime.now()}\n")
    print("Intento de inicio de sesión fallido registrado.")    


def registrar_acceso(id_usuario, username):
    fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    acceso = Acceso(id_usuario, fecha_ingreso, "", username)  # Fecha de salida se completará después

    try:
        # Leer el archivo si ya tiene registros
        with open("accesos.ispc", "rb") as archivo:
            accesos = pickle.load(archivo)
    except (FileNotFoundError, EOFError):
        accesos = []  # Si no existe el archivo, crea una lista vacía

    accesos.append(acceso)

    with open("accesos.ispc", "wb") as archivo:  # Guardar el acceso actualizado
        pickle.dump(accesos, archivo)

    print(f"Acceso registrado para usuario: {username}")

def registrar_egreso(username):
    try:
        with open("accesos.ispc", "rb") as archivo:
            accesos = pickle.load(archivo)
    except (FileNotFoundError, EOFError):
        print("No se encontraron accesos para actualizar.")
        return

    # Buscar el último registro de ingreso del usuario sin hora de salida
    for acceso in reversed(accesos):
        if acceso.getUsuarioLogueado() == username and acceso.getFechaSalida() == "":
            acceso.setFechaSalida(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            break
    else:
        print("No se encontró un registro de ingreso abierto para el usuario.")
        return

    # Guardar el cambio en el archivo
    with open("accesos.ispc", "wb") as archivo:
        pickle.dump(accesos, archivo)

    print(f"Egreso registrado para el usuario: {username}")

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
            registrar_acceso(usuario.getId(), username)
            sleep(1)
            system("cls")
            return True,username
    registrar_intento_fallido(username)
    print("Usuario o contraseña incorrectos.")
    return False


def mostrar_intentos_fallidos():
    try:
        with open("logs.txt", "r") as archivo:              #Cambiamos el nombre del archivo para trabajar y lo habilitamos en modo lectura
            print("\nIntentos fallidos de ingreso:")
            print(archivo.read())                           #Leemos el archivo
    except FileNotFoundError:
        print("No hay intentos fallidos registrados.")


def mostrar_accesos():
    try:
        with open("accesos.ispc", "rb") as archivo:          #Cambiamos el nombre del archivo para trabajar y lo habilitamos en modo lectura binaria
            accesos = pickle.load(archivo)
            print("\nHistorial de accesos:")
            for acceso in accesos:
                print(acceso)
    except (FileNotFoundError, EOFError):
        print("No hay accesos registrados.")