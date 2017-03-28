#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Aquí lo importante es entender cómo generar la función exponencial y cómo guardar los datos en un archivo*/

int main(){
    
    float lambda = 1.0/5.0;
	float N0 = 10.0;
	float dt = 0.001;

	float t_total = 3.0/lambda;
	int n_points = (int)t_total/dt;
	int i;
	
	float t = 0.0;
	float n = N0*exp(-lambda*t);
	
    FILE *out = fopen("data.txt","w+"); /* Abrir el archivo*/
    
    fprintf(out, "%f %f\n",t, n);  /*Imprimir en el archivo*/
    	
	for(i=0;i<n_points;i++){
		t += dt;
		n = N0*exp(-lambda*t);
		fprintf(out,"%f %f\n", t, n);
	}
    fclose(out);    /*Cerrar el archivo */

	return 0;
    
}