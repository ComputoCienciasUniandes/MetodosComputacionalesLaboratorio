#include <stdlib.h>
#include <math.h>
#include <stdio.h>

void IC(double *u_init, double *x, int n_points, double c, double L);
void PT(double *u_init, double *x, double *u_future, int n_points, double c, double L, double dt);
void COPYI(double *u_init, double *u_past, double *u_present, double *u_future, double n_points);
void COPY(double *u_init, double *u_past, double *u_present, double *u_future, double n_points);

int main(){

double *x;
double *u_init;
double *u_past;
double *u_present;
double *u_future;
int n_points=1000;
double T=40; //N
double pho = 0.01;//kg/m
double c;
double L=100;
double dt = 0.0005;
int i;
int j;
int t=10000;
x = malloc(sizeof(double)*n_points);
u_init = malloc(sizeof(double)*n_points);
u_past = malloc(sizeof(double)*n_points);
u_present = malloc(sizeof(double)*n_points);
u_future = malloc(sizeof(double)*n_points);

c = pow(T/pho,0.5);

//printf("%f \n", c);

IC(u_init, x, n_points, c, L);
PT(u_init,  x,  u_future,  n_points,  c,  L, dt);
COPYI(u_init, u_past, u_present, u_future, n_points);

double dx = x[1]-x[0];
double r = c*dt/dx;

for(j=0;j<t;j++){
for(i=0;i<n_points-1;i++){
u_future[i] = 2*(1-pow(r,2))*u_present[i]-u_past[i]+pow(r,2)*(u_present[i+1]+u_present[i-1]);
COPY(u_init, u_past, u_present, u_future, n_points);
}

}

for(i=0;i<n_points;i++){
printf("%f \t %f \t %f\n",x[i], u_init[i], u_present[i]);
}

return 0;
}

void IC(double *u_init, double *x, int n_points, double c, double L){
int i;
x[0] = 0;
u_init[0] = 0;
u_init[n_points-1] = 0;
for(i=1;i<n_points-1;i++){
//u_init[i] = 0;
x[i] = x[i-1] + L/(n_points);
}



for(i=0;i<n_points-1;i++){
if(i<=800){
u_init[i] = 1.25*x[i]/L;}
if(i>800){
u_init[i] = 5-(5*x[i]/L);
}
}
}

void PT(double *u_init, double *x, double *u_future, int n_points, double c, double L, double dt){

int i;
double dx = x[1]-x[0];
double r = c*dt/dx;

for(i=1;i<n_points-1;i++){
u_future[i] = u_init[i] + pow(r,2)/2.0*(u_init[i+1]-2*u_init[i]-u_init[i-1]); 
}

}

void COPYI(double *u_init, double *u_past, double *u_present, double *u_future, double n_points){

int i;

for(i=0;i<n_points;i++){
u_past[i] = u_init[i];
u_present[i] = u_future[i];
}

}

void COPY(double *u_init, double *u_past, double *u_present, double *u_future, double n_points){

int i;

for(i=0;i<n_points;i++){
u_past[i] = u_present[i];
u_present[i] = u_future[i];
}

}

