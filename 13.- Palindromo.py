# Palindromo

# Palabra que se lee igual al derecho que al reves
# Ana
# Luz Azul
# Yo hago Yoga hoy

# Escribir una funcion que identifiue si una palabra es palindromo o no

def palindromo(palabra):
    palabra = palabra.strip()
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")

    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

def main():
    palabra = input("Ingrese palabra: ")
    resultado = palindromo(palabra)

    if resultado:
        print("Es palindromo")
    else:
        print("No es palindromo")

# Punto de entrada
# Es una buena practica
if __name__ == '__main__':
    main()