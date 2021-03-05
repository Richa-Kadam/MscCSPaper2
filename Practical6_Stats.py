#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv (r'G:/MSCs Practicals/DataScience/stats.csv')
print (df)


# Mean salary

# In[2]:


mean1 = df['Salary'].mean()
mean1


# Sum of salaries

# In[3]:


sum1 = df['Salary'].sum()
sum1


# Maximum salary

# In[4]:


max1 = df['Salary'].max()
max1


# Minimum salary

# In[5]:


min1 = df['Salary'].min()
min1


# Total count

# In[7]:


count1 = df['Salary'].count()
count1


# Median

# In[8]:


median1 = df['Salary'].median() 
median1


# Mode

# In[9]:


mode1 = df['Salary'].mode()
mode1


# Standard Deviation of salaries

# In[10]:


std1 = df['Salary'].std() 
std1


# Variance of salaries

# In[11]:


var1 = df['Salary'].var()  
var1


# In[12]:


groupby_sum1 = df.groupby(['Country']).sum() 
groupby_sum1
groupby_count1 = df.groupby(['Country']).count()
groupby_count1


# In[13]:


skew1=df.skew(axis = 0, skipna = True) 
skew1


# In[ ]:




