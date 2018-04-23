
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import sklearn as sc


# In[42]:


Col_Names= ['LectureID','LecturePaired','Frequency']
df_Pairs=pd.read_csv('C:\\Users\priya\Documents\Python Scripts\pairs.csv',sep=',',names=Col_Names)


# In[43]:


df_Pairs.head()


# In[44]:


df_Pairs=df_Pairs.drop(df_Pairs.index[0])


# In[7]:


Col_Names1= ['LectureID','Type','language','parentId','views','rec_date','pub_date','name']
df_Lectures=pd.read_csv('C:\\Users\priya\Documents\Python Scripts\lectures_train_New1.csv',sep=',',names=Col_Names1)


# In[8]:


df_Lectures.head()


# In[9]:


df_Lectures=df_Lectures.drop(df_Lectures.columns[[1, 3,5]], axis=1)


# In[10]:


df_Lectures=df_Lectures.drop(df_Lectures.index[0])


# In[11]:


Col_Names2= ['AuthorID','A_Name','email','homepage','gender','organization']
df_Authors=pd.read_csv('C:\\Users\\priya\\Documents\\Python Scripts\\authors.csv',sep=',',names=Col_Names2)
Col_Names3= ['CategoryID','C_Name','parentID','wikipediaURL']
df_Categories=pd.read_csv('C:\\Users\priya\Documents\Python Scripts\categories.csv',sep=',',names=Col_Names3)
Col_Names4= ['CategoryID','LectureID']
df_Categories_Lectures=pd.read_csv('C:\\Users\priya\Documents\Python Scripts\categories_lectures.csv',sep=',',names=Col_Names4)
Col_Names5= ['AuthorID','LectureID']
df_Authors_Lectures=pd.read_csv('C:\\Users\\priya\\Documents\\Python Scripts\\authors_lectures.csv',sep=',',names=Col_Names5)


# In[12]:


df_Authors=df_Authors.drop(df_Authors.columns[[2, 3,5,4]], axis=1)
df_Categories=df_Categories.drop(df_Categories.columns[[2, 3]], axis=1)
df_Categories=df_Categories.drop(df_Categories.index[0])
df_Authors=df_Authors.drop(df_Authors.index[0])
df_Categories_Lectures=df_Categories_Lectures.drop(df_Categories_Lectures.index[0])
df_Authors_Lectures=df_Authors_Lectures.drop(df_Authors_Lectures.index[0])


# In[34]:


df_Authors.head()


# In[33]:


df_Categories.head()


# In[31]:


df_Categories_Lectures.head()


# In[30]:


df_Authors_Lectures.head()


# In[18]:


df_Authors_Lectures=pd.merge(df_Authors_Lectures,df_Authors, on='AuthorID')


# In[19]:


df_Categories_Lectures=pd.merge(df_Categories_Lectures,df_Categories, on='CategoryID')


# In[20]:


df_Authors_Lectures_Category=pd.merge(df_Categories_Lectures,df_Authors_Lectures, on='LectureID')


# In[1]:


df_Authors_Lectures_Category.head()


# In[45]:


df_Authors_Lectures_Category=pd.merge(df_Authors_Lectures_Category,df_Lectures, on='LectureID')


# In[23]:


df_Authors_Lectures_Category=df_Authors_Lectures_Category.dropna()    #Dropping Null Values


# In[24]:


df_Authors_Lectures_Category=df_Authors_Lectures_Category.drop_duplicates()                                #removing duplicate values


# In[25]:


from sklearn.preprocessing import StandardScaler                  
scaler = StandardScaler()
array = df_Authors_Lectures_Category.values
X = array[:,0:9]


# In[ ]:


df_Authors_Lectures_Category=pd.merge(df_Authors_Lectures_Category,df_Pairs, on='LectureID')


# In[26]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[27]:


sns.set_style('white')


# In[28]:


get_ipython().magic('matplotlib inline')


# In[29]:


df_Lectures.groupby(by=['LectureID'])['views'].mean().sort_values(ascending=False).head()

