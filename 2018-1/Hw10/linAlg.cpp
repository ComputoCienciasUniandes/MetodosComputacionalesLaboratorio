#include <iostream>
#include <cstdlib>
#include <ctime>



using std::cout;
using std::cin;
using std::endl;



// Declaramos las funciones que vamos a usar
double** get_Matrix(int rows, int cols);
double** matrix_product( double** A, double** B, int rowsA, int colsB, int rowsB);





// EL MAIN
int main(){
   
  
  
  // Inicializamos los valores de dimensiones de las matrices que vamos a usar
  int rowsA;
  int colsA;
  int rowsB;
  int colsB;
  
  
  // indices
  int i;
  int j;
   
  
  
  // Mensaje para indicar al usuario el que ingrese los las dimensiones de cada matriz
  cout << "Este programa realizara la multiplicacion matricial AxB" << endl << "--------------------------------------------------------------------" << endl;
  
  
  
  cout << "Ingrese el numero de filas de A: ";
  cin  >> rowsA;
  cout << "Ingrese el numero de columnas de A: ";
  cin  >> colsA;
  cout << "Ingrese el numero de filas de B: ";
  cin  >> rowsB;
  cout << "Ingrese el numero de columnas de B: ";
  cin  >> colsB;
  
  
  
  // Verificamos que las dimensiones tengan sentido
  if ( colsA != rowsB ){
    cout << "El numero de columnas de A debe ser igual al numero de filas de B " << endl;
    // El return en el main hace que se termine el programa
    return 0;
  }
  
  
  
  // Si el programa pasa por aqui ya validamos que colsA = rowsB dado que no se termino el programa
  
  // Llamamos la funcion get matrix para A y para B
  cout << "Ingrese el los valores de A: " << endl;
  // No es necesario inicializar la matriz porque eso se hace dentro de la funcion getMatrix()
  double **A = get_Matrix(rowsA,colsA);
  cout << "Ingrese el los valores de B: " << endl;
  // No es necesario inicializar la matriz porque eso se hace dentro de la funcion getMatrix()
  double **B = get_Matrix(rowsB,colsB);
  
  
  
  // Ahora que ya tenemos las matrices, podemos hacer la multiplicacion matricial
  double **C = matrix_product(A,B,rowsA,colsB,rowsB);
  
  
  
  // Recorremos la matriz C de dimensiones (rowsA,colsB) para imprimirla 
  cout <<"-----------------------------------------------------------------------------------" << endl << "Esta es la matriz C resultado de la multiplicacion: " << endl;
  for( i=0; i<rowsA; i++ ){
      
      cout << "| ";
      for( j=0; j<colsB; j++ ){
          
          cout << C[i][j]<<" ";
          
      }
      cout << "|"<< endl;
  }
   
  
  
  // Return 0 para saber que el programa termino
  return 0;


}




/*  Este metodo toma como parametros las dimensiones rows,cols y retorna una matriz que es ingresada por el usuario a traves de la consola
 *  La matriz es inicializada dentro de la funcion
 *  params: int rows -> El numero de filas de la matriz
 *  params: int cols -> El numero de columnas de la matriz
 *  return: double** -> La matriz ingresada por el usuario
 *
 */

double** get_Matrix(int rows, int cols){
    
    
    // Inicializamos un vector de M=rows vectores (fila)
    double** mat = new double*[rows];
    int l;
    
    
    // Recorremos cada uno de los vectores fila para inicializarlo con N=cols elementos (columnas)
    for( l=0; l<rows; l++ ){
        mat[l] = new double[cols];
    }
    
    
    // Mensaje para indicar al usuario el tamano de la matriz a ingresar
    cout << "Ingrese los valores de la matriz " << rows << "X" << cols << endl << "------------------------------------------------------------------------" << endl;
    int i;
    int j;
    // Recorremos la matriz ya inicializada para llenarla con los valores que ingresa el usuario
    for( i=0; i<rows; i++ ){
        for( j=0; j<cols; j++ ){
            // Variable auxiliar para captar el input del usuario
            double aux;
            // Mensaje para saber en que valor vamos
            cout << "Ingrese el elemento (" << i << " , " << j << "):  ";
            cin  >> aux;
            mat[i][j] = aux;
        }
    }
    
    
    // Recorremos la matriz para imprimirla 
    cout <<"-----------------------------------------------------------------------------------" << endl << "Esta es la matriz que ha ingresado: " << endl;
    for( i=0; i<rows; i++ ){
        cout << "| ";
        for( j=0; j<cols; j++ ){
            
            cout << mat[i][j]<<" ";
            
        }
        cout << "|"<< endl;
    }
    
    
    // Retorno
    return mat; 
      
    
}



/*  Este metodo toma como parametros dos matrices A,B junto con sus dimensiones y realiza el producto C = AB y lo retorna
 *  La matriz producto C es inicializada dentro de la funcion
 *  Las matrices A y B deben ser multiplicables
 *  params: double**A -> La matriz que multiplica por la derecha
 *  params: double**B -> La matriz que multiplica por la izquierda
 *  params: int rowsA -> El numero de filas de la matriz A
 *  params: int colsB -> El numero de columnas de la matriz B
 *  params: int rowsB -> El numero de filas de la matriz B que debe ser el mismo numero de columnas de A
 *  return: double** -> La matriz producto C = AB
 *
 */

double** matrix_product( double** A, double** B, int rowsA, int colsB, int rowsB){
    
    
    // Inicializamos un vector de M=rowsA vectores (fila)
    double** C = new double*[rowsA];
    int l;
    
    
    // Recorremos cada uno de los vectores fila para inicializarlo con N=colsB elementos (columnas)
    for( l=0; l<rowsA; l++ ){
        C[l] = new double[colsB];
    }
    
    
    // Vamos a recorrer cada elemento (i,j) de la matriz producto para calcular cada componente
    
    int i;
    int j;
    // Este for se encarga de recorrer cada fila de C. Hay rowsC=rowsA filas en C
    for( i=0; i<rowsA; i++ ){
        // Este for se encarga de recorrer cada columna de C. Hay colsC=colsB columnas en C    
        for( j=0; j<colsB; j++ ){

            // El elemento i,j de C es el producto punto del VECTOR FILA i de A << A[i][:] >> y el VECTOR COLUMNA j de B << B[:][j] >>
            // Inicializamos el valor en cero just in case
            C[i][j] = 0;
            
            // Como C++ NO es python, entonces NO podemos utilizar [:] para indicar "todos los indices"
            // En lugar, nos toca hacer el producto punto a mano
            int k;
            for( k=0; k<rowsB; k++ ){
                // Vamos anadiendo cada contribucion del producto punto a C
                C[i][j] += A[i][  k  ]*B[  k  ][j];
            
            }
        }
    }
    
    // Simplemente retornamos C
    return C;
}










