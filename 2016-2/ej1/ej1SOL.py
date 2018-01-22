import numpy as np
import matplotlib.pyplot as plt

'''
La siguiente función retorna el integrando de la función de Bessel J_m(x). Sus parámetros son m, x, y la variable de integración t.
'''
def bessel_integrand(m, x, t):
    return 1.0/np.pi * np.cos(m*t - x*np.sin(t))

'''
La siguiente función realiza la integral entre a y b de la función f para un número de pasos N utilizando la regla de Simpson. Los parámetros m y x son los correspondientes a J_m(x).
'''
def simpson(f, a, b, N, m, x):
    if N%2 == 1:
        N += 1
    h = (b-a)/N
    result = f(m,x,a) + f(m,x,b)
    for i in range(1, N, 2):
        result += 4*f(m,x,a + i*h)
    for i in range(2, N-1, 2):
        result += 2*f(m,x,a + i*h)
    result *= h/3.0
    return result

'''
Note que una integral corresponde a un punto de las gráficas que se quieren obtener. Entonces, la siguiente función realiza el procedimiento varias veces, generando arreglos para el eje X y el eje Y de las gráficas
'''
def plot_bessel(m):
    X = np.linspace(0,20,41)
    Y =np.zeros(41)
    for i in list(range(len(X))):
        Y[i]=simpson(bessel_integrand, 0.0, np.pi, 1000, m, X[i])
    
    plt.plot(X,Y)
    plt.xlabel("$x$", fontsize = "15")
    plt.ylabel("$J_m(x)$", fontsize = "15")
    plt.title("$m = $"+str(m), fontsize="15")
    plt.show()
    plt.close()

'''
Ahora sólo queda llamar esta función para cada m.
'''
plot_bessel(0)
plot_bessel(1)
plot_bessel(2)
