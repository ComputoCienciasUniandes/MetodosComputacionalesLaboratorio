#include <stdlib.h>
#include <stdio.h>

/*Este es un ejemplo pequeño de cómo funcionan los punteros. La función scanf recibe como parámetro un puntero (dirección en mamoria) y modifica lo que hay en dicha dirección */


int main()
{
    char *a=malloc(sizeof(char)*2);
    
    printf("%p \n",a);
    
    
    printf("Escriba su nombre: ");
    
    /* La funcicón scanf recibe como parámetro una dirección en memoria */
    
    scanf("%s",a);
    printf("Su nombre es: ");
    printf("%s\n",a);
    
    
    char b[10];
    
    printf("Escriba su apellido: ");
    
    /* La funcicón scanf recibe como parámetro una dirección en memoria */
    
    scanf("%s",b);
    
    printf("Su apellido es: ");
    printf("%s\n",b);
    
   
   return(0);
    
}
