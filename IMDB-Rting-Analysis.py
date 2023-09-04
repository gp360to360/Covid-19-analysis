#!/usr/bin/env python
# coding: utf-8

# # IMDB Rating analysis

# In[1]:


## importing liabraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[2]:


df = pd.read_csv(r'C:\Users\gpra7\Downloads\archive (9)\movies.csv')


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


df.shape


# In[6]:


df.duplicated().sum()


# In[7]:


df.isnull()


# In[8]:


pd.isnull(df).sum()[pd.isnull(df).sum() > 0]


# ### What are the top 10 movies on the basis of imdb rating?

# In[9]:


df2 = df.sort_values('Rating',ascending = False)
df2


# In[10]:


Top_10_rating = df2.head(10)


# In[11]:


Top_10_rating


# In[12]:


Top_10_rating.columns


# In[13]:


Top_10_budget = df.sort_values('Income',ascending = False)
Top_10_budget.head(10)


# In[14]:


get_ipython().system('pip install forex_python')
from forex_python.converter import CurrencyRates


# In[15]:


df.isnull().sum()


# In[16]:


df.dtypes


# In[17]:


df['Budget'] = df['Budget'].replace(['Unknown'],0,inplace = True)


# In[18]:


df['Income'] = df['Income'].replace(['Unknown'],0)


# In[19]:


Top_10_budget.head(10)


# In[20]:


df['Budget'].replace({'Unknown':'0'},inplace = True)


# In[21]:


Top_10_budget.head(10)


# In[22]:


df = df.replace(Unknown,0)


# In[ ]:


df.count().sum()


# ### Rating vs Count Ratio

# In[23]:


fig = px.bar(df, x=df['Rating'], y=df['Rating'],  barmode='stack')
fig.show()


# In[25]:


df['Country_of_origin'].unique_values


# In[26]:


df2 = df.pivot_table(index = ['Country_of_origin'], aggfunc ='size')
df2


# In[27]:


sort_df2 = df2.sort_values(ascending = False)


# In[28]:


sort_df2.head(20)


# In[29]:


fig = px.pie(df, values=sort_df2, names=sort_df2.index, title='Population of European continent')
fig.show()


# In[30]:


Count_of_movies_yearwise = df.pivot_table(index = ['Year'], aggfunc ='size')
Count_of_movies_yearwise


# ###     
# 1.Equal movies taken each year. 
# 
# 2.Their is a chance that they miss some important movies.

# In[ ]:





# In[ ]:




