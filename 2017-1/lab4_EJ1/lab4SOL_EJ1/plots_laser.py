import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

datos = np.loadtxt('red3_filtrado.txt')

long_onda = datos[:,0]
amplitud = datos[:,1]

plt.plot(long_onda, amplitud)
plt.savefig('red3.png')
plt.close()

for i in range(len(amplitud)):
	if amplitud[i] == np.amax(amplitud):
		print('La longitud de onda de maxima amplitud es ' +str(long_onda[i])+ ' nm')

def gaussian_function(x, a, b, c):
    return a*np.exp(-(x-b)**2/c)

pars, covm = curve_fit(gaussian_function, long_onda, amplitud, [1,650,1])
amplitud_fit = gaussian_function(long_onda, pars[0], pars[1], pars[2])
plt.plot(long_onda, amplitud)
plt.plot(long_onda, amplitud_fit)
plt.savefig('red3_fit.png')
plt.close()

for i in range(len(amplitud_fit)):
	if amplitud_fit[i] == np.amax(amplitud_fit):
		print('La longitud de onda de maxima amplitud segun el ajuste es ' +str(long_onda[i])+ ' nm')





