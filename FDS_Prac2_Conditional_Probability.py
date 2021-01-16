#!/usr/bin/env python
# coding: utf-8

# # FDS: PRACTICAL 2 : CONDITIONAL PROBABILITY

# In[6]:


import pandas as pd
import numpy as np
df = pd.read_csv('D:/MscPart1_RollNo34/student-mat.csv')
df.head(3)


# In[7]:


len(df)


# In[10]:


df['grade_A']=np.where(df['G3']*5>=80,1,0)
df['high_absenses'] = np.where(df['absences'] >= 10, 1, 0)
df['count'] = 1
df = df[['grade_A','high_absenses','count']]
df.head()


# In[11]:


pd.pivot_table(
    df, 
    values='count', 
    index=['grade_A'], 
    columns=['high_absenses'], 
    aggfunc=np.size, 
    fill_value=0
)

