#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Screen Time Analysis lets you know how much time you spend on what kind of applications and websites using your device. 
##And screen time analysis gives a visual report of the same.

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("C:\\Users\\Syam Prabath\\Downloads\\SCREEN TIME APP DETAILS.csv")
print(data.head())


# In[2]:


##Now let’s have a look if the dataset has any null values or not:

data.isnull().sum()


# In[3]:


##The dataset doesn’t have any null values. Now let’s have a look at the descriptive statistics of the data:

print(data.describe())


# In[4]:


##Now let’s start with analyzing the screen time of the user
##lets will first look at the amount of usage of the apps:

figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage")
figure.show()


# In[5]:


##Now let’s have a look at the number of notifications from the apps:

figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Notifications", 
                color="App", 
                title="Notifications")
figure.show()


# In[6]:


##Now let’s have a look at the number of times the apps opened:

figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened")
figure.show()


# In[7]:


##We generally use our smartphones when we get notified by any app.
##So let’s have a look at the relationship between the number of notifications and the amount of usage:

figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()


# In[8]:


##There’s a linear relationship between the number of notifications and the amount of usage. 
##It means that more notifications result in more use of smartphones.


# In[ ]:




