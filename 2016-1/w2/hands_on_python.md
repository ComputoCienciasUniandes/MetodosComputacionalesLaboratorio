# Hands-on Python/IPython
27-01-2016

Escribir un script de Python llamado sroot.py que calcule la raíz cuadrada de un número por medio del método de Newton. Hoy vamos a ejecutar este script dentro del entorno de IPython

- Primero: Que calcule y devuelva la raíz cuadrada de un número positivo (>0) tras 6 iteraciones. Escriba los comandos necesarios para que devuelva el valor de la solución y del número de iteración tras cada iteración. Bajo qué condiciones es adecuado el resultado, comparándolo con la función sqrt del módulo numpy?

- Segundo: Añada una condición para que el programa pare de iterar (y devuelva la solución) cuando la iteraciones sucesiva de la solución cambien en menos de 1e-14.

- Tercero: Dé formato a la salida que muestra la solución, para que aparezca en formato de punto fijo. Pruebe también a dejarlo en formato científico.

- Cuarto: Modifique su script para que ahora sea una función llamada sqrt2(x). Dentro de IPython, ejecute el script, y ejecute la función para probarla. Luego de un %reset, importe el módulo sroot, y ejecute la función sroot.sqrt2 para probar que funcione sobre distintos argumentos. Qué cambia en la manera de llamar la función si importamos directamente la función desde el módulo sroot?

- Quinto: Añada un docstring explicando cómo funciona la función sqrt2.

- Sexto: Especifique dentro de la función lo que debe ocurrir cuando el argumento sea 0. Especifique que la función retorne un nan cuando el argumento sea negativo, junto con un mensaje de error.

- Séptimo: Usando assert, verifique que el argumento de la función sea un float.

- Octavo: Añada un modo debug, para que en la ejecución del programa no muestre las iteraciones a menos que debug sea True.

