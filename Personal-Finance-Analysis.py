#!/usr/bin/env python
# coding: utf-8

# # Personal Finance Analysis
# 

# In[21]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[5]:


df = pd.read_excel(r'C:\Users\gpra7\Downloads\Bank_Personal_Loan_Modelling.xlsx',1)


# In[6]:


df


# In[7]:


df.shape


# In[8]:


df.head()


# In[9]:


df.isnull().sum()


# In[10]:


df.drop(['ID','ZIP Code'],axis=1,inplace = True)


# In[12]:


df.columns


# In[13]:


fig = px.box(df,y=['Age', 'Experience', 'Income', 'Family', 'Education'])
fig.show()


# In[14]:


df.skew()


# In[15]:


df.dtypes


# In[16]:


df.hist(figsize=(20,20))


# In[22]:


sns.distplot(df['Experience'])


# In[23]:


df['Experience'].mean()


# In[25]:


Negative_exp = df[df['Experience']<0]
Negative_exp


# In[27]:


sns.distplot(Negative_exp['Age'])


# In[28]:


Negative_exp['Experience'].mean()


# In[29]:


Negative_exp.size


# In[30]:


print('There are {} records which has negative values for experience, approx {} %'.format(Negative_exp.size , ((Negative_exp.size/df.size)*100)))


# In[31]:


data = df.copy()


# In[32]:


data.head()


# In[33]:


data['Experience']=np.where(data['Experience']<0,data['Experience'].mean(),data['Experience'])


# In[34]:


data[data['Experience']<0]


# In[35]:


plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),annot=True)


# In[36]:


data = data.drop(['Experience'],axis=1)


# In[37]:


data.head()


# In[38]:


data['Education'].unique()


# In[39]:


def mark(x):
    if x==1:
        return 'Undergrad'
    elif x==2:
        return 'Graduate'
    else :
        return 'Advanced/Professional'


# In[40]:


data['Edu_mark']=data['Education'].apply(mark)


# In[41]:


data.head()


# In[42]:


EDU_dis=data.groupby('Edu_mark')['Age'].count()


# In[43]:


EDU_dis


# In[46]:


fig = px.pie(data,values=EDU_dis,names=EDU_dis.index,title='Pie chart')
fig.show()


# In[47]:


data.columns


# In[48]:


def Security_CD(row):
    if (row['Securities Account']==1) & (row['CD Account']==1):
        return 'Holds Securites & Deposit'
    elif (row['Securities Account']==0) & (row['CD Account']==0):
        return 'Does not Holds Securites or Deposit'
    elif (row['Securities Account']==1) & (row['CD Account']==0):
        return ' Holds only Securites '
    elif (row['Securities Account']==0) & (row['CD Account']==1):
        return ' Holds only Deposit'


# In[49]:


data['Account_holder_category']=data.apply(Security_CD,axis=1)


# In[50]:


data.head()


# In[51]:


values = data['Account_holder_category'].value_counts()
values.index


# In[52]:


fig=px.pie(data,values=values, names=values.index,title='Pie CHart')
fig.show()


# In[53]:


px.box(data,x='Education',y='Income',facet_col='Personal Loan')


# In[54]:


plt.figure(figsize=(12,8))
sns.distplot(data[data['Personal Loan']==0]['Income'],hist=False,label='Income with no personal loan')
sns.distplot(data[data['Personal Loan']==1]['Income'],hist=False,label='Income with personal loan')
plt.legend()


# In[55]:


def plot(col1,col2,label1,label2,title):
    plt.figure(figsize=(12,8))
    sns.distplot(data[data[col2]==0][col1],hist=False,label=label1)
    sns.distplot(data[data[col2]==1][col1],hist=False,label=label2)
    plt.legend()
    plt.title(title)


# In[56]:


plot('Income','Personal Loan','Income with no personal loan','Income with personal loan','Income Distribution')


# In[57]:


plot('CCAvg','Personal Loan','Credit card avg with no personal loan','Credit card avg with personal loan','Credit card avg Distribution')


# In[58]:


col_names=['Securities Account','Online','Account_holder_category','CreditCard']


# In[59]:


for i in col_names:
    plt.figure(figsize=(10,5))
    sns.countplot(x=i,hue='Personal Loan',data=data)


# In[ ]:





# In[ ]:





# In[ ]:




