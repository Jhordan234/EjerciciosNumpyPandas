#Ejercicio Número 1

import numpy as np 
arr= np.random.rand(3, 3)

print("Array:\n" , arr)
print("Maximo:", arr.max())
print("Minimo:", arr.min())
print("Media:", arr.mean())

#Ejercicio Número 2

A= np.random.randint(1, 10, (2, 2))
B= np.random.randint(1, 10, (2, 2))

print("Matriz:\n", A)
print("Matriz:\n", B)
print("Suma:\n", A+B)
print("Resta:\n", A-B)
print("Multiplicacion:\n", A*B)
print("Divicion:\n", A/B)

#Ejercicio Número 3

arr= np.random.randint(1, 50 , 10)

print("Array completo: ", arr)
print("Primeros 5 elementos:", arr[:5])
print("Ultimos 3 elementos:", arr[-3:])
print("Elementos en posiciones pares:", arr[::2])