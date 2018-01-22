import matplotlib.pyplot as plt
import numpy as np

X = np.loadtxt('datos.dat')
x_obs = X[:,0]
y_obs = X[:,1]

plt.scatter(x_obs, y_obs)
plt.show()
plt.close()

def likelihood(y_obs, y_model):
	chi_squared = 1.0/2.0 * sum((y_obs - y_model)**2)
	#return np.exp(-chi_squared)
	return chi_squared

def my_model(x_obs, a, b, c):
	return a*x_obs**2 + b*x_obs + c

a_walk = np.empty(0)
b_walk = np.empty(0)
c_walk = np.empty(0)
l_walk = np.empty(0)

a_walk = np.append(a_walk, np.random.random())
b_walk = np.append(b_walk, np.random.random())
c_walk = np.append(c_walk, np.random.random())

y_init = my_model(x_obs, a_walk[0], b_walk[0], c_walk[0])
l_walk = np.append(l_walk, likelihood(y_obs, y_init))

n_iterations = 20000
for i in range(n_iterations):
	a_prime = np.random.normal(a_walk[i], 0.2)
	b_prime = np.random.normal(b_walk[i], 0.2)
	c_prime = np.random.normal(c_walk[i], 0.2)

	y_init = my_model(x_obs, a_walk[i], b_walk[i], c_walk[i])
	y_prime = my_model(x_obs, a_prime, b_prime, c_prime)

	l_prime = likelihood(y_obs, y_prime)
	l_init = likelihood(y_obs, y_init)

	alpha = np.exp(-(l_prime - l_init))
	if(alpha >= 1.0):
		a_walk = np.append(a_walk, a_prime)
		b_walk = np.append(b_walk, b_prime)
		c_walk = np.append(c_walk, c_prime)
		l_walk = np.append(l_walk, l_prime)

	else:
		beta =  np.random.random()
		if(beta <= alpha):
			a_walk = np.append(a_walk, a_prime)
			b_walk = np.append(b_walk, b_prime)
			c_walk = np.append(c_walk, c_prime)
			l_walk = np.append(l_walk, l_prime)
		else:
			a_walk = np.append(a_walk, a_walk[i])
			b_walk = np.append(b_walk, b_walk[i])
			c_walk = np.append(c_walk, c_walk[i])
			l_walk = np.append(l_walk, l_init)

max_likelihood_index = np.argmax(l_walk[int(n_iterations/2.0):])
best_a = a_walk[max_likelihood_index]
best_b = b_walk[max_likelihood_index]
best_c = c_walk[max_likelihood_index]

print(best_a, best_b, best_c)
y_best = my_model(x_obs, best_a, best_b, best_c)

# plt.scatter(x_obs, y_obs)
# plt.plot(x_obs, y_best)
# plt.show()
# plt.close()

# plt.plot(l_walk)
# plt.show()
# plt.close()

# #Shows histograms
# hist_data_a = plt.hist(a_walk, bins = 30)
# plt.show()
# plt.close()
# hist_data_b = plt.hist(b_walk, bins = 30)
# plt.show()
# plt.close()
# hist_data_c = plt.hist(c_walk, bins = 30)
# plt.show()
# plt.close()

