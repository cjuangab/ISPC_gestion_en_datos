import Menus
from os import system
from time import sleep


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
            consulta("Informatico")
        case 2:
            consulta("Herramental")
        case 3:
            consulta("Equipamiento")
        case 4:
            consulta("Insumo")
        case 0:
            system("cls")
            Menus.menu_principal()
        case _:
            print("Opcion Incorrecta")
            modificacion()
            
            
def consulta(tipo):
    system("cls")
    id = int(input("Ingrese el ID del recurso: "))
    print(f"Su {tipo} ID: {id}")
    sleep(1)
    print("-------------------------")
    print("Que desea realizar: ")
    print("-------------------------")
    print("1. Modificar")
    print("2. Eliminar")
    print("0. Volver atras")
    i = int(input(": "))
    match i:
        case 1:
            print("---------------------------")
            print("Funcion aun en construccion")
            print("---------------------------")
            print("Deberia pedir elementos para modificar BDD")
            sleep(2)
            modificacion()
        case 2:
            print("¿ESTA TOTALMENTE SEGURO?")
            sup = int(input("---1:SI----2:NO---"))
            match sup:
                case 1:
                    print("RECURSO ELIMINADO DEL INVENTARIO")
                    sleep(1)
                    modificacion()
                case 2:
                    modificacion()
        case 0:
            modificacion()
        case _:
            print("Valor invalido")
            
#modificacion()



