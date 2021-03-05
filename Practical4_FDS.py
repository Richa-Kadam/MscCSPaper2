#!/usr/bin/env python
# coding: utf-8

# DISCRETE DISTRIBUTIONS

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image


# In[2]:


import seaborn as sns
sns.set(color_codes=True)
sns.set(rc={'figure.figsize':(5,5)})


# UNIFORM DISTRIBUTION

# In[3]:


from scipy.stats import uniform


# In[4]:


n = 100
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc = start, scale=width)


# In[5]:


ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')


# Bernoulli Distribution

# In[6]:


from scipy.stats import bernoulli
data_bern = bernoulli.rvs(size=10000,p=0.6)
ax= sns.distplot(data_bern,
                 kde=False,
                 color="skyblue",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')


# BINOMINAL DISTRIBUTION

# In[7]:


from scipy.stats import binom
data_binom = binom.rvs(n=10,p=0.8,size=10000)


# In[8]:


ax = sns.distplot(data_binom,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')


# Poisson Distribution

# In[9]:


from scipy.stats import poisson
data_poisson = poisson.rvs(mu=3, size=10000)

ax = sns.distplot(data_poisson,
                  bins=30,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')


# In[ ]:




