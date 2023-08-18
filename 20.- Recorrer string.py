# Recorrer string y string

def main():
    nombre = input("Ingrese un nombre: ")
    print( len(nombre) )
    for letra in nombre:
        print(letra)


    lista = ["elemento 1", "elemento 2", "elemento 3", "elemento 4", "elemento 5"]
    print( len(lista) )
    for elemento in lista[::-1]:
        print(elemento)
        print(elemento[::-1])
        #for letra in elemento[::-1]:
        #    print(letra, end="")

if __name__ == '__main__':
    main()