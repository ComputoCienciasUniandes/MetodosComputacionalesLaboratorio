#Experimento 1 - Distribución de Velocidades de Maxwell - Boltzmann 2D
*Métodos Computacionales - Laboratorio*

10-Jun-2015

Haga una copia de este archivo en su repositorio de GitHub en la carpeta /MC/Experimentos/Exp1/. No olvide al final hacer un *commit* y un *push*.

Descargue el [software](http://www.ph.biu.ac.il/~rapaport/mdbook/) del libro *The Art of Molecular Dynamics Simulation de Rapaport*, descomprima y reemplace el archivo `/src/pr_02_1.in` con [esta](https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesLaboratorio/master/2015-V/actividades/experimentos/Exp1/pr_02_1.c) ligera modificación. El código simula un gas de discos suaves que interactúan de acuerdo al [potencial de Lennard Jones](http://en.wikipedia.org/wiki/Lennard-Jones_potential) truncado. El método de integración empleado es el [leapfrog method](http://en.wikipedia.org/wiki/Leapfrog_integration). Las velocidades iniciales de las partículas tienen una distribución uniforme y sus posiciones iniciales se toman en una cuadrícula.

Compile usando:

```
gcc -O -o pr_02_1 pr_02_1.c -lm
``` 

Copie el ejecutable a una nueva carpeta llamada *MB* junto con el archivo de configuración `/data/pr_02_1.in`. El archivo `.in` contiene las condiciones experimentales y el experimento se ejecuta de la siguiente forma:

```
./pr_02_1 < pr_02_1.in
```

Las condiciones experimentales están determinadas por las siguientes cantidades.

| deltaT        | descripción |
|:-------------:|
| density | densidad, determina la separación inicial entre partículas |
| initUcell | tamaño de la cuadrícula, una partícula por celda |
| stepAvg | número de iteraciones entre toma de datos |
| stepEquil | iteraciones esperadas para llegar al equilibrio |
| stepLimit | número de pasos máximos |
| temperature | temperatura |


El output del experimento son una serie de líneas con las posiciones y velocidades de cada partícula cada `stepAvg` iteraciones.

| Columna        | Cantidad       |
|:-------------:|:-------------:|
| 1     | x | 
| 2     | y |
| 3 | vx      | 
| 4 | vy |

Diseñe y ejecute un procedimiento experimental para determinar la evolución de la distribución de rapideces de las partículas en diferentes condiciones. Haga su análisis de datos en un cuaderno de iPython llamado `Rayleigh.ipynb`. El análisis debe incluir animaciones, histogramas y ajustes de tipo apropiado.

[Rayleigh distribution](http://en.wikipedia.org/wiki/Rayleigh_distribution)

**Al terminar la clase ejecute `lottery.sh` para saber si el informe de su experimento va a ser revisado.**
