#!/usr/bin/env python
# coding: utf-8

# # FDS: PRACTICAL 1 : PERMUTATION AND COMBINATION

# Combinations

# In[25]:


import itertools 
from itertools import product
box_1=['g','b']
perm=[]
for p in itertools.product(box_1,repeat=2):
    perm.append(p)
    
perm


# In[26]:


box_2=['g','b','y']
perm=[]
for p in itertools.product(box_2,repeat=3):
    perm.append(p)

perm


# In[27]:


import itertools
box_1 = ['g','b']
perm = itertools.permutations(box_1)

for i in list(perm):
    print(i)


# In[28]:


box_2 = ['g','b','y']
perm = itertools.permutations(box_2)

for i in list(perm):
    print(i)


# Variation

# In[29]:


box_2=['g','b','y']
perm=[]
for p in itertools.product(box_2,repeat=2):
    perm.append(p)

perm


# In[30]:


box_2=['g','b','y']
perm = itertools.permutations(box_2,2)

for i in list(perm):
    print(i)


# Combinations

# In[31]:


from itertools import combinations_with_replacement

box_1=['g','b']
comb=combinations_with_replacement(box_1,2)

for i in list(comb):
    print(i)


# In[33]:


from itertools import combinations_with_replacement

box_2=['g','b','y']
comb=combinations_with_replacement(box_2,2)
for i in list(comb):
    print(i)


# In[34]:


from itertools import combinations
comb=combinations(box_1,2)
for i in list(comb):
    print(i)


# In[35]:


from itertools import combinations
comb=combinations(box_2,2)
for i in list(comb):
    print(i)

