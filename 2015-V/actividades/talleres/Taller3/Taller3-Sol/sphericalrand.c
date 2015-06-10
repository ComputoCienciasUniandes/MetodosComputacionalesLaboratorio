#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double gaussrand (void);

int main(void){
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
