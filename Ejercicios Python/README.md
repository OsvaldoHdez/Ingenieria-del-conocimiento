### <html><H3 align="center"> Ejercicios python 1 al 10 </H3></html>
---
#### Ejercicio 1
Imprimir los enteros del 9 al 43
```Python
print("------Imprimir números enteros del 9 al 44------")
for i in range(9, 44):
    print(i)
```
---
#### Ejercicio 2
Imprimir los enteros impares del 7 al 51.
```Python
print("------Imprimir números impares del 7 al 51------")
for i in range(7, 52):
    if i % 2 != 0:
        print(i)
```
---
#### Ejercicio 3
Imprimir los enteros pares del 2 al 48.
```Python
print("------Imprimir números pares del 2 al 48------")
for i in range(2, 49):
    if i % 2 == 0:
        print(i)
```
---
#### Ejercicio 4
Imprimir los enteros del 1 al 30, apareados con sus recíprocos.
```Python
print("------Imprimir números enteros del 1 al 30 con su recíproco------")
for i in range(1, 31):
    print(i, f"Recíproco: 1/{i}")
```
---
#### Ejercicio 5
Imprimir una tabla de potencias del 2 que no exceda al 1000.
```Python
print("----------Tabla de potencias del número 2----------")
for i in range (1,11):
    print ("Dos elevado a la potencia", i, "es:", 2**i)
```
---
#### Ejercicio 6
Convertir pulgadas a yardas, y píes a pulgadas.
```Python
from os import system
system("cls")
import os
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()
print("--------Programa de conversión--------")
print("1. Convertir pulgadas a yardas")
print("2. Convertir píes a pulgadas")
print("3. Salir")
opción = input("Elija una opción: ")
if opción == "1":
    clear()
    print("--------Convertir pulgadas a yardas--------")
    pulgadas = float(input("Introduzca las pulgadas a convertir: "))
    print("Las pulgadas convertidas a yardas son:", pulgadas * 0.0277778)
elif opción == "2":
    clear()
    print("--------Convertir píes a pulgadas--------")
    píes = int(input("Introduzca los píes a convertir: "))
    print("Las píes convertidos a pulgadas son:", píes * 12)
elif opción == "3":
    print("Hasta luego...")
else:
    print("Elija un número entre 1 y 2")
print ("Fin de la ejecución")
```
---
#### Ejercicio 7
Determinar si un número dado es divisible entre 14.
```Python
print("--------Programa para determinar si un número dado es divisible entre 14--------")
número = int(input("Introduzca el número a comprobar: "))
if número % 14 == 0:
    resultado = número / 14
    print("El número introducido es divisible entre 14 y el resultado es:", resultado)
else:
    print("El número introducido no es divisible entre 14")
```
---
#### Ejercicio 8
Determinar si un entero dado es múltiplo de 6.
```Python
print("--------Programa para determinar si un número dado es múltiplo de 6--------")
número = int(input("Introduzca el número a comprobar: "))
if número % 6 == 0:
    resultado = número / 6
    print("El número introducido es múltiplo de 6 y cabe un número exacto de:", resultado)
else:
    print("El número introducido no es múltiplo de 6")
```
---
#### Ejercicio 9
Introducir y determinar si un número es "par" o "impar".
```Python
print("--------Programa para determinar si un número dado es par o impar--------")
número = int(input("Introduce el número a verificar: "))
if número % 2 == 0:
    print(f"El número dado '{número}' es un número PAR")
else:
    print(f"El número dado '{número}' es un número IMPAR")
```
---
#### Ejercicio 10
Escribir un programa que acepte 25 enteros positivos como datos y describir cada uno como "impar o "par".
```Python
print("--------Programa para determinar si una serie de números dados es par o impar--------")
números = []
for i in range(25):
    núm = int(input(f"Escriba el número {i+1}: "))
    if núm > 0:
        números.append(núm)
    else:
        print("Sólo números positivos")

print("------------------Resultado------------------")
for i in range(25):
    if números[i] % 2 == 0:
        print(f"El número dado '{números[i]}' es un número PAR")
    else:
        print(f"El número dado '{números[i]}' es un número IMPAR")
```
---