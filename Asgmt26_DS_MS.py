#!/usr/bin/env python
# coding: utf-8

# # Pandas 1 🐼👩‍💻

# In[ ]:


# Q1. Create a Pandas Series that contains 
#the following data: 4, 8, 15, 16, 23, and 42. 
#Then, print the series.



# In[13]:


import pandas as pd
import numpy as np
import os


# In[4]:


data = [4, 8, 15, 16, 23, 42]
series = pd.Series(data)


# In[5]:


print(series)


# In[6]:


# Q2. Create a variable of list type containing 10 elements in it, 
#and apply pandas.Series function on the variable print it.

l = ['No quiero salir a las', 19, 'espero gastar menos de ' , (21.93)]

series = pd.Series(l)


# In[7]:


print(series)


# In[ ]:


# Q3. Create a Pandas DataFrame that contains the following data:


# Name
# Alice
# Bob
# Claire
# 
# Age
# 25
# 30
# 27
# 
# Gender
# Female
# Male
# Female

# In[8]:


data = { 'Name': ['Alice', 'Bob', 'Claire'],
         'Age': [25, 30, 27],
         'Gender':['Female', 'Male', 'Female']
}


# In[9]:


df = pd.DataFrame(data)


# In[10]:


df


# In[ ]:


# Q4. What is ‘DataFrame’ in pandas and 
#how is it different from pandas.series? Explain with an example.


# First a pandas series is a 1d array capable of storing various data types (int, str, float, obj etc)
# We can convert list to tuple , dict into series using 'Series()' mthd

# Dataframes , are 2-Dlabeled data structures with often columns of different types, in df each
# column is represented as pd



# In[ ]:


# Q5. What are some common functions you can use to manipulate data 
# in a Pandas DataFrame? 
# give an example of when you might use one of these functions


# In[19]:


# There are many , but here are a few of the top ones


# .read_csv('')

df = pd.read_csv("C:\\Users\\Maria Guevara\\Desktop\\condavscodejupyter\\taxonomy.csv")


# In[35]:


df


# In[ ]:


# Getting top and lower rows


# In[20]:


df.head()


# In[21]:


df.tail()


# In[ ]:


# Getting basic info about columns in table 


# In[22]:


df.info()


# In[23]:


df.shape


# In[24]:


df.size


# In[ ]:


# Choose n number of random samples from dataset


# In[25]:


df.sample(n=10)


# In[26]:


# Getting stats from numerical data
df.describe()


# In[28]:


# Getting unique values, will tell us how many categorical
df.nunique()


# In[29]:


# Finding missing values
df.isna().any()


# In[30]:


# Findinf null values
df.isnull().sum()


# In[32]:


# Get Columns
df.columns


# In[ ]:


# loc and iloc - for rows


# In[33]:


df.loc[1:6]


# In[36]:


df.iloc[1:6]


# In[37]:


# Slicing Data
df[1:16] # getting til 15th row


# In[38]:


# Group by
df[['name', 'parent_name']].groupby(df[parent_id])


# In[40]:


# Sorting
df.sort_values(by='parend_id', ascending=False)


# In[ ]:


#Q6. Which of the following is mutable in nature Series, DataFrame, Panel?


# In[ ]:


# All pandas data structure are 'value-mutable' but not always size-mutable
# length of a series cannot be changed, but columns can be inserted into df 


# In[ ]:





# In[45]:


# Q7. Create a DataFrame using multiple Series. Explain with an example.


recipes = pd.Series(['Pekin Duck', 'Shrimp Garlic Pasta', 'Protein McnCheese'], name='recipes')

calories = pd.Series([900, 1100, 1200], name='calories')

protein_macros = pd.Series([200, 175, 135], name='protein_macros')


# In[46]:


# Combining Series
df = pd.concat([recipes, calories, protein_macros], axis=1)


# In[47]:


print(df)


# In[ ]:




