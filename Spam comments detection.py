#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("C:\\Users\\Syam Prabath\\Downloads\\Yt.csv")
print(data.sample(5))


# In[2]:


data = data[["CONTENT", "CLASS"]]
print(data.sample(5))


# In[3]:


data["CLASS"] = data["CLASS"].map({0: "Not Spam",
                                   1: "Spam Comment"})
print(data.sample(5))


# In[4]:


## Bernoulli Naive Bayes algorithm 

x = np.array(data["CONTENT"])
y = np.array(data["CLASS"])

cv = CountVectorizer()
x = cv.fit_transform(x)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.2, 
                                                random_state=42)

model = BernoulliNB()
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))


# In[5]:


sample = "Check this out: https://thecleverprogrammer.com/" 
data = cv.transform([sample]).toarray()
print(model.predict(data))


# In[6]:


sample = "Lack of information!" 
data = cv.transform([sample]).toarray()
print(model.predict(data)) 


# In[ ]:




