import sys
import matplotlib.pyplot as plt

# Carga el archivo con permisos de lectura, teniendo en cuenta el nombre del archivo que viene por parametro de la terminal sys.argv[1]
arch = open(sys.argv[1], 'r')

# La lista de las lineas (es una lista de strings)
lines = arch.readlines()[36:-373] # En clase vimos que el libro empezaba en la linea 36 y terminaba 373 lineas antes
# Es valido si toman desde la 40 hasta 380 antes

# Concatena todo en un string
libro_completo = ""
for line in lines:
    libro_completo += line
    
# Calcula la palabra mas larga y tambien calcula la lista de longitudes requerida para el histograma
masLarga = ""
listaLongitudes = []
for palabra in libro_completo.split():
    
    # Verifica si la palabra actual es mas larga que la mas larga que se ha encontrado hasta ahora
    if ( len(palabra) > len(masLarga) ):
        # Si lo es, actualiza la palabra mas larga con la nueva que se ha encontrado
        masLarga = palabra
    
    # Anade la longitud de la palabra actual a la lista de longitudes
    listaLongitudes.append(len(palabra))

# Imprime cual es la palabra mas larga
print "La palabra mas larga del texto es : " + masLarga

# Realiza el histograma
# bins = range(max(listaLongitudes+1)) es para que las barras esten centrada en los numeros enteros 1,2,3,....maximo y no en fraccionarios, que no tiene tanto sentido
# align = "left" para que quede centrado en el valor correspondiente
# El parametro anterior es opcional, es unicamente para visualizar mejor
plt.hist(listaLongitudes,bins = range(max(listaLongitudes)+1), align = 'left')
plt.title("Histograma de palabras en el Quijote")
plt.xlabel("Longitud de la palabra")
plt.ylabel("Numero de palabras")
plt.savefig("hist.png")
