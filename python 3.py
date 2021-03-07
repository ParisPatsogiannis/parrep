
# coding: utf-8

# # AΣΚΗΣΗ 1

# In[1]:


import random
random.seed(2018)
from simple_markov_chain_lib import markov_chain
import numpy as np  # numerical computations library. We will call it np in our code
import matplotlib.pyplot as plt  # library for plotting. We will call it plt in our code

# to plot the results in the notebook:
get_ipython().run_line_magic('matplotlib', 'inline')


start,end,step=0.02,0.98,0.02
x=np.arange(start,end,step)
y= []

for p in x:
    init_probs = {'0-0' : 1.0}
    markov_table = {
        '0-0' : {'15-0' : p, '0-15' : 1 - p},
        '15-0' : {'30-0': p, '15-15' : 1 - p},
        '0-15' : {'15-15': p, '0-30' : 1 - p},
        '30-0' : {'40-0' : p, '30-15' : 1 - p},
        '15-15' : {'30-15' : p, '15-30' : 1 - p},
        '0-30' : {'15-30' : p, '0-40' : 1 - p},
        '40-0' : {'GameA' : p, '40-15' : 1 - p},
        '30-15' : {'40-15' : p, 'Deuce' : 1 - p},
        '15-30' : {'Deuce' : p, '15-40' : 1 - p},
        '0-40' : {'15-40' : p, 'GameB': 1 - p},
        '40-15' : { 'GameA' : p, 'AdvA' : 1 - p},
        '15-40' : {'GameB' : 1 - p, 'AdvB' : p},
        'GameA' : {'GameA' : 1.0},
        'GameB' : {'GameB' : 1.0},
        'AdvA' : {'GameA' : p, 'Deuce' : 1 - p},
        'AdvB' : {'GameB' : 1 - p, 'Deuce' : p},
        'Deuce' : {'AdvA' : p, 'AdvB': 1 - p}
    }

    mc=markov_chain(markov_table,init_probs)

    counter = 0
    N = 2000
    for i in range(N):
        mc.start()
        while mc.running_state != 'GameA' and mc.running_state != 'GameB':
            mc.move()
        if mc.running_state == 'GameA': counter += 1
    y.append(counter/N)
    


# Let's plot (x,y)
plt.figure()
plt.plot(x,y)
# Specify some extra attributes
plt.xlabel('p')
plt.ylabel('F(p)')
plt.title('This is my first tennis game plot')


# Παρατηρούμε απο το διάγραμμα,όπου ο x άξονας δίνει τις τιμές του p και ο άξονας y δίνει τις τιμές του  F(p) ότι στο διάστημα  (0.0,0.2)  η συνάρτηση δεν εμφανίζει μεγάλες μεταβολές, αφού όπως βλέπουμε η τιμή της συνάρτησης μου ειναι σχεδον 0, δηλαδη  F(p)≃0  ενω στο διάστημα  (0.8,1.0)  έχουμε και πάλι μικρές μεταβολές και βλέπουμε ότι η συνάρτηση είναι σχεδόν 1 δηλαδη  F(p)≃1. Αντιθέτως,για το διαστημα  (0.2,0.8)  έχουμε μεγάλες μεταβολές στην συνάρτηση μας όπως φαίνεται απο το διάγραμμα μας! Στο διάστημα (0.2,0.8) λοιπόν η πιθανότητα νίκης του Α αυξάνονται απότομα ενώ στα διαστήματα (0.0,0.2) και (0.8,1.0) η πιθανότητα νίκης του Α είναι σχεδόν σταθερή.

# # ΑΣΚΗΣΗ 2

# In[3]:


from simple_markov_chain_lib import markov_chain

markov_table = {
    0: {1: .5, 2: .5}, # from state 0 we move to state 1 with prob 0.5 and to state 2 with 0.5
    1: {0: 1/3, 3: 2/3},
    2: {2: 1.},
    3: {0: .5, 3: .25, 4: .25},
    4: {4: 1.}
}

init_dist = {0: 1.}  # we start from state 0 with probability 1

mc = markov_chain(markov_table, init_dist)

import statistics as stat
import numpy as np 
import matplotlib.pyplot as plt
estimates = []
Var = []


get_ipython().run_line_magic('matplotlib', 'inline')
M=30
x = []

for z in range(5,12):
    sample_size = 2 ** z # Ν
    x.append(sample_size)
    
    for j in range(M):
        running_total = 0

        for i in range(sample_size):
            mc.start()
            while mc.running_state != 2 and mc.running_state != 4:
                mc.move()
            running_total += mc.steps # steps it took to be absorbed


        estimates.append(running_total / sample_size)
    Var.append(stat.variance(estimates))
               
               
plt.figure(figsize=(12, 7)) 
# Right Axes
plt.subplot(1, 2, 1)
plt.plot(x,Var)
plt.xlabel('N')
plt.ylabel('Var(En)')
plt.title('Linear Axis')
plt.grid(True) 

# Left Axes
plt.subplot(1, 2, 2) 
plt.loglog(x, Var, basex=2, basey=2)
plt.xlabel('N')
plt.ylabel('Var(En)')
plt.title('Log-log Axis')
plt.grid(True)

plt.subplots_adjust(wspace = 0.5)

print(np.polyfit(np.log2(x),np.log2(Var),1))


# Στην πρώτη γραφική παράσταση οπου απεικονίζεται η διασπορά  Var(En)  συναρτήσει του  N  βλέπουμε ότι είναι της μορφής Var=αN^n.Aφού στο δεύτερο διάγραμμα έχουμε την διασπορά με τη βοήθεια του log,και τα Ν μου ειναι ολα της μορφής  2^n ,θα λογαριθμήσουμε με τη βοήθεια του λογάριθμου με βάση το 2!. Λογαριθμίζοντας λοιπόν την  Var=αN^n  θα πάρουμε την σχέση  log2(Var)=nlog2(N)+log2(a) η οποία είναι γραμμική μιας και είναι της μορφής  y=Ax+B  Αντικαθιστώντας, το  N=2^κ  στην  log2(Var)=nlog2(N)+log2(a)  παίρνουμε:  log2(Var)=nk+log2(a)

# ΟΝΟΜΑΤΕΠΩΝΥΜΟ:ΠΑΡΗΣ ΠΑΤΣΟΓΙΑΝΝΗΣ 
# 
# ΣΧΟΛΗ:ΕΜΦΕ 
# 
# ΑΡ.ΜΗΤΡΩΟΥ:ge15138
