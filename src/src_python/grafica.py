import matplotlib
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]

nombre_linea="linea 1"

plt.plot(x, y, label="linea 1", color="blue")

#Agregar parametros
plt.title("Primero grafico")
plt.xlabel("Datos eje X")
plt.xlabel("Datos eje y")
plt.legend()
plt.show()