
# coding: utf-8

# # ΑΣΚΗΣΕΙΣ 35-37

# In[3]:


import statistics as stat
import random 
estimates=[]
random.seed(2018) #for reproducibility
from simple_markov_chain_lib import markov_chain

p = 1/6

# A dictionary for the initial distibution. 
# We prescribe the initial distribution
init_probs = {1: 1.0} 
 
# A dictionary for the transition probability matrix. 
# Every state-key correspond to a list with tuples of (Next_State,Probability)    
markov_table = {
    1: {2: 1.},
    2: {2: 2/3, 3: 1/3},
    3: {1: p, 2: 1-p}
}
 
mc = markov_chain(markov_table, init_probs)

#Experiment parameters
M = 50
N = 200 # number of samples
steps = 20 # the target time

for k in range(M):
    counter=0
    for i in range(N):
        mc.start() 
        for j in range(steps):  mc.move()
        if mc.running_state == 1:  counter += 1
    estimates.append(counter / N)
    
print(
    """ 
    The sample mean is {0:.5f} and the sample variance is {1:.5f}
    """.format(stat.mean(estimates), stat.variance(estimates))
)


# In[4]:


import statistics as stat
import random 
estimates=[]
random.seed(2018)
from simple_markov_chain_lib import markov_chain

p = 1/6

init_probs = {1: 1.0} 
 
markov_table = {
    1: {2: 1.},
    2: {2: 2/3, 3: 1/3},
    3: {1: p, 2: 1-p}
}
 
mc = markov_chain(markov_table, init_probs)
M = 50
N = 20000
steps = 20 
for k in range(M):
    counter = 0
    for i in range(N):
        mc.start() 
        for j in range(steps):  mc.move()
        if mc.running_state == 1:  counter += 1
    estimates.append(counter / N)
    
print(
    """ 
    The sample mean is {0:.5f} and the sample variance is {1:.5f}
    """.format(stat.mean(estimates), stat.variance(estimates))
)


# In[5]:


import statistics as stat
import random 
estimates=[]
random.seed(2018) #for reproducibility
from simple_markov_chain_lib import markov_chain

p = 1/6

# A dictionary for the initial distibution. 
# We prescribe the initial distribution
init_probs = {1: 1.0} 
 
# A dictionary for the transition probability matrix. 
# Every state-key correspond to a list with tuples of (Next_State,Probability)    
markov_table = {
    1: {2: 1.},
    2: {2: 2/3, 3: 1/3},
    3: {1: p, 2: 1-p}
}
 
mc = markov_chain(markov_table, init_probs)

#Experiment parameters
M = 50
N = 200 # number of samples
steps = 20 # the target time
for k in range(M):
    counter = 0
    for i in range(N):
        mc.start() 
        for j in range(steps):  mc.move()
        if mc.running_state == 3:  counter += 1
    estimates.append(counter / N)
    
print(
    """ 
    The sample mean is {0:.5f} and the sample variance is {1:.5f}
    """.format(stat.mean(estimates), stat.variance(estimates))
)


# ΑΠΑΝΤΗΣΕΙΣ ΣΤΙΣ ΕΡΩΤΗΣΕΙΣ ΤΗΣ ΕΡΓΑΣΤΗΡΙΑΚΗΣ ΑΣΚΗΣΗΣ 1: 
# 1)TA AΠΟΤΕΛΕΣΜΑΤΑ ΓΙΑ ΤΙΣ 2 ΠΕΡΙΠΤΩΣΕΙΣ ΠΑΡΑΤΙΘΕΝΤΑΙ ΑΠΟ ΠΑΝΩ (ΕΧΟΥΜΕ ΤΡΕΞΕΙ ΤΟΝ ΚΩΔΙΚΑ ΚΑΙ ΓΙΑ ΤΙΣ 2 ΠΕΡΙΠΤΩΣΕΙΣ ΣΤΑ ΚΕΛΙΑ 1,2) 2)Η θΕΩΡΗΤΙΚΗ ΜΟΥ ΤΙΜΗ ΟΠΩΣ ΒΛΕΠΟΥΜΕ ΚΑΙ ΑΠΟ ΤΟΥΣ ΠΑΡΑΠΑΝΩ ΚΩΔΙΚΕΣ ΕΙΝΑΙ ΠΟΛΥ ΚΟΝΤΑ ΣΤΙΣ ΤΙΜΕΣ ΠΟΥ ΒΡΗΚΑΜΕ ΓΙΑ Ν=200 ΚΑΙ Ν=20000 ΚΑΙ ΜΑΛΙΣΤΑ ΒΡΙΣΚΕΤΑΙ ΠΙΟ ΚΟΝΤΑ ΣΕ ΑΥΤΗ ΓΙΑ Ν=20000. 
# 3)ΣΤΗΝ ΠΡΩΤΗ ΠΕΡΙΠΤΩΣΗ ΔΗΛΑΔΗ ΓΙΑ Ν=200 Η ΔΕΙΓΜΑΤΙΚΗ ΔΙΑΣΠΟΡΑ ΕΙΝΑΙ:S_1=0.00012.ΣΤΗΝ ΔΕΥΤΕΡΗ ΠΕΡΙΠΤΩΣΗ ΔΗΛΑΔΗ ΓΙΑ Ν=20000 Η ΔΕΙΓΜΑΤΙΚΗ ΔΙΑΣΠΟΡΑ ΕΙΝΑΙ:S_2= 0.00000
# 4)ΑΝ Η ΑΛΥΣΙΔΑ ΞΕΚΙΝΑΕΙ ΑΠΟ ΤΗΝ ΚΑΤΑΣΤΑΣΗ 3 ΑΛΛΑΖΟΝΤΑΣ ΤΗΝ ΑΡΧΙΚΗ ΠΙΘΑΝΟΤΗΤΑ ΩΣΤΕ ΝΑ ΞΕΚΙΝΑΕΙ ΑΠΟ ΤΗΝ ΚΑΤΑΣΤΑΣΗ 3 ΒΡΙΣΚΟΥΜΕ ΟΤΙ X(ΔΕΙΓΜΑΤΙΚΟΣ ΜΕΣΟΣ)=0.20330 ΑΡΑ ΑΛΛΑΖΕΙ Η ΕΚΤΙΜΗΣΗ ΜΟΥ ΣΕ ΣΧΕΣΗ ΜΕ ΤΟ ΚΕΛΙ 1

# # ΑΣΚΗΣΗ 40

# In[6]:


import random
random.seed(2018)
from simple_markov_chain_lib import markov_chain

p = 0.6
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
 
mc = markov_chain(markov_table, init_probs)

counter = 0
N = 200
for i in range(N):
    mc.start()
    while mc.running_state != 'GameA' and mc.running_state != 'GameB':
        mc.move()
    if mc.running_state == 'GameA': counter += 1
phat = counter/N
    
print(
    '''The probability of player_A winning the set is''',phat
)


# ΟΝΟΜΑΤΕΠΩΝΥΜΟ:ΠΑΤΣΟΓΙΑΝΝΗΣ ΠΑΡΑΣΚΕΥΑΣ
# 
# ΣΧΟΛΗ:ΕΜΦΕ
# 
# ΑΡ.ΜΗΤΡΩΟΥ:GE15138
