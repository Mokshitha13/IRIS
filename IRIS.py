#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


from warnings import filterwarnings
filterwarnings(action='ignore')


# In[2]:


iris=pd.read_csv("iris.csv")
print(iris)


# In[3]:


print(iris.shape)


# In[4]:


print(iris.describe())


# In[6]:


iris.head()


# In[7]:


iris.head(100)


# In[8]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
l = ['Versicolor', 'Setosa', 'Virginica']
s = [25,25,25]
ax.pie(s, labels = l,autopct='%1.2f%%')
plt.show()


# In[9]:


iris.hist()
plt.show()


# In[10]:


iris.plot(kind ='density',subplots = True, layout =(3,3),sharex = False)


# In[11]:


iris.plot(kind ='box',subplots = True, layout =(2,5),sharex = False)


# In[12]:


corr_mat = iris.corr()
print(corr_mat)

