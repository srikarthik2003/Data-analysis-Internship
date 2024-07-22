#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[4]:


data = pd.read_csv("C:\\Users\\srika\\OneDrive\\Desktop\\house.csv")


# In[5]:


display(data.head(10))


# In[6]:


#scatter plot with year against own
plt.scatter(data['year'],data['own'])

#adding title to the plot
plt.title("scatter plot")

#setting x and y label
plt.xlabel('year')
plt.ylabel('own')

plt.show()


# In[8]:


#line chart with year against own
plt.plot(data['year'])
plt.plot(data['own'])

plt.title("line chart")

plt.xlabel('year')
plt.ylabel('own')

plt.show()


# In[9]:


#bar chart
plt.bar(data['year'],data['own'])

plt.title("bar chart")

plt.xlabel('year')
plt.ylabel('own')

plt.show()


# In[10]:


plt.hist(data['income'])

plt.title("histogram")

plt.show()

