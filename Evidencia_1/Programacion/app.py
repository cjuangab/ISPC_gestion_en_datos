#Creamos el arreglo de usuarios precargados
from os import system
from time import sleep
from captcha import captcha


usuario1 = dict(nombreUsuario="alucas",clave="112aws",nombre="Lucas",apellido="Aguirre",dni="23345235",email="alucas@mail.com",fnac="23-1-1970")
usuario2 = dict(nombreUsuario="vicludueña",clave="12345678",nombre="Victoria",apellido="Ludueña",dni="40392283",email="vicludueña@mail.com",fnac="08-03-2000")
usuario3 = dict(nombreUsuario="lauraoc",clave="qwerty12",nombre="Laura",apellido="Ocampo",dni="30324837",email="lauraocampo@mail.com",fnac="13-02-1989")
usuario4 = dict(nombreUsuario="topabli",clave="1298a@",nombre="Pablo",apellido="Marquez",dni="44867423",email="pablom@mail.com",fnac="04-06-2003")
usuarios = [usuario1,usuario2,usuario3,usuario4]

def bienvenida():
    print("---------------------------------------------------------------")
    print("                                                               ")
    print("---------------------------------------------------------------")
    print("          Instituto Provincial de Educacíon Técnica            ")
    print("                            N° 251                             ")
    print("                    Guarnicíon Aérea Córdoba                   ")
    print("---------------------------------------------------------------")
    print("                                                               ")
    print("---------------------------------------------------------------")

def menu_principal():
    op_menu=99
    print("-----------------------------------")
    print('          Menú Principal          ')
    print("-----------------------------------")
    print('1. Iniciar Sesion')
    print('2. Registrarse.')

    print('0. Salir')
    
    try:
        op_menu=int(input("Por Favor, Ingrese el número de la opción deseada: "))
        match op_menu:
            case 1:
                in_sesion()
            case 2:
                registrar()
            case 3:
                exit
            case 0:
               exit
            case _:
                print("Opcion Incorrecta")
                sleep(1)
                system("cls")
                menu_principal()
    except Exception as e:
        print("Opcion Incorrecta")
        sleep(1)
        system("cls")
        menu_principal()


def login():
    print("---------------------")
    user = input("INGRESE USUARIO: ")
    print("---------------------")
    past = input("INGRESE CONTRASEÑA: ")
    return(user,past)

def in_sesion():
    intentos = 0
    while intentos < 4: 
        user, password = login()
        for usuario in usuarios:
            if usuario["nombreUsuario"] == user and usuario["clave"] == password:
                print(f"Bienvenido {user}")
                return  
        print("Usuario o contraseña incorrectos. Inténtelo de nuevo.")
        intentos += 1

    print("Número máximo de intentos alcanzado. Intente más tarde.")

def registrar():
    print("---------------------")
    print("Registro de Usuario")
    print("---------------------")

    while True:
        nombreUsuario = input("Ingrese nombre de usuario (6 a 12 caracteres): ")
        if any(usuario["nombreUsuario"] == nombreUsuario for usuario in usuarios):
            print("El nombre de usuario ya está en uso. Intente con otro.")
        elif len(nombreUsuario) < 6 or len(nombreUsuario) > 12:
            print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
        else:
            break

    while True:
        dni = input("Ingrese DNI: ")
        if any(usuario["dni"] == dni for usuario in usuarios):
            print("El DNI ya está registrado.")
        else:
            break

    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    email = input("Ingrese correo electrónico: ")
    fnac = input("Ingrese fecha de nacimiento (dd-mm-aaaa): ")

    while True:
        clave = input("Ingrese contraseña (mínimo 8 caracteres, con al menos 2 de los siguientes: 1 mayúscula, 1 minúscula, 1 número, 1 caracter especial): ")

        if validar_clave(clave):
            break
        else:
            print("La contraseña no cumple con los requisitos.")
    while True:
        if captcha():
            break
    nuevo_usuario = dict(nombreUsuario=nombreUsuario, clave=clave, nombre=nombre, apellido=apellido, dni=dni, email=email, fnac=fnac)
    usuarios.append(nuevo_usuario)
    print(f"Usuario {nombreUsuario} registrado con éxito.")

def validar_clave(clave):
    if len(clave)>= 8:
        return True
    else:
        return False


menu_principal()