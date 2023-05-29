from os import system;system("cls")
"""
Ejercicio 1.
 
El complejo educacional “Chile 2030”, desea realizar una
aplicación computacional que le permita registrar en sus
establecimientos los alumnos a sus cursos.
Por tal razón le ha solicitado que cree un programa que
le permita a coordinación estudiantil registrar los
alumnos que pertenezcan a un curso en particular.
Como prototipo, usted desarrolla un algoritmo que permite
almacenar un número variable de alumnos a un curso, pero
con un máximo de 30 por curso.
"""

def registarPersonas():
    alumnos: list = []

    print("""Escriba "q" para salir en cualquier momento""")
    for i in range(29):
        i += 1
        alumno: list = []

        nombre: str = input("Ingrese nombre del alumno: ")
        if nombre == "q":
            break

        curso: str = input("Ingrese curso del alumno: ")

        alumno.append( nombre )
        alumno.append( curso )

        alumnos.append( alumno )
    
    print( alumnos )

registarPersonas()