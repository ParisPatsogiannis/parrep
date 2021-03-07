
# coding: utf-8

# # Άσκηση 1

# In[1]:


import numpy as np
from numpy.random import choice

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (10, 6)  # default figure size


# In[2]:


np.random.seed(2017) 
def rand_walk_Z(start = 0, probs = (0.5, 0.5)):
    x = start
    steps = [-1, 1]  
    while True:  
        x += choice(steps, p=probs)
        yield x  


# In[3]:


fig, ax = plt.subplots()  

a, b = -70, 100
N = 500
escape_time = {'left' : np.zeros(N, dtype=int), 'right' : np.zeros(N, dtype=int) }


for col in ['red', 'blue']:
    for k in range(N):
        x = 0 
        if col == 'red': walker = rand_walk_Z(start=x, probs=(4 / 5, 1 / 5))  
        else: walker = rand_walk_Z(start = x, probs = (1 / 5, 4 / 5))
        
        chain = [x]
        t=0
        
        while a <= x <= b:
            x = next(walker)
            chain.append(x)
            t += 1
        if col == 'red' : escape_time['left'][k] = t
        else : escape_time['right'][k] = t    
            
        ax.plot(chain, color=col)

plt.axhspan(a, b, color = '#cccccc', alpha = 0.8)  # box between a & b
ax.grid() 
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Random walks-left (red) and right (blue)')
plt.show()


# In[4]:


plt.figure();
plt.hist(escape_time['left'], color='red', alpha = 0.8, bins=30, edgecolor='black', label='left', normed=True)
plt.hist(escape_time['right'], color='blue', alpha = 0.8, bins=30, edgecolor='black', label='right', normed=True)
plt.title('Histogram')
plt.xlabel('Time')
plt.ylabel('Density')
plt.show()


# Θέλουμε να βρούμε την πιθανότητα $P_z[Τ_Α<\infty]= Φ_Α(z)$ με $z\in [-70,100]$. Έστω ότι το $A=\{X_n(ω)\notin [-70,100]\}$
# Λύνοντας το πρόβλημα συνοριακών τιμών:
#                                  $$h(x)=ph(x+1)+(1-p)h(x-1), x\neq -71,101$$
#                                  $$h(-71)=h(101)=1$$
#  Η λύση του προβλήματος συνοριακών τιμών είναι η $h(x)=B+C(\frac{1-p}{p})^x$ οπότε για $p\neq 1/2$ βρίσκουμε τις σταθερές.
#  Επομένως βγαίνει ότι $h(x)=1$ αφού $B=1, C=0$ και άρα είμαστε σίγουροι ότι ο τυχαίος περίπατος θα βγει από το διάστημα.

# # Άσκηση 2

# In[5]:


def rand_walk_Z_pos(start = 0, probs = (0.5, 0.5)):
     
    x = start
    
    steps = [-1, 1]  
    while True:  
        if x > 0: x += choice(steps, p=probs)
        else: x += choice([0, 1], p = probs)
        yield x  


# In[6]:


sitx = 100 #situation 100
N = 1000 #φορές επανάληψης
M = 1000
maxright_pos = np.zeros(N, dtype=int);
max_pos = -1 * np.ones(N, dtype=int);


for k in range(N):
    x = 0
    walker = rand_walk_Z_pos(start=x, probs = (2/3, 1/3))
    
    for n in range(M):
        x = next(walker)
        max_pos[n] = max(max_pos[n], x)
        if t == sitx + 1 : maxright_pos[n] = x   


# In[7]:


plt.figure();
plt.hist(maxright_pos, color='red', alpha = 0.9, bins=30, edgecolor='black', label='left', normed=True)
plt.xlabel('Pos')
plt.ylabel('Density')
plt.title('X_{}'.format(sitx))
    
plt.figure()
plt.hist(max_pos, color='blue', alpha = 0.8, bins=30, edgecolor='black', label='left', normed=True)
plt.xlabel('Pos')
plt.ylabel('Density')
plt.title('Maximum position in the first {} steps. Average = {}, Variance = {}'.format(M, np.mean(max_pos), np.var(max_pos, ddof=0)))


# # Άσκηση 3

# In[8]:


def rand_walk_Z2(start=(0, 0), probs=(0.25, 0.25, 0.25, 0.25)):
    
    x, y = start
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while True:
        dx, dy = steps[choice(4, p=probs)]  # choice(4) = choose a number in [0,3]
        x, y = x + dx, y + dy 
        yield x, y
        


# In[18]:


R = np.arange(start=10, stop=50, step=10) #stop=50 διότι έκανε πολύ ώρα να τρέξει με stop=100
all_escape_times = np.zeros(len(R)) #We can use the len() to get the length of the given string, array, list, tuple, dictionary, etc. We can use len function to optimize the performance of the program. The number of elements stored in the object is never calculated, so len helps provide the number of elements

N = 500


# In[19]:


for j, r in enumerate(R): #The enumerate() method adds counter to an iterable and returns it (the enumerate object).
    r2 = r**2 
    escape_time = np.zeros(N, dtype=int) 
    for n in range(N):
        walker = rand_walk_Z2()
        x, y = (0, 0)
        t = 0
        while x**2 + y**2 < r2:
            x, y = next(walker)
            t += 1
        escape_time[n] = t
    all_escape_times[j] = np.mean(escape_time)


# In[22]:


plt.figure();
plt.loglog(R, all_escape_times);
ax.grid()
plt.xlabel('R (log)');
plt.ylabel('Escape Time (log)');

#Polyfit is a function that computes a least squares polynomial for a given set of data. Polyfit generates the coefficients of the polynomial, which can be used to model a curve to fit the data.
p, q = np.polyfit(np.log (R) , np.log(all_escape_times), 1)  
print('p = {}, q = {}'.format(p,q))


# Από το διάγραμμα φαίνεται οι 2 μεταβλητές να έχουνε γραμμική σχέση μεταξύ τους, δηλαδή οι χρόνοι εξόδου από τον δίσκο έχουν γραμμική σχέση με τις ακτίνες.Όσο αυξάνεται η ακτίνα τόσο μεγαλύτερος είναι ο χρόνος διαφυγής από τον δίσκο κάτι που φαίνεται λογικό.
