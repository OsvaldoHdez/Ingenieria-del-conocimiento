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
    print("Las pulgadas convertidas a yardas son:", pulgadas * 0.027777777777778)
elif opción == "2":
    clear()
    print("--------Convertir píes a pulgadas--------")
    píes = int(input("Introduzca los píes a convertir: "))
    print("Las píes convertidos a pulgadas son:", píes * 12)
elif opción == "3":
    print("Hasta luego..")
else:
    print("Elija un número entre 1 y 2")
print ("Fin de la ejecución")