import numpy as np
from numpy import linalg as lng #Vamos a importar el paquete de álgebra lineal de Numpy.

#Crear vectores y matrices

vector=np.array([0,4,6])
#print(vector)

matriz=np.matrix([[1,3,5],[3,4,6],[5,6,4]])
print(matriz)

#operaciones entre vectores y matrices

#en vectores tenemos producto punto y producto por escalar

vector1=np.array([4,7,8])
#print(vector1)

vector2=np.dot(vector,vector1)

#print(vector2)

#vector3=2*vector

#print(vector3)

#Autovalores y autovectores

eigenvalues, eigenvectors = lng.eig(matriz)

#print (eigenvalues, "\n")
#print(eigenvectors)


#norma, determinante y otras medidas

vector4_1=lng.norm(vector)
vector4_2=lng.norm(vector1)

#print(vector4_1)
#print(vector4_2)


det1=lng.det(matriz)

#print(det1)

matriz2=([[1,0,0],[0,2,0],[0,0,3]]) #Matriz diagonal para verificar

#print(matriz2)
det2=lng.det(matriz2) 

#print(det2)

#resolver sistemas de equaciones lineales e invertir matrices

A=np.matrix([[2,-2],[5,1]])
b=np.array([2,3])

#print(A,b)

x=lng.solve(A,b)  #Encuentra x para el sistema "Ax=b"

#print(x)

inver=lng.inv(matriz)

print(inver)


