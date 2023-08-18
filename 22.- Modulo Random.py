# Modulo Random

import random

def main():
    numero_aleatorio = random.randint(1, 10)
    print(numero_aleatorio)

    lista_numeros = ["Hola", 15, 45.3, [1,2,3], False, {'nombre':'juan'}]
    elemento_aleatorio = random.choice(lista_numeros)
    print(elemento_aleatorio)

if __name__ == '__main__':
    main()