
# coding: utf-8

# In[7]:

import matplotlib.pyplot as plt
import numpy as np

# Carga los datos
data = np.loadtxt('room-temperature.csv', skiprows=1, usecols=[1,2,3,4],delimiter=',')
front_left = data[:,0]
front_right = data[:,1]
back_left = data[:,2]
back_right = data[:,3]

# Grafica los datos en funcion del tiempo
figur, axarr = plt.subplots(4, 1, figsize= (10,10))

axarr[0].plot(front_left)
axarr[0].set_title('Front left')
axarr[0].set_ylabel('Temperature (AU)')
axarr[0].set_xlim([0,len(front_left)])
axarr[0].set_ylim([290,300])

axarr[1].plot(front_right)
axarr[1].set_title('Front right')
axarr[1].set_ylabel('Temperature (AU)')
axarr[1].set_xlim([0,len(front_left)])
axarr[1].set_ylim([290,300])

axarr[2].plot(back_left)
axarr[2].set_title('Back left')
axarr[2].set_ylabel('Temperature (AU)')
axarr[2].set_xlim([0,len(front_left)])
axarr[2].set_ylim([290,300])

axarr[3].plot(back_right)
axarr[3].set_title('Back right')
axarr[3].set_xlabel('Time (AU)')
axarr[3].set_ylabel('Temperature (AU)')
axarr[3].set_xlim([0,len(front_left)])
axarr[3].set_ylim([290,300])

figur.subplots_adjust(hspace=0.5)
plt.savefig('room.pdf')
plt.close()

# Realiza PCA, retorna los valores propios, vectores propios y los datos en la base de los vectores propios (scores)
# Tambien imprime los mensajes necesarios
def pca(data_matrix):
    '''data_matrix must be the data matrix by COLUMNS i.e. a column is a variable and a row is an observation'''
    data_matrix = data_matrix.T
    cov_matrix = np.cov(data_matrix)
    print('La matriz de covarianza es:')
    print(cov_matrix)
    print('')
    values, vectors = np.linalg.eig(cov_matrix.T)
    print('Las dos componentes principales en orden ascendente son:')
    print(vectors[:,0], ' con valor ', values[0])
    print(vectors[:,1], ' con valor ', values[1])
    
    total_values = np.sum(values)
    
    print('\nLa primera componente explica el', values[0]/total_values * 100, '% de la varianza')
    print('La segunda componente explica el', values[1]/total_values * 100, '% de la varianza')
    
    scores = np.dot(data_matrix.T, vectors)
    return values, vectors, scores

# Escala y centra los datos, retorna la matriz de datos reescalada.
def center_scale(data):
    data_scaled = np.zeros_like(data)
    for i in range(len(data[0])):
        av_col = np.mean(data[:,i])
        std_col = np.std(data[:,i])
        for j in range(len(data)):
            data_scaled[j,i] = ( data[j,i] - av_col )/ std_col
    return data_scaled

# Grafica la variable j vs la variable i del los datos junto con las dos componentes principales proyectadas en 
# el plano de dichas variables.
def plot_eigen(data, i, j, vectors, labels, name):
    '''Grafica las variables i, j de los datos junto con las dos componentes principales'''
    plt.scatter(data[:,i], data[:,j])
    x = np.linspace(min(data[:,i]), max(data[:,i]))
    plt.plot(x, x*vectors[j,0]/vectors[i,0], linewidth = 1.0, c='r', label = 'Primer vector')
    plt.plot(x, x*vectors[j,1]/vectors[i,1], linewidth = 1.0, c='y', label = 'Segundo Vector')
    plt.title(labels[j]+ ' vs. '+ labels[i])
    plt.xlabel(labels[i])
    plt.ylabel(labels[j])
    plt.ylim(min(data[:,j])-1, max(data[:,j])+1)
    plt.legend(loc=0)
    plt.savefig(name)
    plt.close()

# Escala los datos    
data_matrix = center_scale(data)
# Realiza PCA
values, vectors, scores = pca(data_matrix)    
# Realiza las graficas de los vectores
labels = ['Front Left', 'Front Right', 'Back left', 'Back right']
plot_eigen(data_matrix, 0, 1, vectors, labels, 'pca_fr_fl.pdf')
plot_eigen(data_matrix, 0, 2, vectors, labels, 'pca_bl_fl.pdf')



