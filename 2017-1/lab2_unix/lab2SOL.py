# Script para contar el numero de estudiantes de matematicas del curso
# El archivo de notas debe estar descargado y encontrarse en el mismo directorio del script

# Abre el archivo en modo lectura "r"
archivo = open("01_notas.tsv", "r")

# La variable lineas es una lista. Cada elemento de la lista es una linea del archivo
lineas = archivo.readlines()

# Se inicializa un contador en 0 y se recorre cada linea, agregando uno si en dicha se encuentra el string "MATEMA"
contador = 0
for linea in lineas:
	if "MATEMA" in linea:
		contador += 1

# Se imprime el valor del contador. Se usa str(contador) para pasar de entero a string y poderlo concatenar con los mensajes.
print("El curso tiene " + str(contador) + " estudiantes de matematicas")
