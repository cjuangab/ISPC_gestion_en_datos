import Menus
from random import randint          #Importamos del modulo random la funcion randint para poder obtener numeros aleatorios
from os import system               #Importamos del modulo os la funcion system("cls") para poder borrar la consola
def visualizar_elementos():         #Def de func principal del modulo, sub menu principal de visualizacion
    system("cls")
    print("-----------------------------------")
    print('     VISUALIZACION DE RECURSOS     ')
    print("-----------------------------------")
    print("                                   ")
    print("        Que desea visualizar       ")
    print("-----------------------------------")
    print("                                   ")
    print('1. Recursos Informaticos')
    print('2. Herramental')
    print('3. Equipamiento')
    print('4. Insumos')
    print('0. Menu Principal')
    print("                                   ")
    op_vi = int(input(": "))
    match op_vi:
        case 1:
            visualizar_info("Recursos Informaticos")
        case 2:
            visualizar_info("Herramental")
        case 3:
            visualizar_info("Equipamiento")
        case 4:
            visualizar_info("Insumos")
        case 0:
            system("cls")
            Menus.menu_principal()
        case _:
            print("Opcion Incorrecta")
            visualizar_elementos()


def visualizar_info(tipo):          #Def de sub menu dentro de visualizacion
    
    system("cls")
    print("-----------------------------------")
    print("        Como desea visualizar      ")
    print(f"              {tipo}              ")
    print("-----------------------------------")
    print("                                   ")
    print('1. Listado completo')
    print('2. Elemento unico')
    print('3. Volver atras')
    print("                                   ")
    vi = int(input(": "))
    match vi:
        case 1:
            listado_completo(tipo)
            delay()
            
        case 2:
            i = int(input("Ingrese ID de elemento: "))
            print(f"El elemento {i} de tipo {tipo}: ......")
            delay()
        case 3:
            visualizar_elementos()
        case _:
            print("Opcion Incorrecta")
            visualizar_info(tipo)
    visualizar_elementos()

def listado_completo(tipo):                     #Esta funcion va a estar vinculada con consulta de BDD
    print(f"Listado completo {tipo}")
    for i in range(0,randint(1,20)):            #Obtenemos un numero aleatorio para simular una lista
        print(f"Elemento {i}: ..........")      
def delay():                                    #Funcion para reducir espacio, debe esperar al usuario para continuar
    input("Presione ENTER para continuar ")

 
        
#visualizar_elementos()