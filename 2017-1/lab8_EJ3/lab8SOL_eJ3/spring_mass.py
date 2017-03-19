import numpy as np
import matplotlib.pyplot as plt

N = 5000 #number of steps to take
xo = 0.2 #initial position in m
vo = 0.0 #initial velocity
tau = 4.0 #total time for the simulation in s .
dt = tau/float(N) # time step
k = 42.0 #spring constant in N/m
m = 0.25 #mass in kg
g = 9.8 #in m/ s ^2
mu = 0.15 #friction coefficient

y = np.zeros([N,2])

#y is the vector of positions and velocities.

y[0,0] = xo #initial position
y[0,1] = vo #initial velocity


#This function defines the derivatives of the system.
def SpringMass(state,time) :

    g0=state[1]
    if g0 > 0 :
        g1=-k/m*state[0]-g*mu
    else:
        g1=-k/m*state[0]+g*mu
    
    return np.array([g0,g1])

#This is the basic step in the Euler Method for solving ODEs.
def euler (y,time,dt,derivs) :  
    
    k0 = dt*derivs(y,time)
    ynext = y + k0
    
    return ynext    


for j in range (N-1):

    y[j+1] = euler(y[j],0,dt,SpringMass)

#Just to plot  
time = np.linspace(0,tau,N)
plt.plot(time, y[:,0],'b',label="position")
plt.xlabel( "time" )
plt.ylabel( "position" )
plt.savefig('spring_mass.png')