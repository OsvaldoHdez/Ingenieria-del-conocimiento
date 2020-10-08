print("--------Programa para determinar si un número dado es divisible entre 14--------")
número = int(input("Introduzca el número a comprobar: "))
if número % 14 == 0:
    resultado = número / 14
    print("El número introducido es divisible entre 14 y el resultado es:", resultado)
else:
    print("El número introducido no es divisible entre 14")