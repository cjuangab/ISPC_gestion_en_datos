

def sumar(a,b):
    try:
        c = a + b
        c = float(c)
        c = round(c,2)
        return c
    except Exception as e:
        print("Dato ingresado no valido")
 

def restar(a,b):
    try:
        c = a - b
        c = float(c)
        c = round(c,2)
        return c
    except Exception as e:
        print("Dato ingresado no valido")

def dividir(a,b):

    try: 
        c = a/b
        c = float(c)
        c = round(c,2)
        return c
    except ZeroDivisionError as e:
        print("La division por 0 no esta definida")
    except ValueError as e:
        print("No ingresaste un valor valido")

def multiplicar(a,b):
    try:
        c = a * b
        c = float(c)
        c = round(c,2)
        return c
    except Exception as e:
        print("Dato ingresado no valido")

