#!/usr/bin/env python
# coding: utf-8

# Visualization Techniques In Data Science

# In[2]:


import pandas as pd
iris = pd.read_csv('G:/MSCs Practicals/DataScience/iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())


# In[3]:


wine_reviews = pd.read_csv('G:/MSCs Practicals/DataScience/winemag-data-130k-v2.csv', index_col=0)
wine_reviews.head()


# Scatter Plot

# In[4]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(iris['sepal_length'], iris['sepal_width'])
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')


# Line Chart

# In[5]:


columns = iris.columns.drop(['class'])
x_data = range(0, iris.shape[0])
fig, ax = plt.subplots()
for column in columns:
    ax.plot(x_data, iris[column], label=column)
ax.set_title('Iris Dataset')
ax.legend()


# Histogram

# In[6]:


fig, ax = plt.subplots()
ax.hist(iris['sepal_length'])
ax.set_title('iris')
ax.set_xlabel('sepal_length')
ax.set_ylabel('Frequency')


# Bar Chart

# In[7]:


fig, ax = plt.subplots() 
data = wine_reviews['points'].value_counts() 
points = data.index 
frequency = data.values 
ax.bar(points, frequency) 
ax.set_title('Wine Review Scores') 
ax.set_xlabel('Points') 
ax.set_ylabel('Frequency')


# In[8]:


wine_reviews['points'].value_counts().sort_index().plot.bar()


# In[9]:


wine_reviews['points'].value_counts().sort_index().plot.barh()


# In[10]:


wine_reviews.groupby("country").price.mean().sort_values(ascending=False)[:5].plot.bar()


# In[ ]:




