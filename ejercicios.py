import numpy as np
import random
#EJERCICIO 2
x = range(0, 10)
c = np.array([random.randint(1, 1000) for i in x])
print(c)

num_par = 0
for num in c:
    if num % 2 == 0:
        num_par += 1

print("El número de pares es:", num_par)

num_impar = 0
for num in c:
    if num % 2 != 0:
        num_impar += 1
print("El número de impares es:", num_impar)







