from random import randint
from time import sleep
from aritmetica import *
from os import system  

def captcha():
    a = randint(1,10)
    b = randint(0,5)
    c = randint(1,10)
    d = randint(1,10)
    e = randint(0,5)
    result = sumar_n(a,c,d) - multiplicar(b,e)
    print("Resolver el siguiente calculo para verificar:")
    print(f"({a} + {c} + {d} ) - ( {b} x {e})")
    try:
        opcion = float(input("Ingrese el valor: "))
        if result == opcion:
            return True
        else:
            return False
    except Exception as e:
        print("Valor ingresado no valido")
        sleep(1.5)
        system("cls")
        captcha()
        
        
