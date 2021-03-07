
# coding: utf-8

# In[2]:


from simple_markov_chain_lib import markov_chain #import markov chain simulator

#transition table
markov_table = {
    'Μ': {'Σ': 1.},
    'Σ': {'Μ': 1/4, 'Β': 1/4, 'Κ': 1/4, 'Υ': 1/4},
    'Β': {'Σ': .5, 'Κ': .5},
    'Κ': {'Σ': .5, 'Β': .5},
    'Υ': {'Σ': 1.}
}

#initial distribution
init_dist= {'Μ': 1.} #we start from state 0 with probability 1

mc=markov_chain(markov_table, init_dist)

mc.start()
print("At time {} the chain is in state {}". format(mc.steps, mc.running_state))
for i in range(20):
    mc.move()
    print("At time {} the chain is in state {}". format(mc.steps, mc.running_state))

