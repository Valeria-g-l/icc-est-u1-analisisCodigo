class MetodosOrdenamiento:

    def sortBubble(self,arreglo):
        arreglo =arreglo.copy()
        n=len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i]>arreglo[j]:
                    arreglo[i], arreglo[j]=arreglo[j],arreglo[i]
                    #aux=arreglo[i]
                    #arreglo[i]=arreglo[j]
                    #arreglo[j]=aux

    
    def sort_seleccion(self,array):
        arreglo =arreglo.copy()
        for (int i = 0; i < arreglo.length - 1; i++) {
            int indiceMinimo = i;
            for (int j = i + 1; j < arreglo.length; j++) {
                if (arreglo[j] < arreglo[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }
            int smallerNumber = arreglo[indiceMinimo];
            arreglo[indiceMinimo] = arreglo[i];
            arreglo[i] = smallerNumber;
        }
        return arreglo; 
    
