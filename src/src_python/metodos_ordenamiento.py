class MetodosOrdenamiento:

    def sortBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n - i - 1):  
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo  

    def sort_seleccion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n - 1):
            indice_minimo = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[indice_minimo]:
                    indice_minimo = j
            if indice_minimo != i: 
                arreglo[i], arreglo[indice_minimo] = arreglo[indice_minimo], arreglo[i]
        return arreglo  
 

 
    
