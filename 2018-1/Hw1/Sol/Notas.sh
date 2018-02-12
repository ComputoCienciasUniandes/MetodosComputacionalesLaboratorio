#!/bin/bash

# Concatena los 3 archivos en total.csv para hacer los calculos mas sencillos
cat Sec1.csv Sec2.csv Sec3.csv > Total.csv

# Cambia todos los NaN por ceros
sed -i 's/NaN/0/g' Total.csv

# El calculo del promedio se hace dentro de awk (teniendo cuidado con la ultima fila)
# awk imprime solo los estudiantes que pasaron y luego se cuentan cuantas lineas hay con cat
# La opcion -F permite elegir el separador

awk -F',' '{ if(  ((0.2*$1) + (0.25*$2) + (0.25*$3) + (0.3*$4*(5.0/8.0)))  >= 3.0  ) print $0 }' Total.csv | wc -l

echo " estudiantes pasaron el curso."

# Espacio para que se vea mas ordenado
echo " "

# El complemento de la condicion anterior

awk -F',' '{ if(  ((0.2*$1) + (0.25*$2) + (0.25*$3) + (0.3*$4*(5.0/8.0)))  < 3.0  ) print $0 }' Total.csv | wc -l

echo " estudiantes perdieron el curso."

# Remueve el archivo temporal Total.csv
rm Total.csv
