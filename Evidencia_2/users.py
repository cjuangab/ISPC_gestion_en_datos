class Usuario:
    __id:int
    __username:str
    __password:str
    __email:str

    def __init__(self,id:int, username:str, password:str, email:str) -> None:
        self.__id = id
        self.__username = username
        self.__password = password
        self.__email = email
     
    def getId(self):
        return self.__id
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getEmail(self):
        return self.__email
    



class Acceso:
    __id :int
    __fechaIngreso:str
    __fechaSalida:str
    __usuarioLogueado:str

    def __init__(self, id:int, fechaIngreso:str, fechaSalida:str, usuarioLogueado:str) -> None:
        self.__id = id
        self.__fechaIngreso = fechaIngreso
        self.__fechaSalida = fechaSalida
        self.__usuarioLogueado = usuarioLogueado

    def getId(self):
        return self.__id
    def getFechaIngreso(self):
        return self.__fechaIngreso
    def getFechaSalida(self):
        return self.__fechaSalida
    def getUsuarioLogueado(self):
        return self.__usuarioLogueado
    

usuario1= Usuario(1323,"cjuangab","qwerty","tumama@tumama")

print(usuario1.getUsername())
print(usuario1.getEmail())