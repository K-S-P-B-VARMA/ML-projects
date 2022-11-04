#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


crimes_df = pd.read_csv("C:\\Users\\Syam Prabath\\Downloads\\crime against women data.csv")


# In[3]:


crimes_df


# In[4]:


crimes_df.shape


# In[5]:


##data preparation and cleaning

overall_crime = crimes_df.isna().sum()


# In[6]:


overall_crime


# In[7]:


##none of the columns have null values

districts = len(crimes_df.DISTRICT.unique())


# In[8]:


districts


# In[9]:


##But there are 718 districts in India, in total,
##which means there is messy or false datas in a huge amount, 
##in this case, we better drop the column "District" and also "Unnamed: 0", 
##as it is of no use, in our data analysis process.

crimes_df.drop(['DISTRICT', 'Unnamed: 0'], axis = 1, inplace=True)


# In[10]:


crimes_df.rename( columns = {'Kidnapping and Abduction':'Kidnapping_Abduction','Dowry Deaths':'Dowry_Deaths',
                             'Assault on women with intent to outrage her modesty':'Hurting_of_womens_modesty',
                             'Insult to modesty of Women':'Insult_to_womens_modesty',
                             'Cruelty by Husband or his Relatives':'Domestic_Cruelty',
                             'Importation of Girls':'Importation_of_Girls'}, inplace = True)


# In[11]:


crimes_df


# In[12]:


print(crimes_df['STATE/UT'].unique())


# In[13]:


## We can see from above that there are lot many repeated datas, like some of them are repeated again by using capital 
##letters and some of them have issues with space too, like A&N Islands 
##and also Delhi has been repeated again by mentioning it as Delhi UT

# Fist we will remove all the repeated uppercase values
def remove_uppercase(r):
    r = r['STATE/UT'].strip()
    r = r.upper()
    return r
crimes_df['STATE/UT'] = crimes_df.apply(remove_uppercase, axis=1)

#Now use replace function to replace the other type of repeated datas as dicussed above
crimes_df['STATE/UT'].replace("A&N ISLANDS", "A & N ISLANDS", inplace = True)
crimes_df['STATE/UT'].replace("D&N HAVELI", "D & N HAVELI", inplace = True)
crimes_df['STATE/UT'].replace("DELHI UT", "DELHI", inplace = True)


# In[14]:


#### Let's go through the datas now!

crimes_df['STATE/UT'].unique()


# In[15]:


#### Let's check the total number of States+UT


# In[16]:


len(crimes_df['STATE/UT'].unique())


# In[17]:


victims_raped = crimes_df.Rape.sum()
victims_kidnapped_abducted = crimes_df.Kidnapping_Abduction.sum()
dowery_death = crimes_df.Dowry_Deaths.sum()
modesty_assault = crimes_df.Hurting_of_womens_modesty.sum()
insult_to_modesty = crimes_df.Insult_to_womens_modesty.sum()
domestic_violence = crimes_df.Domestic_Cruelty.sum()
girls_imported = crimes_df.Importation_of_Girls.sum()


# In[18]:


total_population_of_victim_overall = victims_raped + victims_raped + dowery_death +modesty_assault+ insult_to_modesty + domestic_violence+ girls_imported
total_population_of_victim_overall


# In[19]:


fig, axes = plt.subplots(2, 3, figsize=(25, 12))

axes[0,0].set_title("Chart of rape cases in India in 2001-2014")
axes[0,0].bar(crimes_df.Year, crimes_df.Rape, color = 'black');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Rape in India') #Y-axis

axes[0,1].set_title("Chart of Kidnapping and Abduction cases in India in 2001-2014")
axes[0,1].bar(crimes_df.Year, crimes_df.Kidnapping_Abduction, color = 'violet');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Kidnapping and Abduction in India') #Y-axis

axes[0,2].set_title("Chart of Dowry death cases in India in 2001-2014")
axes[0,2].bar(crimes_df.Year, crimes_df.Dowry_Deaths, color = 'navy');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Dowry deaths in India') #Y-axis

axes[1,0].set_title("Chart of Assault to her modesty in 2001-2014")
axes[1,0].bar(crimes_df.Year, crimes_df.Hurting_of_womens_modesty, color = 'cyan');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Assaulting a women for her modesty in India') #Y-axis

axes[1,1].set_title("Chart of Domestic Violence cases in India in 2001-2014")
axes[1,1].bar(crimes_df.Year, crimes_df.Domestic_Cruelty, color = 'orange');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Domestic Violence in India') #Y-axis

axes[1,2].set_title("Chart of Importation of girls in India in 2001-2014")
axes[1,2].bar(crimes_df.Year, crimes_df.Importation_of_Girls, color = 'red');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases ofImportation of girls in India') #Y-axis


# In[20]:


count_df = crimes_df.groupby('Year')[['STATE/UT']].count()
count_df


# In[21]:


plt.figure(figsize=(10,5))
plt.title("Total cases reported from every state Year wise")
sns.heatmap(count_df);


# In[22]:


crimes_df = crimes_df.drop(['Hurting_of_womens_modesty', 'Insult_to_womens_modesty'], axis=1)


# In[23]:


max_rape_cases = crimes_df.sort_values('Rape', ascending = False).head(10)
max_rape_cases


# In[24]:


max_dowry_death_cases = crimes_df.sort_values('Dowry_Deaths', ascending = False).head(10)
max_dowry_death_cases


# In[25]:


max_domestic_violance_cases = crimes_df.sort_values('Domestic_Cruelty', ascending = False).head(10)
max_domestic_violance_cases


# In[26]:


max_importation_case = crimes_df.sort_values('Importation_of_Girls', ascending = False).head(10)
max_importation_case


# In[27]:


counts_df = crimes_df.groupby('STATE/UT')[['Rape', 'Kidnapping_Abduction', 'Dowry_Deaths','Domestic_Cruelty', 'Importation_of_Girls']].sum()
counts_df


# In[28]:


counts_df.sort_values(by = 'Rape', ascending = False).head(5)


# In[29]:


counts_df.sort_values(by = 'Kidnapping_Abduction', ascending = False).head(5)


# In[30]:


counts_df.sort_values(by = 'Dowry_Deaths', ascending = False).head(5)


# In[31]:


counts_df.sort_values(by = 'Domestic_Cruelty', ascending = False).head(5)


# In[32]:


counts_df.sort_values(by = 'Importation_of_Girls', ascending = False).head(5)


# In[33]:


max_importation_case = max_importation_case.merge(max_rape_cases)
max_importation_case


# In[34]:


max_dowry_death_cases = max_dowry_death_cases.merge(max_rape_cases)
max_dowry_death_cases


# In[ ]:




