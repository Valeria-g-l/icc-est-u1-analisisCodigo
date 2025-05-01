import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    def __init__(self):
        print('Bench initialization')

    def ejemplo(self):
        self.mOrdenamiento = MetodosOrdenamiento()
        array = self.buildArreglo(5000)

        tarea = lambda: self.mOrdenamiento.sortByBubble(array.copy())  
        timeMillis = self.count_with_current_time_millis(tarea)
        timeNanos = self.count_with_nano_time(tarea)

        print(f'Time Millis: {timeMillis}')
        print(f'Time Nanos: {timeNanos}')

    def buildArreglo(self, size):
        return [random.randint(0, 99999) for _ in range(size)]

    def count_with_current_time_millis(self, tarea):  
        inicio = time.time()
        tarea()
        fin = time.time()
        return fin - inicio

    def count_with_nano_time(self, tarea): 
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return fin - inicio

    def medir_tiempo(self, tarea, array):
        array_copia = array.copy() 
        inicio = time.perf_counter()
        tarea(array_copia)
        fin = time.perf_counter()
        return fin - inicio
