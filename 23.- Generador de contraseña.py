import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E']
    minusculas = ['a', 'b', 'c', 'd', 'e']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    simbolos = ['!', '@', '?', '=', 'ç', '&', '%']

    caracteres = mayusculas + minusculas + numeros + simbolos
    contrasena = []

    for i in range(12):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    # Convertir lista a string
    # "" o '' simbolizan un string vacio
    # .join concatenar cada elemento de la lista
    contrasena = ''.join(contrasena)

    return contrasena

def main():
    clave = generar_contrasena()
    print(clave)

if __name__ == '__main__':
    main()