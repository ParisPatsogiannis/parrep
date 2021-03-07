
# coding: utf-8

# # ΑΣΚΗΣΗ 1

# In[1]:


from numpy import random

def vol(N,d):
    nhits = 0
    for i in range(N):
        x = random.uniform(-1,1,d)
        if sum(x ** 2) < 1: 
            nhits += 1
    return 2 ** d * nhits / N

d = 3
N = 10_000       
print ("The Monte Carlo estimate of ω(", d,") is  : %.5f " % vol (N,d))


# In[2]:


from math import gamma, pi 

def Vol1(d):
    x = d/2
    return pi ** x / gamma(x + 1)

print("The actual value of ω(", d,") is  : %.5f " % Vol1(d))


# In[3]:


N = 10e6

def print_volumes(N = 1000000):
    d = 2
    mc = []
    actual_pr = []
    error = []
    z = [] #z=p(d)
    while 1 == 1:
        v1 = vol(N, d)
        if v1 == 0: break
        v2 = Vol1(d)
        mc.append(v1)
        actual_pr.append(v2)
        print(d)
        print ("The Monte Carlo estimate of ω(", d,") is  : %.5f " % v1)
        print("The actual price of ω(", d,") is  : %.5f " % v2)
        e = abs(v2 - v1) / v2
        print('Relative error is {}'.format(e))
        error.append(e)
        z.append(v1 / 2**d)
        d += 1
    return mc, actual_pr, error, z    
        
mc, actual_pr, error, z = print_volumes()        


# In[5]:


from matplotlib import pyplot as plt


plt.semilogy(range(2, len(z) + 2), z) #make a plot with log scaling on the y axis
plt.title('diagram of d-log(p(d))')


# Tο σχετικό σφάλμα της εκτίμησης στο (α) είναι μεγάλο καθώς η διάσταση αυξάνει, δηλαδή ο όγκος της σφαίρας γίνεται όλο και μικρότερος σε σχέση με τον όγκο του κύβου επομένως όλο και λιγότερα σημεία θα πέφτουν στην σφαίρα

# In[6]:


import numpy as np

print('N is equal to {}'.format(np.ceil( 1000 / (Vol1(20) / 2**20 ) )) )


# Έστω ότι οι πράξεις που κάνει ένας υπολογιστής το δευτερόλεπτο είναι της τάξης του $10^5$ τότε ο συνολικός χρόνος που θα χρειαζόταν ο υπολογιστής θα ήταν περίπου 11  με 12 ώρες.

# # ΑΣΚΗΣΗ 2

# In[7]:


import random as r

def mcmc2d(samples = 1000, delta = 1.0, N = 100):
    point_x = []
    point_y = []

    for _ in range(samples):
        x = [0,0]  ## start at the centre of th disc. This variable will keep the position of the chain
        R_sq = 0.0  ## this variable keeps the squared distance from 0. It saves some computations to keep it

        for _ in range(N):
            k = r.choice([0,1])  ## choose a jump direction at random
            z = r.uniform(-delta,delta) ## choose a jump size uniformly in (-delta,delta)
            x_prop_k = x[k] + z   ## propose a jump by z in the direction k
            R_sqprop = R_sq - x[k]**2+ x_prop_k**2 ## compute the squared distance from 0 after the proposed jump 
            if R_sqprop < 1.0: 
                R_sq = R_sqprop
                x[k]= x_prop_k   ## if the proposed jump leads to a point in the disc, then jump

        point_x.append(x[0])
        point_y.append(x[1])
    return point_x, point_y


# In[8]:


plt.figure();
plt.scatter( *mcmc2d(samples = 1000, delta = 1.00));
plt.figure();
plt.scatter( *mcmc2d(samples = 1000, delta = 0.01) )
plt.figure();
plt.scatter( *mcmc2d(samples = 1000, delta = 20) );


# In[9]:


def mcmc_volume(dmax = 10, N = 100, delta = 1.0):
    samples = 1000 
    D = {}
    D[1] = 2 
    for d in range(1, dmax + 1):
        points = []
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
                    points.append(x)
        Npoints = len(points)
        Nhits = 0
        # cylinder
        for p in points:   
            xc = r.uniform(-delta, delta)
            R_sq = xc**2 + sum([g**2 for g in p])
            if R_sq <= 1: # p and xc are in D_{d+1}
                Nhits += 1
        ratio = Nhits / Npoints 
        
        D[d + 1] = D[d] * ratio * 2
        
    return D

D = mcmc_volume(100)
print(D)   


# In[10]:


error = {}
for d in D.keys():
    Vactual = Vol1(d)
    r = abs(Vactual - D[d]) / Vactual
    print('MCMC Estimate for d = {} : {}, Actual = {}, (Abs) Relative Error = {}'.format(d, D[d], Vactual,  r))
    error[d] = r


# In[11]:


plt.semilogy(error.keys(), error.values());    
plt.title('Relative error');
plt.xlabel('');


# ΟΝΟΜΑΤΕΠΩΝΥΜΟ:ΠΑΤΣΟΓΙΑΝΝΗΣ ΠΑΡΑΣΚΕΥΑΣ
# 
# ΣΧΟΛΗ:ΕΜΦΕ
# 
# 
