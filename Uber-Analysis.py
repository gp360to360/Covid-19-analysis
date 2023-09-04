#!/usr/bin/env python
# coding: utf-8

# # Uber Analysis
# 

# ### Prepare data for analysis

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


uber_15=pd.read_csv(r'C:\Users\gpra7\Downloads\archive (7)/uber-raw-data-janjune-15.csv',encoding='utf-8')


# In[3]:


uber_15.head(5)


# In[4]:


uber_15.shape


# In[5]:


uber_15.duplicated().sum()


# In[6]:


uber_15.drop_duplicates(inplace = True)


# In[7]:


uber_15.shape


# In[ ]:





# In[8]:


uber_15.dtypes


# In[9]:


uber_15['Pickup_date'] = pd.to_datetime(uber_15['Pickup_date'],format = '%Y-%m-%d %H:%M:%S')


# In[10]:


uber_15['Pickup_date'].dtype


# In[11]:


uber_15['month'] = uber_15['Pickup_date'].dt.month


# In[12]:


uber_15['month']


# In[13]:



uber_15['month'].value_counts().plot(kind = 'bar')


# In[14]:


uber_15['weekday']=uber_15['Pickup_date'].dt.day_name()
uber_15['day']=uber_15['Pickup_date'].dt.day
uber_15['hour']=uber_15['Pickup_date'].dt.hour
uber_15['month']=uber_15['Pickup_date'].dt.month
uber_15['minute']=uber_15['Pickup_date'].dt.minute


# In[15]:


uber_15.head(5)


# In[16]:


temp = uber_15.groupby(['month','weekday'],as_index = False).size()
temp.head()


# In[17]:


temp['month'].unique()


# In[18]:


dict_month = {1:'Jan',2:'Feb',3:'March',4:'April',5:'May',6:'June' }


# In[19]:


temp['month'] = temp['month'].map(dict_month)


# In[20]:


temp['month']


# In[21]:


plt.figure(figsize=(12,8))
sns.barplot(x='month',y='size',hue = 'weekday',data = temp)


# In[22]:


summary = uber_15.groupby(['weekday','hour'],as_index = False).size()


# In[23]:


plt.figure(figsize=(12,8))
sns.pointplot(x='hour',y='size',hue='weekday',data=summary)


# In[24]:


uber_foil=pd.read_csv(r'C:\Users\gpra7\Downloads\archive (7)/Uber-Jan-Feb-FOIL.csv')


# In[25]:


uber_foil


# In[26]:


get_ipython().system('pip install chart_studio --quiet')
get_ipython().system('pip install plotly --quiet')


# In[27]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs ,plot ,iplot ,init_notebook_mode
init_notebook_mode(connected=True)


# In[28]:


px.box(x = 'dispatching_base_number',y = 'active_vehicles',data_frame = uber_foil)


# In[29]:


px.violin(x = 'dispatching_base_number',y = 'active_vehicles',data_frame = uber_foil)


# In[30]:


import os


# In[31]:


files = os.listdir(r'C:\Users\gpra7\Downloads\archive (7)')[-7:]


# In[32]:


files.remove('uber-raw-data-jul14.csv')


# In[33]:


files


# In[34]:


path = r'C:\Users\gpra7\Downloads\archive (7)'
final=pd.DataFrame()

for file in files:
    current_df=pd.read_csv(path+'/'+file,encoding='utf-8')
    final=pd.concat([current_df,final])


# In[35]:


final.head()


# In[36]:


final.isnull().sum()


# In[37]:


final.shape


# In[38]:


final.duplicated().sum()


# In[39]:


final.drop_duplicates()


# In[40]:


final.shape


# In[41]:


rush_uber = final.groupby(['Lat','Lon'],as_index=False).size()


# In[42]:


rush_uber


# In[43]:


get_ipython().system('pip install folium')


# In[44]:


import folium


# In[45]:


folium.Map()


# In[46]:


basemap = folium.Map()


# In[47]:


from folium.plugins import HeatMap


# In[48]:


HeatMap(rush_uber).add_to(basemap)


# In[49]:


basemap


# In[50]:


final.tail(35)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[51]:


final['Date/Time'] = pd.to_datetime(final['Date/Time'],format='%m/%d/%Y %H:%M:%S')


# In[52]:


final['weeday'] = final['Date/Time'].dt.day
final['hour'] = final['Date/Time'].dt.hour


# In[53]:


final.head(3)


# In[54]:


pivot=final.groupby(['weeday','hour']).size().unstack()


# In[55]:


type(final.groupby(['weeday','hour']).size())


# In[56]:


pivot


# In[57]:


pivot.style.background_gradient()


# In[58]:


def gen_pivot_table(df,col1,col2):
    pivot=df.groupby([col1,col2]).size().unstack()
    return pivot.style.background_gradient()


# In[59]:


final.columns


# In[60]:


gen_pivot_table(final,'weeday','hour')


# In[ ]:




