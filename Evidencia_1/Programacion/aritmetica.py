

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

def sumar_n(*num):
    try:
        a = 0.00
        for i in num:
            a += i
        a = round(a,2)
        return a
    except Exception as e:
        print("Dato ingresado no valido")
        
def promedio_n(*num):
        try:
            a = 0.00
            b = 0
            for i in num:
                a += i
                b += 1
            a = (a/b)
            a = round(a,2)    
        except Exception as e:
            print("Dato ingresado no valido")
        else:
            return a

                   