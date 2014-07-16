import numpy
import pylab
import math

def likelihood(y_obs, y_model):
    chi_squared = sum((y_obs - y_model)**2)
    return (-chi_squared)
    
def my_model(x_obs, a, b, c):
    return a*(x_obs**2) + b*(x_obs) + c

data = numpy.loadtxt("movimiento.dat")
x_data = data[:,0]
y_data = data[:,1]

a_walk = numpy.empty((0))
b_walk = numpy.empty((0))
c_walk = numpy.empty((0))

a_walk = numpy.append(a_walk, numpy.random.random())
b_walk = numpy.append(b_walk, numpy.random.random())
c_walk = numpy.append(c_walk, numpy.random.random())

n_iterations = 100000

for i in range(n_iterations):

	a_prime = numpy.random.normal(a_walk[i], 0.1)
	b_prime = numpy.random.normal(b_walk[i], 0.1)
	c_prime = numpy.random.normal(c_walk[i], 0.1)

	y_init = my_model(x_data, a_walk[i], b_walk[i], c_walk[i])
	y_prime = my_model(x_data, a_prime, b_prime, c_prime)

	alpha = likelihood(y_data, y_prime)/likelihood(y_data, y_init)
    
	if(alpha<=1.0):
    
		a_walk = numpy.append(a_walk,a_prime)
		b_walk = numpy.append(b_walk,b_prime)
		c_walk = numpy.append(c_walk,c_prime)
        
	else:
    
		beta = numpy.random.random()
        
		if(beta<=math.exp(-alpha)):
        
			a_walk = numpy.append(a_walk,a_prime)
			b_walk = numpy.append(b_walk,b_prime)
			c_walk = numpy.append(c_walk,c_prime)

		else:
        
			a_walk = numpy.append(a_walk,a_walk[i])
			b_walk = numpy.append(b_walk,b_walk[i])
			c_walk = numpy.append(c_walk,c_walk[i])

best_y = my_model(x_data, numpy.average(a_walk), numpy.average(b_walk), numpy.average(c_walk))
pylab.scatter(x_data,y_data)
pylab.plot(x_data, best_y)	
pylab.show()
