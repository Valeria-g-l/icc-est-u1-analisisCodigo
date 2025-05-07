from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt

metodos = MetodosOrdenamiento()
benchmark = Benchmarking()

sizes = [500, 1000, 2000]

metodos_dic = {
    "burbuja": metodos.sortByBubble,
    "seleccion": metodos.sort_seleccion,
}

resultados = []

for size in sizes:
    array_base = benchmark.build_array(size)  
    for nombre, metodo in metodos_dic.items():
      
        tiempo = benchmark.medir_tiempo(metodo, array_base)
       
        tuplaResultado = (size, nombre, tiempo)
        resultados.append(tuplaResultado)

for resultado in resultados:
   
    size, nombre, tiempo = resultado
    print(f'Tamaño:  {size}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos')

# Diccionario para clasificar los tiempos según el método
tiempos_by_metodo = {
    "burbuja": [],
    "seleccion": [],
}

for size, nombre, tiempo in resultados:
    tiempos_by_metodo[nombre].append(tiempo)

# Crear una gráfica
plt.figure(figsize=(10, 6))

# Graficar una línea de tiempo para cada método
# donde x sean los tamaños del arreglo y y los tiempos obtenidos
for nombre, tiempos in tiempos_by_metodo.items():
    plt.plot(sizes, tiempos, label=nombre, marker='o')

# Agregar los parámetros
plt.title('Comparativa metodos')
plt.title('Valeria Guaman- 2025-05-07  9:00')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo (segundos)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()