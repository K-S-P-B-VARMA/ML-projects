#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("C:\\Users\\Syam Prabath\\Downloads\\covid transformed data.csv")
data2 = pd.read_csv("C:\\Users\\Syam Prabath\\Downloads\\covid raw data.csv")
print(data)


# In[2]:


##The dataset that we are using here contains two data files. 
##One file contains raw data, and the other file contains transformed one.
##let’s have a look at both the datasets one by one:

print(data.head())


# In[3]:


print(data2.head())


# In[4]:


##let’s have a look at how many samples of each country are present in the dataset:

data["COUNTRY"].value_counts()


# In[5]:


##Let’s have a look at the mode value:

data["COUNTRY"].value_counts().mode()


# In[6]:


##let’s create a new dataset by combining the necessary columns from both the datasets:

# Aggregating the data

code = data["CODE"].unique().tolist()
country = data["COUNTRY"].unique().tolist()
hdi = []
tc = []
td = []
sti = []
population = data["POP"].unique().tolist()
gdp = []

for i in country:
    hdi.append((data.loc[data["COUNTRY"] == i, "HDI"]).sum()/294)
    tc.append((data2.loc[data2["location"] == i, "total_cases"]).sum())
    td.append((data2.loc[data2["location"] == i, "total_deaths"]).sum())
    sti.append((data.loc[data["COUNTRY"] == i, "STI"]).sum()/294)
    population.append((data2.loc[data2["location"] == i, "population"]).sum()/294)

aggregated_data = pd.DataFrame(list(zip(code, country, hdi, tc, td, sti, population)), 
                               columns = ["Country Code", "Country", "HDI", 
                                          "Total Cases", "Total Deaths", 
                                          "Stringency Index", "Population"])
print(aggregated_data.head())


# In[7]:


## let’s sort the data according to the total cases of Covid-19:

# Sorting Data According to Total Cases

data = aggregated_data.sort_values(by=["Total Cases"], ascending=False)
print(data.head())


# In[8]:


##we can select the top 10 countries with the highest number of cases:

# Top 10 Countries with Highest Covid Cases

data = data.head(10)
print(data)


# In[9]:


## I will add two more columns (GDP per capita before Covid-19, GDP per capita during Covid-19) to this dataset:

data["GDP Before Covid"] = [65279.53, 8897.49, 2100.75, 
                            11497.65, 7027.61, 9946.03, 
                            29564.74, 6001.40, 6424.98, 42354.41]
data["GDP During Covid"] = [63543.58, 6796.84, 1900.71, 
                            10126.72, 6126.87, 8346.70, 
                            27057.16, 5090.72, 5332.77, 40284.64]
print(data)


# In[10]:


#Note: The data about the GDP per capita is collected manually.

figure = px.bar(data, y='Total Cases', x='Country',
            title="Countries with Highest Covid Cases")
figure.show()


# In[11]:


figure = px.bar(data, y='Total Deaths', x='Country',
            title="Countries with Highest Deaths")
figure.show()


# In[12]:


## let’s compare the total number of cases and total deaths in all these countries:

fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Total Cases"],
    name='Total Cases',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Total Deaths"],
    name='Total Deaths',
    marker_color='lightsalmon'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()


# In[13]:


##the percentage of total deaths and total cases among all the countries with the highest number of covid-19 cases:

# Percentage of Total Cases and Deaths
cases = data["Total Cases"].sum()
deceased = data["Total Deaths"].sum()

labels = ["Total Cases", "Total Deaths"]
values = [cases, deceased]

fig = px.pie(data, values=values, names=labels, 
             title='Percentage of Total Cases and Deaths', hole=0.5)
fig.show()


# In[14]:


death_rate = (data["Total Deaths"].sum() / data["Total Cases"].sum()) * 100
print("Death Rate = ", death_rate)


# In[15]:


##It shows how strictly countries are following these measures to control the spread of covid-19:

fig = px.bar(data, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'], 
             color='Stringency Index', height=400, 
             title= "Stringency Index during Covid-19")
fig.show()


# In[16]:


##Analyzing Covid-19 Impacts on Economy

fig = px.bar(data, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'], 
             color='GDP Before Covid', height=400, 
             title="GDP Per Capita Before Covid-19")
fig.show()


# In[17]:


##Now let’s have a look at the GDP per capita during the rise in the cases of covid-19:

fig = px.bar(data, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'], 
             color='GDP During Covid', height=400, 
             title="GDP Per Capita During Covid-19")
fig.show()


# In[18]:


fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["GDP Before Covid"],
    name='GDP Per Capita Before Covid-19',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["GDP During Covid"],
    name='GDP Per Capita During Covid-19',
    marker_color='lightsalmon'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()


# In[19]:


##Let’s have a look at how many countries were spending their budget on the human development:

fig = px.bar(data, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'], 
             color='HDI', height=400, 
             title="Human Development Index during Covid-19")
fig.show()


# In[ ]:




