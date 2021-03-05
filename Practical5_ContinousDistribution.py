#!/usr/bin/env python
# coding: utf-8

# CONTINOUS DISTRIBUTION

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
import seaborn as sns
sns.set(color_codes=True)
sns.set(rc={'figure.figsize':(5,5)})


# NORMAL DISTRIBUTION

# In[2]:


from scipy.stats import norm
data_normal = norm.rvs(size=10000,loc=0,scale=1)


# In[3]:


ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')


# Exponential Distribution

# In[4]:


from scipy.stats import expon
data_expon = expon.rvs(scale=1,loc=0,size=1000)


# In[5]:


ax = sns.distplot(data_expon,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')


# Chi Square Distribution

# In[6]:


from numpy import random
x = random.chisquare(df=2, size=(2, 3))
print(x) 


# In[7]:


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show() 


# In[ ]:




