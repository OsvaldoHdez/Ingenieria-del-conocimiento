print("--------Programa para determinar si una serie de números dados es par o impar--------")
números = []
for i in range(25):
    núm = int(input(f"Escriba el número {i+1}: "))
    números.append(núm)

print("------------------Resultado------------------")
for i in range(25):
    if números[i] % 2 == 0:
        print(f"El número dado '{números[i]}' es un número PAR")
    else:
        print(f"El número dado '{números[i]}' es un número IMPAR")