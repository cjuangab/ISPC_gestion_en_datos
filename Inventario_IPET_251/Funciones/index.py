from Bienvenida import *
from Menus import *
from Login import *
from visualizacion import *
from os import system                   #Importamos el modulo os la funcion system("cls") para poder borrar la consola
from time import sleep


system("cls")                           #Borrado automatico de consola
bienvenida()                            #Funcion de bienvenida a sistema

"""
prof, contra = login()                  #Llamamos a la funcion login() y recuperamos el usuario y contraseña
sleep(1.5)                              #Establecemos un delay para que se pueda leer el mensaje

system("cls")                           
bienvenida_prof(prof)                   #Llamamos a la funcion importada saludo_prof para dar una bienvenida
"""
ingreso()
#menu_principal()                        #Ejecutamos el menu principal
system("cls")
#cierre(prof)                            #Llamamos a la funcion saludo_prof pero para dar una despedida