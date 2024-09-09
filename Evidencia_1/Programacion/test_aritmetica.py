from aritmetica import *

def test_sumar():
    assert sumar(1, 1) == 2
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(3, 2) == 1
    assert restar(10, 5) == 5
    assert restar(-3, -2) == -1

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(0, 100) == 0
    assert multiplicar(-2, 3) == -6

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3
    try:
        dividir(5, 0)
    except ValueError:
        assert True  
    else:
        assert False 


if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_multiplicar()
    test_dividir()
    print("Todas las pruebas pasaron correctamente")
