#!/bin/bash

# Descarga el archivo
wget http://www.gutenberg.org/cache/epub/2000/pg2000.txt

# Corre el analisis sobre el archivo
# En este caso, el programa esta disenado para que el nombre del archivo sea parametro de entrada en la terminal
python analisis.py pg2000.txt

# Remueve el archivo descargado
rm pg2000.txt
