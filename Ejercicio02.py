def leer_tabla_multiplicar():
    while True:
        try:
            numero = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                break
            else:
                print("Por favor, introduce un número entre 1 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    nombre_archivo = f"tabla-{numero}.txt"

    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(f"Contenido del archivo '{nombre_archivo}':\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

leer_tabla_multiplicar()
