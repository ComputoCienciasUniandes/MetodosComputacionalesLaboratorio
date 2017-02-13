import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
from scipy.stats import norm

# Parte 2. Genere 1000 numeros aleatorias con una distribucion exponencial, grafique el histograma y compare con la PDF conocida de dicha distribucion.

# Luego Realice 1000 sumas de 1000 numeros aleatorios con una distribucion exponencial y compare (haga un fit) a una distribucion normal, verificando el teorema del limite central.

n=[]
for i in range(1000):
    n.append(np.random.exponential(10)) # Llenamos la lista "n" con numeros aleatorios con distribución exponencial de media 10.
    
    
loc1,scale1 = expon.fit(n)  # obetenemos los parámetros "Scale" y "loc" de un fit sobre los datos en la lista "n". Para este caso, la media de la distribución es igual a "scale".
print(scale1,loc1) #imrpimimos estos parámetros

x = np.linspace(0,50, 100)  
y=expon.pdf(x,scale=scale1, loc=loc1)  # Graficamos una distribución exponencial con media 10.

f, fig1 = plt.subplots(1,1)  

fig1.plot(x, y,'r-', lw=5, alpha=0.6, label='expon pdf') #Graficamos x vs y (distribución)
fig1.hist(n,bins=50,normed=True) #Hacemos el histograma de n. Es importante que esté normalizado.
f.savefig('graficas.png') #Guardamos en una archivo las gráficas.

#Hasta aca verificamos que los datos si pertenecen a la distribución dada. Ahora tenemos que repetir el proceso creando una variable que es la suma de las variables generadas.


sumas=[] #En cada elemento de la lista "sumas" guardamos la suma de 1000 varables aleatorias con distribución exponencial. 
for i in range(1000):
    suma=0
    for j in range(1000):
        suma+=np.random.exponential(10)
    sumas.append(suma)

loc2,scale2 = norm.fit(sumas)   # obetenemos los parámetros "scale" y "loc" de un fit sobre los datos en la lista "n". Para este casp, la media de la distribuciíon es igual a "loc" y la desviación estandar a "scale".
print(scale2,loc2)

x2 = np.linspace(8000,11000,10000)  
y2=norm.pdf(x2,loc=loc2,scale=scale2)  # Graficamos una distribución normal con media igual a "loc2" y desviación estandar igual a "scale".


f2, fig2 = plt.subplots(1,1)
fig2.plot(x2, y2,'r-', lw=5, alpha=0.6, label='norm pdf')
fig2.hist(sumas,bins=50, normed=True)
f2.savefig('limite.png')
