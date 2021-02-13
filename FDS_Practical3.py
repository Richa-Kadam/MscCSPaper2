#!/usr/bin/env python
# coding: utf-8

# # FDS Practical 3 : Handling datasets

# In[1]:


my_dict = { 'name' : ["a", "b", "c", "d", "e","f", "g"],
                   'age' : [20,27, 35, 55, 18, 21, 35],
                   'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}

import pandas as pd
import numpy as np
df = pd.DataFrame(my_dict)
dfmy_dict = { 'name' : ["a", "b", "c", "d", "e","f", "g"],
                   'age' : [20,27, 35, 55, 18, 21, 35],
                   'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}

import pandas as pd
import numpy as np
df = pd.DataFrame(my_dict)
df


# In[2]:


df.to_csv('csv_example')
df


# In[3]:


df_csv = pd.read_csv('csv_example')
df_csv


# In[4]:


df.to_csv('csv_example', index=False)
df_csv = pd.read_csv('csv_example')
df_csv


# In[5]:


import pandas as pd
Location = "G:/MSCs Practicals/DataScience/student-mat.csv"
df = pd.read_csv(Location, header=None)
df.head()


# In[6]:


import pandas as pd
Location = "G:/MSCs Practicals/DataScience/student-mat.csv"
df = pd.read_csv(Location)
df.head


# In[7]:


import pandas as pd
Location = "G:/MSCs Practicals/DataScience/student-mat.csv"
# To add headers as we load the data...
df = pd.read_csv(Location, names=['RollNo','Names','Grades'])
# To add headers to a dataframe
df.columns = ['RollNo','Names','Grades']
df.head()


# In[8]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.to_csv('studentgrades.csv',index=False,header=False)
df


# In[9]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees)
columns = ['Names','Grades','BS','MS','PhD']
df = pd.DataFrame(data = Degrees, columns=columns)
df


# In[10]:


import pandas as pd
Location = "G:/MSCs Practicals/DataScience/gradedata.xlsx"
df = pd.read_excel(Location)
df.columns = ['first','last','sex','age','exer','hrs','grd','addr']
df.head()


# In[11]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,columns=['Names','Grades'])
writer = pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# In[21]:


pip install xlrd


# In[22]:


pip install xlwt openpyxl


# In[12]:


import sqlite3
con = sqlite3.connect("G:/MSCs Practicals/DataScience//portal_mammals.sqlite")

cur = con.cursor()
for row in cur.execute('SELECT * FROM species;'):
    print(row)

con.close()


# In[14]:


import sqlite3

con = sqlite3.connect("G:/MSCs Practicals/DataScience/portal_mammals.sqlite")

cur = con.cursor()

cur.execute('SELECT plot_id FROM plots WHERE plot_type="Control"')
print(cur.fetchall())

cur.execute('SELECT species FROM species WHERE taxa="Bird"')
print(cur.fetchone())

con.close()


# In[16]:


import pandas as pd
import sqlite3

con = sqlite3.connect("G:/MSCs Practicals/DataScience/portal_mammals.sqlite")
df = pd.read_sql_query("SELECT * from surveys", con)

print(df.head())

con.close()


# In[ ]:




