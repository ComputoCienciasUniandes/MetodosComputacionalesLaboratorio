# Parte 1. Para un numero cualquiera que entra por parametro, realice lo siguiente:
	# Si es par, dividalo entre 2
	# Si es par, multipliquelo por 3 y sumele 1
	# Repita esta procedimiento hasta llegar a 1
# Imprima la cantidad de iteraciones de la sucesion

import sys #Es necesario importar sys para poder tener acceso a los parametros de la consola

n=int(sys.argv[1])  # sys.argv es una lista de strings con los parámetros de la consola. En la variable "n" guardamos el segundo parámetro como un int.
i=0  # la variable "i" sirve para contar la cantidad de números que tendremos en la sucesión.
while(n!=1): #nuestro ciclo terminará cuando n sea igual a 1.
    i+=1
    print(n)
    if(n%2==0):
        n=int(n/2)
    else:
        n=int((n*3)+1)
print(n)
print('La cantidad de numeros en la sucesion es:',i+1)
