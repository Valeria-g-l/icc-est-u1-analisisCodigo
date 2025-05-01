# import benchmarking as Ben  
from benchmarking import Benchmarking
from metodos import MetodosOrdenamiento  

if __name__ == '__main__':  
    print("funciona")
    
    benchmark = Benchmarking()  
    benchmark.benchmarking()    

    # Instancias
    metodos = MetodosOrdenamiento()

    tam = 10000
    arreglo_base = benchmark.buildArreglo(tam)

    metodos_dict = { 
        "burbuja": metodos.sortBubble,
        "seleccion": metodos.sort_seleccion,
    }

    resultados = []
    for nombre, metodo in metodos_dict.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tupla_resultado = (tam, nombre, tiempo)
        resultados.append(tupla_resultado)

    for resultado in resultados: 
        tam, nombre, tiempo = resultado
        print(f'Tamanio: {tam}, Metodo: {nombre}. Tiempo: {tiempo:.6f} segundos')
