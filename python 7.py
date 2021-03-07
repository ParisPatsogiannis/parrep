
# coding: utf-8

# # Παραδοτέο 1

# In[1]:


import numpy as np


def random_walk_next(state):
    if np.random.uniform() < 0.5:
        return 0
    return state + 1

def ergodic_sum(N = 10**4):
    running_state = 0
    sum_result = 0

    for i in range(N):
        running_state = random_walk_next(running_state)
        sum_result += running_state

    return sum_result / N 

    
### Ergodic Limit Theorem
z = ergodic_sum()
print("The simulated ergodic average [X1+X2+X3+...+XN]/N is: %.4f" % z)


# In[2]:


import numpy as np


def random_walk_next(state):
    if np.random.uniform() < 0.5:
        return 0
    return state + 1

def ergodic_sum(N = 50):
    running_state = 0
    sum_result = 0

    for i in range(N):
        running_state = random_walk_next(running_state)
        sum_result += running_state

    return sum_result / N 

    
### Ergodic Limit Theorem
z = ergodic_sum()
print("The simulated ergodic average [X1+X2+X3+...+XN]/N is: %.4f" % z)


# In[3]:



inf_sum  = lambda N = 1000 : sum([k / 2**(k+1) for k in range(N)])
S = inf_sum()
print('The sum using 1000 terms is {}'.format(S))
r = abs(z - S) / S
print('Relative error is {}'.format(r))


sums = np.array([ergodic_sum() for i in range(100)])
print('Variance of sums is ', np.var(sums, ddof = 1))


sums = np.array([ergodic_sum(N = 2 * 10**4) for i in range(100)])
print('Variance of sums is ', np.var(sums, ddof = 1))


def ergodic_sum_2(N = 10**4):
    running_state = 0
    sum_result = 0

    for i in range(N):
        running_state = random_walk_next(running_state)
        sum_result += np.cos(running_state + np.cos(running_state)) * 2 

    return sum_result / N 

S2 = ergodic_sum_2()
print('Sum of Σ cos(k + cos(k)) / 2^k) = ', S2)


# # Παραδοτέο 2

# In[4]:


import numpy as np
import random as r
from math import gamma, pi 

def Vol1(d):
    x = d/2
    return pi ** x / gamma(x + 1)


def mcmc_volume(dmax = 10, N = 100, delta = 1.0):
    samples = 1000 
    D = {}
    D[1] = 2 
    for d in range(1, dmax + 1):
        pts = []
        for _ in range(samples):
            x = np.zeros(d)  
            R_sq = 0.0  

            for _ in range(N):
                k = r.choice(range(d))  
                z = r.uniform(-delta,delta) 
                x_prop_k = x[k] + z   
                R_sqprop = R_sq - x[k]**2+ x_prop_k**2 
                if R_sqprop < 1.0: 
                    R_sq = R_sqprop
                    x[k]= x_prop_k   
                    pts.append(x)
                    
                    
        Npoints = len(pts)
        Nhits = 0
        # cylinder
        for p in pts:   
            xc = r.uniform(-delta, delta)
            R_sq = xc**2 + sum([g**2 for g in p])
            y = (x, )
            
            if R_sq <= 1: 
                Nhits += 1
        ratio = Nhits / Npoints 
       
        D[d + 1] = D[d] * ratio * 2
        
    return D

def mcmc_volume_ergodic_mean(dmax = 10, N = 100, delta = 1.0):
    D = {}
    Z = 0
    N = 100
    samples = 1000 
    D[1] = 2 
    for d in range(1, dmax+1):  
        Nhits = 0
        all = []
        R_sq = 0.0  
        x = np.zeros(d)
        l = 0 
        for _ in range(N * samples):
            k = r.choice(range(d)) if d > 1 else 0 
            z = r.uniform(-delta,delta) 
            x_prop_k = x[k] + z   
            R_sqprop = R_sq - x[k]**2+ x_prop_k**2 
            if R_sqprop < 1.0: 
                    R_sq = R_sqprop
                    x[k]= x_prop_k   
            xc = r.uniform(-delta, delta)
            R_sqcl = R_sq + xc**2 
            if(R_sqcl < 1):
                Nhits += 1
        ratio = Nhits / (N * samples) 
        D[d + 1] = D[d] * ratio * 2
    return D


# In[6]:


D1 = mcmc_volume(100)
D2 = mcmc_volume_ergodic_mean(100)

print('Volume with Ergodic Theorem\n') 
for d in D2.keys():
    Vactual = Vol1(d)
    rel = abs(Vactual - D2[d]) / Vactual
    print('MCMC Estimate for d = {} : {}, Actual = {}, Relative Error = {}'.format(d, D2[d], Vactual,  rel))

print('Volume with Monte Carlo\n')
for d in D1.keys():
    Vactual = Vol1(d)
    rel = abs(Vactual - D1[d]) / Vactual 
    print('MCMC Estimate for d = {} : {}, Actual = {}, Relative Error = {}'.format(d, D1[d], Vactual, rel))


# ΟΝΟΜΑΤΕΠΩΝΥΜΟ:ΠΑΤΣΟΓΙΑΝΝΗΣ ΠΑΡΑΣΚΕΥΑΣ
# 
# ΑΡ.ΜΗΤΡΩΟΥ:GE15138
# 
# ΣΧΟΛΗ:ΕΜΦΕ
