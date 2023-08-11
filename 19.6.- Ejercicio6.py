# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, por cada una de ellas se preguntará que nota se obtuvo y finalmente debe mostrar mostrar una por una las asignaturas con su nota correspondiente.

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas = []

for asignatura in asignaturas:
    nota = float( input(f"Ingrese la nota de {asignatura}: ") )
    notas.append(nota)

print(notas)

for i in range( len(asignaturas) ):
    print(f"En {asignaturas[i]} tiene un {notas[i]}")