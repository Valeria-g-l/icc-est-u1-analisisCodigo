import java.util.Arrays;

public class MetodosOrdenamiento {

    // Método de burbuja tradicional con errores
    // Error encontrado: El metodo retorna un arreglo de enteros vacio linea 21
    //Solucion: Cambiar el return para que regrese la variable "arreglo"
    public int[] burbujaTradicional(int[] arregloOriginal) {
        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        int n = arreglo.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arreglo[i] > arreglo[j]) {
                    // Intercambio de elementos
                    int temp = arreglo[i];
                    arreglo[i] = arreglo[j];
                    arreglo[j] = temp;
                }
            }
        }
        return arreglo; //Error corregido
    }

    // Método de burbuja tradicional con errores
    // Error encontrado: En el if hace que el arreglo se imprima descendente linea 34
    //Solucion: Cambie el signo de menor que a mayor que

    public int[] burbujaTradicionalSegundo(int[] arregloOriginal) {
        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        int n = arreglo.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arreglo[i] > arreglo[j]) {// Arreglo ordenado
                    // Intercambio de elementos
                    // Estas 3 lineas NO DEBEN ser modificadas
                    int temp = arreglo[i];
                    arreglo[i] = arreglo[j];
                    arreglo[j] = temp;
                }
            }
        }

        return arreglo;

    }

    // Método de burbuja tradicional con errores
    // Error encontrado: No imprime en consola y al solucionar ese error imprime en desorden
    //Solucion: En el primer for se quito el -1
        // En el segundo for en vez de j=0 se puso i+1
        //En el if en el primer arreglo J se puso i, ademas se dejo de sumar en el segundo arreglo j+1
        //De la linea 64-66 Se colocaron bien i y j
    public int[] burbujaTradicionalTercero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        int n = arreglo.length;
        for (int i = 0; i < n ; i++) {// error corregido
            for (int j = i+1; j < n; j++) {// error corregido
                if (arreglo[i] > arreglo[j]) {// error corregido
                    // Intercambio de elementos
                    int temp = arreglo[i];// error corregido
                    arreglo[i] = arreglo[j];// error corregido
                    arreglo[j] = temp;// error corregido
                }
            }
        }
        return arreglo;
    }
    

    // Método de selección con errores
    // Error encontrado: No retorna ningun arreglo
    //Se retorno el arreglo con "return arreglo"
    public int[] SeleccionPrimero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

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
        return arreglo; //Error corregido
    }

    // Método de selección con errores
    // Error encontrado: No imprime el arreglo
    //En el primer for se agrego -1     En el segundo for cambie para que el for J sume
    public int[] seleccionSegundo(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        for (int i = 0; i < arreglo.length-1; i++) {// Error Corregido
            int indiceMinimo = i;

            for (int j = i + 1; j < arreglo.length; j++) {// Error corregido
                if (arreglo[j] < arreglo[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }

            int smallerNumber = arreglo[indiceMinimo];
            arreglo[indiceMinimo] = arreglo[i];
            arreglo[i] = smallerNumber;
        }
        return arreglo;
    }

    // Método de selección con errores
    // Error encontrado: El arreglo se imprime en desorden
    //
    public int[] seleccionTercero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        for (int i = 0; i < arreglo.length - 1; i++) {
            int indiceMinimo = i;

            for (int j = i + 1; j < arreglo.length; j++) {
                if (arreglo[j] < arreglo[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }

            int smallerNumber = arreglo[indiceMinimo];//
            arreglo[indiceMinimo] = arreglo[i];
            arreglo[i] = smallerNumber;//
        }
        return arreglo;
    }

    // Método de inserción con errores
    // Error encontrado:
    public int[] insercionPrimero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);
        for (int j = 1; j < arreglo.length; j++) {
            int key = arreglo[j];
            int i = j - 1;

            while (i > 0 && arreglo[i] < key) {
                arreglo[i + 1] = arreglo[i];
                i--;
            }
            arreglo[i + 1] = key;
        }
        return arreglo;
    }

    // Método de inserción con errores
    // Error encontrado:
    public int[] insercionSegundo(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);
        for (int j = 1; j < arreglo.length; j++) {
            int actual = arreglo[j];

            int i = j - 1;
            for (; j >= 0 && arreglo[j] > actual; j--) {
                arreglo[j + 1] = arreglo[j];
            }
            arreglo[i + 1] = actual;
        }
        return arreglo;
    }

    // Método de inserción con errores
    // Error encontrado:
    public int[] insercionTercero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);
        for (int j = 1; j < arreglo.length; j++) {
            int key = arreglo[j];
            int i = j;

            while (i > 0 && arreglo[i] < key) {
                arreglo[i + 1] = arreglo[i];
                i++;
            }
            arreglo[i + 1] = key;
        }
        return new int[] { 15, 34, 1, 2, 5, 6, 7, 10 };
    }

}
