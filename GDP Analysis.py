#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[3]:


df = pd.read_csv(r'C:\Users\gpra7\Downloads\archive (11)/List of Countries by GDP Sector Composition.csv')


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.duplicated().sum()


# In[7]:


df.isna().sum()


# In[8]:


df.keys()


# In[9]:


df.head()


# In[10]:


df = df.rename(columns={'Unnamed: 5': 'Agriculture Rank', 'Unnamed: 6': 'Agriculture % of GDP', 'Industry': 'Industry GDP',
          'Unnamed: 8': 'Industry Rank','Unnamed: 9' : 'Industry % of GDP', 'Services': 'Services GDP', 
          'Unnamed: 11': 'Services Rank', 'Unnamed: 12': 'Services % of GDP'})


# In[11]:


df = df.drop(index = 0)


# In[12]:


df.keys()


# In[13]:


df.dtypes


# In[14]:


object_list = [ 'Rank', 'GDP (millions of $)',
       'Agriculture GDP', 'Agriculture Rank', 'Agriculture % of GDP',
       'Industry GDP', 'Industry Rank', 'Industry % of GDP', 'Services GDP',
       'Services Rank', 'Services % of GDP', 'Year GDP ', 'Year Sector']


# In[15]:


df = df.replace('-',np.NaN)
df = df.replace('FY12/13',2012)


# In[16]:


for i in object_list:
    print(i)
    df[i] = pd.to_numeric(df[i])
    


# In[17]:


df.head(152)


# In[39]:


df.dtypes


# In[19]:


df.isna().sum()


# In[20]:


df.describe()


# In[36]:


df.to_csv("C:\\Users\\gpra7\\Downloads\\archive (11)\\Clean GDP.csv")


# In[22]:


df.keys()


# In[23]:


topGDP = df.sort_values(by = 'GDP (millions of $)',ascending = False).head(20)


# In[24]:


topGDP


# In[25]:


topGDP = df.sort_values(by='GDP (millions of $)', ascending=False).head(20)
ax = sns.barplot(data=topGDP, x='Country/Economy', y='GDP (millions of $)').set(title="GDPs from Highest to lowest")
plt.xticks(rotation=90)


# In[26]:


fig = px.pie(topGDP, values='GDP (millions of $)', names='Country/Economy', title='GDPs from Highest to lowest')
fig.show()


# In[ ]:





# In[27]:


topAgr = df.sort_values(by='Agriculture GDP', ascending=False).head(20)
ax = sns.barplot(data=topAgr, x='Country/Economy', y='Agriculture GDP').set(title="Agriculture GDPs from Highest to lowest")
plt.xticks(rotation=90)


# In[28]:


topRank = df.sort_values(by='Agriculture % of GDP', ascending=False).head(20)
ax = sns.barplot(data=topRank, x='Country/Economy', y='Agriculture % of GDP').set(title="Agriculture % of GDPs from Highest to lowest")
plt.xticks(rotation=90)


# In[29]:


topInd = df.sort_values(by='Industry GDP', ascending=False).head(20)
ax = sns.barplot(data=topInd, x='Country/Economy', y='Industry GDP').set(title="Industry GDPs from Highest to lowest")
plt.xticks(rotation=90)


# In[30]:


topInd = df.sort_values(by='Industry % of GDP', ascending=False).head(20)
ax = sns.barplot(data=topInd, x='Country/Economy', y='Industry % of GDP').set(title="Industry % of GDP from Highest to lowest")
plt.xticks(rotation=90)


# In[31]:


topSer = df.sort_values(by='Services GDP', ascending=False).head(20)
ax = sns.barplot(data=topSer, x='Country/Economy', y='Services GDP').set(title="Services GDP from Highest to lowest")
plt.xticks(rotation=90)


# In[32]:


topSer = df.sort_values(by='Services % of GDP', ascending=False).head(20)
ax = sns.barplot(data=topSer, x='Country/Economy', y='Services % of GDP').set(title="Services % of GDP from Highest to lowest")
plt.xticks(rotation=90)


# In[33]:


ax = sns.scatterplot(data=df, x='Agriculture GDP', y='Industry GDP')
corr = df['Agriculture GDP'].corr(df['Industry GDP'])
print("Correlation between Agriculture GDP and Industry GDP is ", round(corr,2))


# In[ ]:





# In[ ]:




