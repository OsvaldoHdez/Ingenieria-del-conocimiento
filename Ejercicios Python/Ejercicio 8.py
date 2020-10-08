print("--------Programa para determinar si un número dado es múltiplo de 6--------")
número = int(input("Introduzca el número a comprobar: "))
if número % 6 == 0:
    resultado = número / 6
    print("El número introducido es múltiplo de 6 y cabe un número exacto de:", resultado)
else:
    print("El número introducido no es múltiplo de 6")