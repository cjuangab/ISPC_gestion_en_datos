import os
import csv
import random


def cargar_registros_pluviales():
    año = int(input("Ingrese el año que desea consultar: "))
    nombre_archivo = f"registros_pluviales_{año}.csv"

    # Verificar si el archivo existe
    if os.path.exists(nombre_archivo):
        print(f"Archivo encontrado: {nombre_archivo}")
        registros = cargar_desde_csv(nombre_archivo)
    else:
        print(f"No se encontró el archivo para el año {año}. Generando datos aleatorios...")
        registros = generar_registros_aleatorios()
        guardar_en_csv(nombre_archivo, registros)

    # Solicitar al usuario que elija un mes para mostrar los registros
    print("Seleccione el mes para ver los registros:")
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    for i, mes in enumerate(meses, start=1):
        print(f"{i}. {mes}")

    try:
        mes_elegido = int(input("Ingrese el número del mes (1-12): "))
        if 1 <= mes_elegido <= 12:
            mostrar_registros_mes(registros, mes_elegido)
        else:
            print("Opción inválida. Debe seleccionar un número entre 1 y 12.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")

def cargar_desde_csv(nombre_archivo):
    #Cargar registros desde un archivo CSV.
    registros = []
    with open(nombre_archivo, mode='r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            registros.append([int(dia) for dia in fila])
    return registros

def generar_registros_aleatorios():
    """Generar datos aleatorios para los 365 días del año."""
    registros = []
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for dias in dias_por_mes:
        mes = [random.randint(0, 100) for _ in range(dias)]  # Genera valores entre 0 y 100 mm de lluvia
        registros.append(mes)

    return registros

def guardar_en_csv(nombre_archivo, registros):
    #Guardar registros en un archivo CSV.
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(registros)
    print(f"Datos guardados en el archivo: {nombre_archivo}")

def mostrar_registros_mes(registros, mes):
    #Mostrar registros pluviales de un mes específico.
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    print(f"Registros de {nombres_meses[mes - 1]}:")
    for dia, lluvia in enumerate(registros[mes - 1], start=1):
        print(f"Día {dia}: {lluvia} mm")