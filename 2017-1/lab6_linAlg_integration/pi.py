import numpy as np
from numpy import linalg as lng


n=100000
N0=0
a=(np.random.rand(n,2)*2)-1
for i in range(n):
    if (lng.norm(a[i,:])<1):
        N0+=1
        
#print(N0)

pi=(4*N0)/n

#print(pi)
        
###########################################################    
    
def function(x):
    y=np.exp(-x)
    return y

def exact(x):
    return -np.exp(-x)

def montecarlo(f, a, b, n):    
    x = np.random.random(n)
    f_eval = f(x)
    result = f_eval.mean()
    return result

result=montecarlo(function,0,1,10000)
exact_result=exact(1)-exact(0)
print(result,exact_result)