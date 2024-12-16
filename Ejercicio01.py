entero = int(input("Introduce un número entero entre el 1 y el 10\n"))

if 1 <= entero <= 10:

    fichero = f"tabla-{entero}.txt"
    

    with open(fichero, "w") as file:
       
        for enteros in range(1, 11):
            file.write(f"{entero} x {enteros} = {entero * enteros}\n")
    

    print(f"La tabla de multiplicar se ha guardado en '{fichero}'")
else:
    print("El número debe estar entre 1 y 10.")
