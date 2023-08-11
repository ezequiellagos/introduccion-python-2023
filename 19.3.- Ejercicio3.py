# Cree un programa que envíe saludos al usuario dependiendo del nombre que ingrese, pero si ingresa la palabra salir, se termina el programa.

nombre = input("Ingrese un nombre: ")

while nombre.lower() != "salir":
    print(f"Hola {nombre.upper()}")
    print(nombre)
    nombre = input("Ingrese un nombre: ")