import numpy as np
import random as rd

matriz = np.diag([1,1,1])
print(matriz)

for i in range(3):
    for j in range(3):
        matriz[i][j] = rd.randint(0,100)

print(matriz)


suma = matriz.sum()
promedio = suma / 9 

print(f"suma : {suma}")
print(f"promedio : {promedio}")

acumulador = 0

for i in range(3):
    for j in range(3):
        acumulador = acumulador + matriz[i][j]
print(f"suma : {suma}")

mayor = 0

for i in range(3):
    for j in range(3):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
print(mayor)
menor = 100

for i in range(3):
    for j in range(3):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
print(menor)
print("Diagonal........")
for i in range(3):
    for j in range(3):
        if i == j:
            print(matriz[i][j])
print("\n ............")