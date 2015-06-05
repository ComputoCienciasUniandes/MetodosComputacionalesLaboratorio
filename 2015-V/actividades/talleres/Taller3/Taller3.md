#Taller 3
*Métodos Computacionales - Laboratorio*

05-Jun-2015

Haga una copia de este archivo en su repositorio de GitHub en la carpeta /MC/Talleres/Taller3/. No olvide al final hacer un *commit* y un *push*.

# gcc, gnuplot y bash

Clone el repositorio [c-examples](https://github.com/tisnik/c-examples) de Pavel Tišnovský. **¡No lo clone al interior de su repositorio personal!**

1. Escriba un comando en `bash` que tome el código de todos los ejemplos en la carpeta `/c-examples/src/` y construya un archivo en Markdown con el código de los archivos en bloques de código bajo headers con el nombre del archivo correspondiente.

2. Ahora borre los archivos `c31_goto.c`, `c83_terminal_io.c` y `cA5_thread_join.c` y haga lo siguiente para los primeros (en orden alfabético) treinta archivos de C restantes.  Escriba un comando de `bash` que compile cada archivo de C, que luego imprima la línea que contiene la palabra *Example* y [la que le sigue](http://stackoverflow.com/questions/19274127/how-do-you-grep-a-file-and-get-the-next-5-lines), que luego ejecute el ejecutable, y que finalmente espere a que [el usuario presione alguna tecla](http://www.linuxquestions.org/questions/linux-general-1/how-to-make-shell-script-wait-for-key-press-to-proceed-687491/) para continuar con el siguiente archivo. 

3. Escriba un programa en C que genere 1000 puntos aleatorios uniformemente distribuidos sobre una esfera de radio unitario. Implemente la idea descrita al final del artículo [Sphere point picking](http://mathworld.wolfram.com/SpherePointPicking.html) y utilice la implementación para generar número con distribución normal [aquí](http://c-faq.com/lib/gaussian.html) detallada. Compile, ejecute y rediriga la salida al archivo `aleatorios_esfericos`. Luego escriba una secuencia de comandos de `gnuplot` para graficar estos puntos usando `splot`.

```
	#include <stdio.h>
	#include <stdlib.h>
	#include <math.h>

	double gaussrand (void);

	int main(void)
	{
		double randx;
		double randy;
		double randz;
		double norm;
		for( int i=0; i<=5000; i++)
		{
			randx=gaussrand();
			randy=gaussrand();
			randz=gaussrand();
			norm=sqrt(randx*randx + randy*randy + randz*randz);
			randx=randx/norm;
			randy=randy/norm;
			randz=randz/norm;
			printf("%f,%f,%f\n", randx,randy,randz);
		}
	return 0;
	}


	/*Taken from http://c-faq.com/lib/gaussian.html*/

	double gaussrand()
	{
		static double V1, V2, S;
		static int phase = 0;
		double X;

	if(phase == 0) {
		do {
			double U1 = (double)rand() / RAND_MAX;
			double U2 = (double)rand() / RAND_MAX;

			V1 = 2 * U1 - 1;
			V2 = 2 * U2 - 1;
			S = V1 * V1 + V2 * V2;
			} while(S >= 1 || S == 0);

		X = V1 * sqrt(-2 * log(S) / S);
	} else
		X = V2 * sqrt(-2 * log(S) / S);

	phase = 1 - phase;

	return X;
	}
```

```
	gnuplot << EOF
		set datafile separator ","
		set view equal xyz
		splot "sphericalrands.csv" using 1:2:3
	EOF
```

**Al terminar la clase ejecute `lottery.sh` para saber si su taller va a ser revisado.**