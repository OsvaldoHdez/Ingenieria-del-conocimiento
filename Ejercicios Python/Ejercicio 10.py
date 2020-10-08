print("--------Programa para determinar si una serie de números dados es par o impar--------")
contador = 0
for i in range(1, 25 + 1):
    números = int(input(f"Escriba el número {i}: "))
    if números % 2 == 0:
        print(f"El número dado '{números}' es un número PAR")
    else:
        print(f"El número dado '{números}' es un número IMPAR")