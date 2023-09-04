#!/usr/bin/env python
# coding: utf-8

# # Covid-19 analysis
# 

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import plotly.graph_objects as go
import plotly.express as px


# In[2]:


files = os.listdir(r'C:\Users\gpra7\Downloads\archive (8)')
files


# In[3]:


### lets create a function to make our task simpler as we have to read data aggain & again 
def read_data(path,filename):
    return pd.read_csv(path+'/'+filename)


# In[4]:


path = r'C:\Users\gpra7\Downloads\archive (8)'
world_data=read_data(path,'worldometer_data.csv')


# In[5]:


world_data


# In[6]:


world_data.head()


# In[7]:


day_wise=read_data(path,files[2])


# In[8]:


fully_grouped = read_data(path,files[3])
fully_grouped


# In[9]:


usa_data=read_data(path,files[4])
usa_data


# In[10]:


province_data=read_data(path,files[1])
province_data


# ## Which Country has maximum Total cases, Deaths, Recovered & active cases lets create TreeMap Representaion of our data

# In[11]:


world_data.columns


# In[12]:


columns = ['TotalCases','TotalDeaths','TotalRecovered','ActiveCases']
for i in columns:
    fig = px.treemap(world_data[0:20],values=i,path=['Country/Region'],template="plotly_dark",title="<b>TreeMap representation of different Countries w.r.t their {}</b>".format(i))
    fig.show()


# ## What is the trend of Confirmed Deaths Recovered Active cases  
#  
#  ## Line Plot

# In[13]:


day_wise.head()


# In[14]:


fig = px.line(day_wise,x="Date",y=["Confirmed","Deaths","Recovered","Active"],title="Covid cases w.r.t date",template = "plotly_dark")
fig


# In[15]:


pop_test_ratio = world_data.iloc[0:20]['Population']/world_data.iloc[0:20]['TotalTests']


# In[16]:


pop_test_ratio


# ## find 20 most effected countries      
# 
# ### BarPlot Representaion of Population to Tests Done Ratio

# In[17]:


fig = px.bar(world_data.iloc[0:20],color='Country/Region',y=pop_test_ratio,x='Country/Region',template="plotly_dark",title="<b>population to tests done ratio</b>")
fig.show()


# ## 20 countries that are badly affected by corona 
# 
# ### Barplot Representaion of CoronaViruses Cases w.r.t Time

# In[18]:


fig = px.bar(world_data.iloc[0:20],x='Country/Region',y=['Serious,Critical','TotalDeaths','TotalRecovered','ActiveCases','TotalCases'],template="plotly_dark")


# In[19]:


fig.update_layout({'title':"Coronavirus cases w.r.t time"})
fig.show()


# ## Top 20 countries of Total Confirmed Cases, Total  Recoverd Cases, Total Deaths, Total Active Cases

# In[20]:


world_data.head()


# In[21]:


world_data['Country/Region'].unique()


# ## Top 20 countries of Confirmed Cases

# In[22]:


fig = px.bar(world_data.iloc[0:20],y='Country/Region',x='TotalCases',color='TotalCases',text="TotalCases")
fig.update_layout(template="plotly_dark",title_text="<b> Top 20 countries of Total confirmed cases</b>")
fig.show()


# ## Top 20 Countries of Total Deaths

# In[23]:


fig = px.bar(world_data.sort_values(by='TotalDeaths',ascending=False)[0:20],y='Country/Region',x='TotalDeaths',color='TotalDeaths',text="TotalDeaths")
fig.update_layout(template="plotly_dark",title_text="<b> Top 20 countries of Total deaths</b>")
fig.show()


# ## Top 20 Countries of Total Active Cases

# In[24]:


fig = px.bar(world_data.sort_values(by='ActiveCases',ascending=False)[0:20],y='Country/Region',color='ActiveCases',text='ActiveCases')
fig.update_layout(template="plotly_dark",title_text="<b>Top 20 countries of Total cases")
fig.show()


# ## Top 20 Countries of Total Recoveries

# In[25]:


fig=px.bar(world_data.sort_values(by='TotalRecovered',ascending=False)[:20],y='Country/Region',x='TotalRecovered',color='TotalRecovered',text='TotalRecovered')
fig.update_layout(template="plotly_dark",title_text="<b>Top 20 countries of Total Recovered")
fig.show()


# In[26]:


world_data.columns


# In[27]:


world_data[0:15]['Country/Region'].values


# ## Pie Chart Represention of Worst Affected Countries 
# 
# 
# ## Pie Chart in Dounut Shape

# In[28]:


labels = world_data[0:15]['Country/Region'].values
cases = ['TotalCases','TotalDeaths','TotalRecovered','ActiveCases']
for i in cases:
    fig = px.pie(world_data[0:15],values=i,names=labels,template="plotly_dark",hole=0.3,title="{} Recorded w.r.t to Who Region of 15 worst".format(i))
    fig.show()


# ## Deaths to Confirmed ratio

# In[29]:


deaths_to_confirmed=((world_data['TotalDeaths']/world_data['TotalCases']))
fig = px.bar(world_data,x='Country/Region',y=deaths_to_confirmed)
fig.update_layout(title={'text':"Death to confirmed ratio of some worst effected countries",'xanchor':'left'},template="plotly_dark")
fig.show()


# ## Deaths to Recovered Ratio

# In[30]:


deaths_to_recovered=((world_data['TotalDeaths']/world_data['TotalRecovered']))
fig = px.bar(world_data,x='Country/Region',y=deaths_to_recovered)
fig.update_layout(title={'text':"Death to recovered ratio of some worst effected countries",'xanchor':'left'},template="plotly_dark")
fig.show()


# ## Tests to Confirmed Ratio

# In[31]:


tests_to_confirmed=((world_data['TotalTests']/world_data['TotalCases']))
fig = px.bar(world_data,x='Country/Region',y=tests_to_confirmed)
fig.update_layout(title={'text':"Tests to confirmed ratio of some  worst effected countries",'xanchor':'left'},template="plotly_dark")
fig.show()


# ## Serious to Deaths Ratio

# In[32]:


serious_to_deaths=((world_data['Serious,Critical']/world_data['TotalDeaths']))
fig = px.bar(world_data,x='Country/Region',y=serious_to_deaths)
fig.update_layout(title={'text':"Tests to confirmed ratio of some  worst effected countries",'xanchor':'left'},template="plotly_dark")
fig.show()


# ## Automate Your Data for Visualize Confirmed, Active Recoverd

# In[33]:


from plotly.subplots import make_subplots  ## for creating subplots in plotly
import plotly.graph_objects as go


# In[34]:


def country_visualization(group_data,country):
    
    data=group_data[group_data['Country/Region']==country]
    df=data.loc[:,['Date','Confirmed','Deaths','Recovered','Active']]
    fig = make_subplots(rows=1, cols=4,subplot_titles=("Confirmed", "Active", "Recovered",'Deaths'))
    fig.add_trace(
        go.Scatter(name="Confirmed",x=df['Date'],y=df['Confirmed']),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(name="Active",x=df['Date'],y=df['Active']),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(name="Recovered",x=df['Date'],y=df['Recovered']),
        row=1, col=3
    )

    fig.add_trace(
        go.Scatter(name="Deaths",x=df['Date'],y=df['Deaths']),
        row=1, col=4
    )

    fig.update_layout(height=600, width=1000, title_text="Date Vs Recorded Cases of {}".format(country),template="plotly_dark")
    fig.show()


# In[35]:


country_visualization(fully_grouped,'Brazil')

