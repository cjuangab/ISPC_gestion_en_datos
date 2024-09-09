#Creamos el arreglo de usuarios precargados
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


in_sesion()