#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor

data = pd.read_csv("C:\\Users\\Syam Prabath\\Downloads\\Instagram reach analysis.csv", encoding = 'latin1')
print(data.head())


# In[3]:


##Before starting everything, let’s have a look at whether this dataset contains any null values or not:

data.isnull().sum()


# In[4]:


##So it has a null value in every column. Let’s drop all these null values and move further:

data = data.dropna()


# In[5]:


##Let’s have a look at the insights of the columns to understand the data type of all the columns:

data.info()


# In[6]:


##Now let’s start with analyzing the reach of my Instagram posts. 
##I will first have a look at the distribution of impressions I have received from home:

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Home")
sns.distplot(data['From Home'])
plt.show()


# In[7]:


##The impressions I get from the home section on Instagram shows how much my posts reach my followers. 
##Looking at the impressions from home, I can say it’s hard to reach all my followers daily. 
##Now let’s have a look at the distribution of the impressions I received from hashtags:

plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Hashtags")
sns.distplot(data['From Hashtags'])
plt.show()


# In[8]:


##Hashtags are tools we use to categorize our posts on Instagram so that we can reach more people based on the kind of content we are creating. 
##Looking at hashtag impressions shows that not all posts can be reached using hashtags, but many new users can be reached from hashtags. 
##Now let’s have a look at the distribution of impressions I have received from the explore section of Instagram:

plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Explore")
sns.distplot(data['From Explore'])
plt.show()


# In[9]:


##Now let’s have a look at the percentage of impressions I get from various sources on Instagram:

home = data["From Home"].sum()
hashtags = data["From Hashtags"].sum()
explore = data["From Explore"].sum()
other = data["From Other"].sum()

labels = ['From Home','From Hashtags','From Explore','Other']
values = [home, hashtags, explore, other]

fig = px.pie(data, values=values, names=labels, 
             title='Impressions on Instagram Posts From Various Sources', hole=0.5)
fig.show()


# In[10]:


##So the above donut plot shows that almost 50 per cent of the reach is from my followers, 
##38.1 per cent is from hashtags, 9.14 per cent is from the explore section, 
##and 3.01 per cent is from other sources.

##Now let’s analyze the content of my Instagram posts. 
##The dataset has two columns, namely caption and hashtags, which will help us understand the kind of content I post on Instagram.

##Let’s create a wordcloud of the caption column to look at the most used words in the caption of my Instagram posts:

text = " ".join(i for i in data.Caption)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.style.use('classic')
plt.figure( figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[11]:


##Now let’s create a wordcloud of the hashtags column to look at the most used hashtags in my Instagram posts:

text = " ".join(i for i in data.Hashtags)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure( figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[12]:


##Let’s have a look at the relationship between the number of likes and the number of impressions on my Instagram posts:

figure = px.scatter(data_frame = data, x="Impressions",
                    y="Likes", size="Likes", trendline="ols", 
                    title = "Relationship Between Likes and Impressions")
figure.show()


# In[13]:


##Now let’s see the relationship between the number of comments and the number of impressions on my Instagram posts:

figure = px.scatter(data_frame = data, x="Impressions",
                    y="Comments", size="Comments", trendline="ols", 
                    title = "Relationship Between Comments and Total Impressions")
figure.show()


# In[14]:


##Now let’s have a look at the relationship between the number of shares and the number of impressions:

figure = px.scatter(data_frame = data, x="Impressions",
                    y="Shares", size="Shares", trendline="ols", 
                    title = "Relationship Between Shares and Total Impressions")
figure.show()


# In[15]:


##Now let’s have a look at the relationship between the number of saves and the number of impressions:

figure = px.scatter(data_frame = data, x="Impressions",
                    y="Saves", size="Saves", trendline="ols", 
                    title = "Relationship Between Post Saves and Total Impressions")
figure.show()


# In[16]:


##Now let’s have a look at the correlation of all the columns with the Impressions column:

correlation = data.corr()
print(correlation["Impressions"].sort_values(ascending=False))


# In[17]:


##Analyzing Conversion Rate

conversion_rate = (data["Follows"].sum() / data["Profile Visits"].sum()) * 100
print(conversion_rate)


# In[18]:


##Let’s have a look at the relationship between the total profile visits and the number of followers gained from all profile visits:

figure = px.scatter(data_frame = data, x="Profile Visits",
                    y="Follows", size="Follows", trendline="ols", 
                    title = "Relationship Between Profile Visits and Followers Gained")
figure.show()


# In[19]:


##Let’s split the data into training and test sets before training the model:

x = np.array(data[['Likes', 'Saves', 'Comments', 'Shares', 
                   'Profile Visits', 'Follows']])
y = np.array(data["Impressions"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.2, 
                                                random_state=42)


# In[20]:


model = PassiveAggressiveRegressor()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)


# In[21]:


##Now let’s predict the reach of an Instagram post by giving inputs to the machine learning model:

# Features = [['Likes','Saves', 'Comments', 'Shares', 'Profile Visits', 'Follows']]
features = np.array([[282.0, 233.0, 4.0, 9.0, 165.0, 54.0]])
model.predict(features)


# In[ ]:




