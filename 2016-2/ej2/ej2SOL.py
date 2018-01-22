'''
Laboratorio de Metodos Computacionales
Solucion Ejercicio 2
'''

import numpy as np

#Funcion que retorna el alcance maximo
def alcance_maximo(theta, v0, g):
	return v0**2 * np.sin(2*theta)/g

#Funcion que retorna la derivada del alcance maximo
def derivada_alcance_maximo(theta, v0, g, h):
	return (alcance_maximo(theta + h, v0, g) - alcance_maximo(theta, v0, g) )/h

#Funcion que retorna la segunda derivada del alcance maximo
def derivada2_alcance_maximo(theta, v0, g, h):
	return (alcance_maximo(theta + h, v0, g) - 2.0*alcance_maximo(theta, v0, g) + alcance_maximo(theta-h, v0, g))/h**2.0

#Funcion que utiliza el metodo de Newton para buscar el cero de la funcion derivada, correspondiente al alcance maxim
def newton(init_guess, delta, v0, g, h):
    
    guess = init_guess
    while np.abs(derivada_alcance_maximo(guess, v0, g, h)) > delta:
        guess = guess - derivada_alcance_maximo(guess, v0, g, h)/derivada2_alcance_maximo(guess, v0, g, h)
        
    return guess

#Corre la funcion Newton para varios guess iniciales
for i in range(2,9):
	guess = np.pi/2.0 / 10.0 * i
	
	print(180.0/np.pi*guess, 180.0/np.pi * newton(guess, 0.001, 20, -10, 0.01))
