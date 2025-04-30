import random
from metodos_ordenamiento import MetodosOrdenamiento
import time
class Benchmarking:
    def_init__(self):
    print("Bench inicializado")
    self.mOrdenamiento=MetodosOrdenamiento()

    arreglo=self.build_arreglo(1000)

    tarea  = lamda:self.mOrdenamiento.sortByBybble(arreglo)
    tiempoMillis=self.contar_concurrent_time_milles(tarea)
    tiempoNano=self.contar_con_nano_time(tarea)

    print(f'Tiempo:  {tiempoMillis}')
    print(f'Tiempo : {tiempoNano}')

    def buildArreglo(self, tamano):
        array=[]
        for i in range(tamano):
            numero= random.randint(0,99999)
            array.append(numero)
        return array

    def contar_concurrent_time_milles(self,tarea):
        inicio=time.time
        task()
        fin=time.time
        returnfin-inicio
        

    def contar_con_nano_time(self, tarea)
        inicio=time.time_ns
        task()
        inicio=time.time_ns
        return  fin-inicio