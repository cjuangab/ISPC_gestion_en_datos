import pickle           #Importamos la libreria pickle que nos permite convertir objetos a binarios 

class Usuario:          #Definicion de la clase Usuario
#Definicion de variables privadas
    __id:int
    __username:str
    __password:str
    __email:str


    def __init__(self,id:int, username:str, password:str, email:str) -> None:   #Constructur
        self.__id = id
        self.__username = username
        self.__password = password
        self.__email = email

#Geters    
    def getId(self):
        return self.__id
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getEmail(self):
        return self.__email
#Seters    
    def setUsername(self, username:str):
        self.__username=username
    def setPassword(self, password:str):
        self.__password=password
    def setEmail(self, email:str):
        self.__email=email

    def __str__(self) -> str:
        return f"DNI: {self.__id} Nombre de Usuario: {self.__username}, Email: {self.__email}"

class Acceso:               #Definicion de clase Acceso
#Definicion de variables privadas
    __id :int
    __fechaIngreso:str
    __fechaSalida:str
    __usuarioLogueado:str

    def __init__(self, id:int, fechaIngreso:str, fechaSalida:str, usuarioLogueado:str) -> None: #Constructor
        self.__id = id
        self.__fechaIngreso = fechaIngreso
        self.__fechaSalida = fechaSalida
        self.__usuarioLogueado = usuarioLogueado

#Geters
    def getId(self):
        return self.__id
    def getFechaIngreso(self):
        return self.__fechaIngreso
    def getFechaSalida(self):
        return self.__fechaSalida
    def getUsuarioLogueado(self):
        return self.__usuarioLogueado
#Seters
    def setFechaIngreso(self,fecha_ingreso:str):
        self.__fechaIngreso = fecha_ingreso
    def setFechaSalida(self, fecha_salida:str):
        self.__fechaSalida = fecha_salida
    def setUsuarioLogeado(self, usuario_logeado:str):
        self.__usuarioLogueado = usuario_logeado

    def __str__(self) -> str:
        return f" ID: {self.__id} - Usuario: {self.__usuarioLogueado} - Fecha de Ingreso: {self.__fechaIngreso} - Fecha de Egreso: {self.__fechaSalida}"

def leer_usuarios(archivo = "usuarios.ispc"):   #Definimos una funcion para leer "usuarios" de un archivo binario, por defecto usuarios.ispc
    with open(archivo,"rb") as archivo:         #Abrimos el documento guardado en archivo y con "rb" definimos que va a ser lectura de un archivo binario
        usuario = pickle.load(archivo)          # Almacenamos en la variable usuario la informacion leida a traves del metodo pickle.load que permite la interpretacion binaria
    return usuario

def agregar_usuario(usuario:Usuario, archivo = "usuarios.ispc"): #Definimos una funcion para agregar "usuarios" de un archivo binario, por defecto usuarios.ispc
    try:
        usuarios_en_lista = leer_usuarios(archivo)              #Utilizamos la funcion predefinina que internamente nos devuelve una lista
    except FileNotFoundError:
        usuarios_en_lista = []
    """
    El try/except es para manejar alguan error que pueda aparecer por no existir el archivo o estar en blanco
    """
    usuarios_en_lista.append(usuario)                           #Agregamos a el usuario a la lista existente en el archivo 

    with open(archivo, 'wb') as archivo:                        
        pickle.dump(usuarios_en_lista, archivo)                 #Sobreescribimos la lista existente con la nueva lista que contiene al usuario nuevo
    
    print(f"El Usuario: {usuario.getUsername()} ha sido agregado exitosamente")

    """
    En esta funcion utilizamos el metodo wb que sobre escribe la informacion que haya en el archivo binario
    utilizamos este metodo porque al trabajar con poca informacion va a ser mas eficiente y mas facil de
    trabajar
    """

def mostrar_usuarios(archivo='usuarios.ispc'):  #Definimos una funcion para Mostrar "usuarios" de un archivo binario, por defecto usuarios.ispc
    try:
        usuarios_lista = leer_usuarios(archivo)
        for usuario in usuarios_lista:
            print(usuario)
    except FileNotFoundError:
        print("No se encontraron usuarios.")
    """
    Con el try/except trabajamos para garantizar que el programa no falle si no llega a existir el archivo
    o llega a estar vacio
    """
    
def actualizar_usuario(username:str, password:str, email:str, archivo="usuarios.ispc"):
    usuarios_lista = leer_usuarios(archivo)
    
    for usuario in usuarios_lista:
        if usuario.getUsername == username:
            usuario.setUsername(username)
            usuario.setPassword(password)
            usuario.setNmail(email)

            # Guardar los cambios en el archivo binario
            with open(archivo, 'wb') as archivo:
                pickle.dump(usuarios_lista, archivo)
            print(f"Usuario con Datos actualizados {usuario.__str__()} .")
            return
    print(f"Usuario con DNI {id} no encontrado.")

def buscar_usuario(id_usuario, archivo='usuarios.ispc'):

    usuarios_lista = leer_usuarios(archivo)
    for usuario in usuarios_lista:
        if usuario.getId() == id_usuario:
            return usuario
    return None

def eliminar_usuario(id, archivo='usuarios.ispc'):     #Definimos una funcion para Eliminar "usuarios" de un archivo binario, por defecto usuarios.ispc
    usuarios_lista = leer_usuarios(archivo)
    
    usuarios_filtrados = [usuario for usuario in usuarios_lista if usuario.get_id() != id]

    # Guardar los cambios en el archivo binario
    with open(archivo, 'wb') as archivo:
        pickle.dump(usuarios_filtrados, archivo)
    
    print(f"Usuario con DNI {id} eliminado.")


def burbuja(usuarios):
    n = len(usuarios)
    for i in range(n):
        for j in range(0, n-i-1):
            if usuarios[j].getUsername() > usuarios[j+1].getUsername():
                usuarios[j], usuarios[j+1] = usuarios[j+1], usuarios[j]
    return usuarios

def ordenar_usuarios(archivo='usuarios.ispc'):
    usuarios = leer_usuarios(archivo)
    if not usuarios:
        print("No hay usuarios para ordenar.")
        return

    
    while True:
        print("Opciones de Ordenamiento:")
        print("1. Bubble Sort o Burbuja")
        print("2. Usar sort() de Python")

        try:
            op = int(input("Seleccione la técnica de ordenamiento: "))
            if ((op == 1) or (op==2)) :
                return op  # Retorna la opción seleccionada si es válida
            else:
                print("Opción inválida")
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número.")
            continue  # Reinicia el bucle para pedir la entrada de nuevo
    match op:
        case 1:
            usuarios = burbuja(usuarios)
    
        case 2:
            usuarios.sort(key=lambda x: x.getUsername())
            
    
    
        
    # Guardar usuarios ordenados
    with open(archivo, 'wb') as archivo:
        pickle.dump(usuarios, archivo)
    print("Usuarios ordenados y guardados correctamente.")

