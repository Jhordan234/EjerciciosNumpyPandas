#Ejercicio Número 1 

import pandas as pd
import numpy as np 

df= pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])

print(df)

print("Primeras 3 filas:\n", df.head(3))
print("Columna B:\n", df['B'])
print("Media por columna:\n", df.mean())

#Ejercicios Número 2

data= {'Nombre':['Pedro', 'Robyn', 'Carlos', 'Megumi', 'Diana'],
       'Sueldo':[10000, 67000, 45000, 50000, 60000]}
df= pd.DataFrame(data)

df_filtrado= df[df['Sueldo']>30000]
print(df_filtrado)

#Ejercicio Número 3
data = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Auriculares'],
    'Cantidad': [3, 10, 5, 2, 8],
    'Precio_Unitario': [800, 25, 50, 200, 40]
}

df = pd.DataFrame(data)
df['Total_Venta'] = df['Cantidad'] * df['Precio_Unitario']
df_mas_vendidos = df[df['Cantidad'] > 5]

total_ingresos = df['Total_Venta'].sum()

print("DataFrame original:")
print(df)
print("\nProductos con más de 5 ventas:")
print(df_mas_vendidos)
print(f"\nTotal de ingresos: ${total_ingresos}")
