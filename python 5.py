
# coding: utf-8

# # ΆΣΚΗΣΗ 1

# # Ερώτημα 1
# 
# 

# Η μαρκοβιανή ιδιότητα είναι το μαθηματικό αποτέλεσμα που μας εξασφαλίζει ότι η προσέγγισή μας είναι σωστή.
# Με άλλα λόγια ισχύει ότι:
# $$P[X_n=x_n|X_{n-1}=x_{n-1},...,X_0=x_0]=P[X_n=x_n|X_{n-1}=x_{n-1}]$$
# 
# Συνεπώς μπορούμε να ξεκινήσουμε από οποιοδήποτε σημείο της αλυσίδας χωρίς να χρειάζεται να ξεκινάμε πάλι από την αρχή.
# 

# # Ερώτημα 2

# Για τον υπολογισμό της κατανομής $π_1$ έχουμε:
# $$π_1(1)=\frac{1}{E[T_1^+]}$$
# 
# επομένως $$π_1(y)=\frac{E_x[\sum 1[X_k=y]}{E[T_1^+]},  y=2,3,4$$
# 
# Θεωρητικά την αναλλοίωτη κατανομή της αλυσίδας:
# $$π_x=π_xP, \sum_{x} π_x(x) $$
# 
# Λύνοντας το σύστημα παίρνουμε τις εξής λύσεις:
# $$π_x=(\frac{18}{97},\frac{9}{97},\frac{45}{97},\frac{25}{97})$$
# 
# Τα δύο αποτελέσματα συμφωνούν και αυτό περιμέναμε, καθώς η  $x=1$  είναι γνησίως επαναληπτική και η  $C_1=(1,2,3,4)$ αποτελεί μη-υποβιβάσιμη κλειστή κλάση.
# 

# # Ερώτημα 3

# In[1]:


from simple_markov_chain_lib import markov_chain

markov_table = {
    1: {2: 0.5, 3: 0.5},
    2: {1: 1/3, 4: 2/3},
    3: {3: 0.8, 4: 0.2},
    4: {1: 0.6, 4: 0.4}
}

def invariant(x0 = 1, N = 100000):
    print('Calculation for initial state x0={}'.format(x0))
    init_dist = {x0 : 1.0}
    for i in range(3):
        print('\nSimulation Number : {}'.format(i + 1))
        mc = markov_chain(markov_table, init_dist)

        visits = {state: 0 for state in (1, 2, 3, 4)} 

        mc.start()
        completed = 0

        sum_times = 0
        t = 0
        while completed < N:
            visits[mc.running_state] += 1
            mc.move()
            if mc.running_state == x0:
                sum_times += t
                t = 1
                completed +=1
            else: t += 1    
        Z = sum_times / completed        
        print('Z = {}'.format(Z))
        invariant = {}        

        print("Expected Visits starting from 1:")
        for x, y in visits.items():
            invariant[x] = 1 / Z if x == x0 else (y / N) / Z
            print('State = {} : p = {}'.format(x, invariant[x]))
        print('Sum of all probs = {}'.format(sum(invariant.values())))
        
invariant()


# Στη λύση του ερωτήματος 2, έχουμε δημιουργήσει και χρησιμοποιήσει τον παραπάνω κώδικα που ακολουθεί την συνάρτηση Python invariant (αναλλοίωτη) που υπολογίζει την αναλλοίωτη για την αρχική κατάσταση $x_0$ με N διαδρομές. Για τις υπόλοιπες αρχικές καταστάσεις $2,3,4$ βρόγχου:
# 
# for i in [1,2,3,4]:
# 
# invariant_calculation(i)

# # ΆΣΚΗΣΗ 2

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

N = 10e6  
Ntrials, Nhits = 0, 0
a_x, a_y = [], [] 
r_x, r_y = [], [] 

while Nhits < N:
    Ntrials += 1
    x, y, z = np.random.uniform(-1, 1, 3)
    if x**2 + y**2 + z**2< 1:
        a_x.append(x)
        a_y.append(y)
        Nhits += 1
    else:
        r_x.append(x)
        r_y.append(y)

print("Samples drawn %d" % Ntrials)
print("Samples in the disk %d" % N)
V3 = 4 * np.pi / 3;
V3_est = 8 *   (Nhits / Ntrials)
err = abs(V3_est - V3)
print('Theoretical value of V(3)=' + str(V3) )
print('Experimental value of V(3)=' + str(V3_est))
print('Error = {}'.format(err))
print('Rel. = {}'.format(err / V3))


# Έχουμε:
# $$V_{avg}(3)=\frac{8N_h}{N}$$
# $$ΔV=|V_{avg}(3)-V(3)|$$
# $$σ_V=\frac{ΔV}{V(3)}$$
# 
# Όπως βλέπουμε η θεωρητική τιμή του V(3) είναι περίπου ίση με την πρακτική τιμή V(3) δηλαδή ισχύει ότι:
# $$V_{theor}=V_{pract}\approx 4,18$$

# # Eρώτημα 2

# In[2]:


N=100000
Ntrials, Nhits = 0, 0
a_x, a_y = [], []  
b_x, b_y = [], []  

while Nhits < N:
    Ntrials += 1
    x, y = np.random.uniform(-1, 1, 2)
    if ( x**2 + y**2 ) **2 <= 2 * abs(x * y):
        a_x.append(x)
        a_y.append(y)
        Nhits += 1
    else:
        b_x.append(x)
        b_y.append(y)

ratio = Nhits / Ntrials
print('Total ratio: ' + str(ratio))

print("Samples drawn %d" % Ntrials)
print("Samples in the disk %d" % N)

fig, ax = plt.subplots()

plt.scatter(a_x, a_y, color = 'black', s = 1) # parameter s determines the size of each dot in the scatter plot
plt.scatter(b_x, b_y, color = 'green', s = 1)

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_aspect('equal')  

plt.show()
L = 4 * ratio
print('Lake area = multiplying the ratio Nhits / Ntrials by 4 -------> |L|={}'.format(L))


# # Ερώτημα 3

# In[4]:


s = 0
for x, y in zip(a_x, a_y):
    s += abs(x + y)
s /= Nhits
I = L * s
print('f(x,y) = |x + y|-----> L, is {}'.format(I) )


# ΟΝΟΜΑΤΕΠΩΝΥΜΟ:ΠΑΡΑΣΚΕΥΑΣ ΠΑΤΣΟΓΙΑΝΝΗΣ
# 
# 
# ΑΡ.ΜΗΤΡΩΟΥ:GE15138
# 
# 
# ΣΧΟΛΗ:ΕΜΦΕ
# 
