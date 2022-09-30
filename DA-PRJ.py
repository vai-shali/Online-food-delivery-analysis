#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data= pd.read_csv("onlinedeliverydata.csv")
data


# In[3]:


# Printing the cols.:
print(data.columns)

#printing no. of cols:
ctr=0
for i in data.columns:
    ctr=ctr+1;

print("\n\nCount of attributes/Columns:"+str(ctr))


# In[4]:


# Count of rows:
row_ctr = len(data)
print("\nCount of unique rows: "+str(row_ctr))


# In[2]:


import pandas as pd
import numpy as np
missing_values = ["nil","NIL","Nil","NA","na","n/a","-","NiL","Nill","nill","N0","NiI","No Comments!","None","NiII","Nil\n"]
df = pd.read_csv("onlinedeliverydata.csv",na_values = missing_values)
df


# In[3]:


df['Reviews'].isnull().sum()


# In[4]:


df.isnull().sum()


# In[7]:


df['Reviews'].fillna('Not Specified',inplace=True)
df


# In[11]:


#These values need to be binned to give a clear picture of the analysis.
df['Age_group'] = pd.cut(df['Age'],bins = [15,20,25,30,35,40], labels = ['15-20y','20-25y','25-30y','30-35y','35-40y'])
df["Age_group"].value_counts()


# In[12]:


import seaborn as sns
sns.boxplot(df['Age'])
#Ages above 30 and below 19 are acting as outliers


# In[13]:


import seaborn as sns
sns.boxplot(df['Family size'])
#no outliers present in the column family size


# In[14]:


import seaborn as sns
sns.boxplot(df['latitude'])
#latitude values above 13.08 are considered as outliers


# In[15]:


import seaborn as sns
sns.boxplot(df['longitude'])
#longitude values above 77.72 are considered as outliers


# In[ ]:


#The other columns do not contain any outliers


# In[ ]:


#correlation among numerical variables


# In[22]:


df.corr()


# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(df.corr())
plt.show()


# In[ ]:


#insights from plots:


# In[24]:


plt.figure(figsize=(6,4))

plt.title('Gender of the population ordering online')
sns.countplot(x='Gender',data=df)
plt.show()
#the plot shows that men order more than women


# In[20]:


plt.figure(figsize=(10,8))
plt.title("Online Food Orders based on the Age of the Customer")
sns.countplot(x='Age',data=df,hue='Output',palette="Set2");
#This plot shows that people of age 23 order food online the most, followed by ages 22 and 25


# In[21]:


plt.figure(figsize=(10,8))
plt.title("Online Food Orders based on the Educational Qualification of the Customer")
sns.countplot(x='Occupation',data=df,hue='Output',palette="Pastel1");
#This plot shows that students order food online the most

