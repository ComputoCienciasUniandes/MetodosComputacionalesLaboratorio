import numpy as np
import matplotlib.pyplot as plt

r = 28.0
s = 10.0
b = 8.0/3.0

def x_prime(t, x, y, z):
	return s*(y-x)
def y_prime(t, x, y, z):
	return x*(r - z) - y
def z_prime(t, x, y, z):
	return x*y -b*z

def rk2_step(t_old, x_old, y_old, z_old, h):

	kx_half = x_prime(t_old, x_old, y_old, z_old)
	ky_half = y_prime(t_old, x_old, y_old, z_old)
	kz_half = z_prime(t_old, x_old, y_old, z_old)

	t_half = t_old + h/2.0
	x_half = x_old + h/2.0 * kx_half
	y_half = y_old + h/2.0 * ky_half
	z_half = z_old + h/2.0 * kz_half

	kx = x_prime(t_half, x_half, y_half, z_half)
	ky = y_prime(t_half, x_half, y_half, z_half)
	kz = z_prime(t_half, x_half, y_half, z_half)
	
	t_new = t_old + h
	x_new = x_old + h * kx
	y_new = y_old + h * ky
	z_new = z_old + h * kz
	
	return t_new, x_new, y_new, z_new

def rk2(x0, y0, z0, t_total, h):

	n_points = int(t_total/h)

	T = np.zeros(n_points)
	X = np.zeros(n_points)
	Y = np.zeros(n_points)
	Z = np.zeros(n_points)

	T[0] = 0.0
	X[0] = x0
	Y[0] = y0
	Z[0] = z0
	
	for i in range(1, n_points):
		T[i], X[i], Y[i], Z[i] = rk2_step(T[i-1], X[i-1], Y[i-1], Z[i-1], h)

	f, ax = plt.subplots(1,3,figsize=(30,10))
	ax[0].set_title("x vs. y")
	ax[0].plot(X,Y)

	ax[1].set_title("x vs. z")
	ax[1].plot(X,Z)
	
	ax[2].set_title("y vs. z")
	ax[2].plot(Y,Z)

	plt.savefig("lorenz.png")
	plt.show()
	plt.close()
	
h = 0.001
t_total = 40.0
x0 = 2.0
y0 = 3.0
z0 = 4.0
rk2(x0, y0, z0, t_total, h)
		
		


	

	
	

