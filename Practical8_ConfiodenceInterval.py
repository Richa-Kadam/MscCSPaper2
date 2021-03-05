#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.stats import sem, t
from numpy import mean
confidence = 0.95
data = [1, 2, 3, 4, 5]

n = len(data)
m = mean(data)
std_err = sem(data)
h = std_err * t.ppf((1 + confidence) / 2, n - 1)

start = m - h
print(start)

end = m + h
print(end)


# In[ ]:




