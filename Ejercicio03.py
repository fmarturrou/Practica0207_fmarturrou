def mostrar_linea_tabla():
    while True:
        try:
            n = int(input("Introduce el primer número (n) entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("Por favor, introduce un número entre 1 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    while True:
        try:
            m = int(input("Introduce el segundo número (m) entre 1 y 10: "))
            if 1 <= m <= 10:
                break
            else:
                print("Por favor, introduce un número entre 1 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    nombre_archivo = f"tabla-{n}.txt"

    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= len(lineas):
                print(f"Línea {m} del archivo '{nombre_archivo}': {lineas[m-1].strip()}")
            else:
                print(f"El archivo '{nombre_archivo}' no tiene {m} líneas.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

mostrar_linea_tabla()
