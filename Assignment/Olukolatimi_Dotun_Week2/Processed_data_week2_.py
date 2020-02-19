#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[6]:


df = pd.read_csv("desktop/preprocessed_data.csv")


# In[7]:


# prints first five rows
df.head(5)


# In[8]:


# prints last five rows
df.tail(5)


# In[9]:


df.columns


# In[10]:


index_4 = df[3:4]
index_4


# In[11]:


df.shape


# In[12]:


df.describe()


# In[17]:


df1 = pd.read_csv("desktop/data.csv")


# In[18]:


df1


# In[19]:


df1.isnull().sum()


# In[20]:


df1.head()


# In[22]:


df1.shape


# In[23]:


df1.tail()


# In[24]:


index_4 = df1[3:4]
index_4


# In[25]:


df1.describe()


# In[35]:


from sklearn.impute import SimpleImputer as Imputer
imputer = Imputer(strategy = "mean") # since the features are mostly averages
imputer = imputer.fit(df1.iloc[:, 12:65])
df1.iloc[:, 12:65] = imputer.transform(df1.iloc[:, 12:65])


# In[59]:


df1.isnull().sum()


# In[44]:


from sklearn.impute import SimpleImputer as Imputer
imputer = Imputer(strategy = "mean") # since the features are mostly averages and some total
imputer = imputer.fit(df1.iloc[:, 77:131])
df1.iloc[:, 77:131] = imputer.transform(df1.iloc[:, 77:131])


# In[55]:


from sklearn.impute import SimpleImputer as Imputer
imputer = Imputer(strategy = "mean") # since the features are mostly ages and weight
imputer = imputer.fit(df1.iloc[:, 140:145])
df1.iloc[:, 140:145] = imputer.transform(df1.iloc[:, 140:145])


# In[58]:


from sklearn.impute import SimpleImputer as Imputer
imputer = Imputer(strategy = "mean") # since the feature is distance related
imputer = imputer.fit(df1.iloc[:, 74:75])
df1.iloc[:, 74:75] = imputer.transform(df1.iloc[:, 74:75])


# In[63]:


df1


# In[66]:


df1.shape


# In[70]:


df1 = df1.dropna() # Reason because the remaining "nan" values are categorical values


# In[71]:


df1.shape


# In[72]:


df1.isnull().sum()


# In[74]:


df2 = pd.read_csv("desktop/raw_fighter_details.csv")


# In[76]:


df2.columns


# In[77]:


df2.shape


# In[78]:


index_4 = df2[3:4]
index_4


# In[79]:


df2.describe()


# In[80]:


df2.corr


# In[84]:


df2["Height"]


# In[93]:


df2['Height'] = df2['Height'].replace(np.nan,5)


# In[95]:


df3 = pd.read_csv("desktop/raw_total_fight_data.csv")


# In[97]:


df3.shape


# In[98]:



df3.head()


# In[99]:



df3.tail()


# In[100]:


df3.corr


# 

# In[ ]:




