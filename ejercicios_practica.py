#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.5

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.5"

def ej1():
    # Ejercicios de práctica numérica
    numero_1 = 5
    numero_2 = 7

    suma = numero_1 + numero_2
    print ("El resultado de la suma es:", suma)
    # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....

    # Imprimir en pantalla el resultado de la suma
    # print(....)

    # Repita el procedimiento para realizar la resta
    resta = numero_1 - numero_2
    print ("El resultado de la resta es:", resta)


def ej2():
    # Ejercicios de práctica numérica

    # Ahora los valores a operar deben ser ingresados por
    # consola con la función "input" como se ve a continuación
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    print("Usted ingresó el número: ", numero_1,"y el número:", numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    division = numero_1 / numero_2
    multiplicacion = numero_1 * numero_2
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6
    # NOTA: No coloque usted los nùmeros y resultados, use las variables

    # Suma
    print("El resultado de sumar ", numero_1, "y ", numero_2, "es ", suma)
    # Resta
    print("El resultado de restar ", numero_1, "y ", numero_2, "es ", resta)
    # División
    print("El resultado de dividir ", numero_1, "y ", numero_2, "es ", division)
    # Multiplicación
    print("El resultado de multiplicar ", numero_1, "y ", numero_2, "es ", multiplicacion)

def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Almacenar su nombre completo en una variable
    # Imprima su nombre completo
    nombre_completo = nombre + " " + apellido
    print(nombre_completo)
    
    # Imprimir la cantidad de letras que posee su nombre completo
    longitud_nombre = len(nombre) + len(apellido)
    print(longitud_nombre)

def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla
    print(palabra_1[0], palabra_2[0], palabra_3[0])


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    sub_1 = palabra_1[0:2] # Inovetip: Acá hay que tener cuidado, si usas [0:2] te trae solo las primeras dos letras
    # porque en [desde:hasta] el "desde" te lo toma desde el cero, pero en "hasta" comienza desde el uno...
    # cuando es así, te conviene usar [:3]
    sub_2 = palabra_2[-3:]

    
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    new_palabra = sub_1 + sub_2
    # Imprima en pantalla los resultados
    print(new_palabra)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
