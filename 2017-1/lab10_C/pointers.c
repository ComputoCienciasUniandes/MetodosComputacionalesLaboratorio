#include <stdio.h>
#include <stdlib.h>

int main(void){
    
    /* Esta es una variable normal*/
    int alpha=2.0;
    
    printf("%s\n","Variable alpha:");
    printf("%d\n",alpha);
    
    /* ¿Qué pasa si imprimimos &a? */
    printf("%s\n","Variable alpha con &:");
    printf("%p\n \n",&alpha);
    
    /* */
    
    /* Creamos una variable puntero*/
    
    int *gamma=malloc(3*sizeof(int)); /*Alocamos memoria*/
    
    gamma[0]=2;
    gamma[1]=3;
    gamma[2]=3;

    
    printf("%s\n","Variable puntero gamma:");
    printf("%p\n",gamma);
    
    printf("%s\n","Variable puntero gamma con *:"); /*Solo imprimirá el primer elemento*/
    printf("%d\n",*gamma);
    
    printf("%s\n","Variable puntero gamma &:");  /*El puntero tambien tiene una dirección en memoria (La dirección en memoria de la dirección en memoria :) )*/
    printf("%p\n",&gamma);

    printf("%s\n","Componentes de la Variable puntero gamma:");
    printf("%d, %d, %d\n",gamma[0],gamma[1],gamma[2]); /*Esta es la manera de imprimir los demás elementos*/ 
    

}

