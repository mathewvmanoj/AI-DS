#!/usr/bin/env python
# coding: utf-8

# # ML group assignment

# # 1. Cleaning DataSet

# In[141]:


#Importing libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[142]:


#Read data from given dataset

data = pd.read_csv(r'/Users/kundansingh/Desktop/College/UserRetentionData.csv')
data


# In[143]:


data.columns


# In[144]:


#To check missing values
data.isnull().sum()


# In[145]:


#To check data types of column
data_type = data.dtypes
data_type


# In[146]:


#To find duplicate values in column
duplicates = data.duplicated().sum()
duplicates


# There is no missing values in any of the column with no duplicate row in data set and also data type of each cloumn is appropriate

# # 2. EDA

# In[147]:


#describe data set
desc = data.describe()
desc


# In[148]:


#Encode for categorical value

from sklearn.preprocessing import OneHotEncoder as prep  #(Import libriay for box plot)

encd = prep(sparse=False)
encd_Column = encd.fit_transform(data[['Region','Trunk Calling Facility','Voice Messaging']])

#Creating data frame from above column
encd_df = pd.DataFrame(encd_Column, columns = encd.get_feature_names_out(['Region','Trunk Calling Facility','Voice Messaging']))

cleaned_data = pd.concat([data.drop(['Region','Trunk Calling Facility','Voice Messaging'], axis=1), encd_df], axis=1)

cleaned_data.head()


# In[149]:


#Description of cleaned data

descCleanData = cleaned_data.describe()
descCleanData


# 
# [Pie chart of some categorical data]
# 
# 

# In[150]:


data['Acct Closed?'].value_counts().plot(kind='pie', autopct='%.2f')


# In[151]:


data['Trunk Calling Facility'].value_counts().plot(kind='pie', autopct='%.2f')


# In[152]:


data['Voice Messaging'].value_counts().plot(kind='pie', autopct='%.2f')


# In[153]:


#Handling outliers

columnOutlier = ['Tenure','Number voice messages','Minutes Peak Hrs','Bill Peak Hrs','Minutes Off Peak','Bill Off Peak','Minutes Night','Bill Night']

#Creating box plot
 
plt.figure(figsize=(16,11))                      
for i, column in enumerate(columnOutlier):      #for every given column ploting Box plot
    plt.subplot(4,4,i+1)
    sns.boxplot(y=cleaned_data[column])         #using above cleaned_data for Box (Without outliers)
    plt.title(column)


# In[154]:


#Histogram for given column

columnHistogram = ['Tenure','Number voice messages','Minutes Peak Hrs','Bill Peak Hrs']

plt.figure(figsize=(15,10))
for i, column in enumerate(columnHistogram): #for every column in above list
    plt.subplot(2,2,i+1)
    sns.histplot(cleaned_data[column], kde=True) #kde = Kernel Density Estimate (Do data smoothing - check line on bars)
    plt.title(column)

plt.show()


# Finding outliers and after removing outliers(cleaned_data) drawing Box ploat of some column to see spread of data in Quartiles, and created Histogram to analysis data distribution with smoothing of data using KDE.

# In[155]:


# Correlation matrix for numerical variables

corr_matrix = cleaned_data.corr()

#plotting for correlation matrix
plt.figure(figsize=(12,10))
sns.heatmap(correlation_matrix,linewidth = 0.5, cmap='coolwarm', annot=False)
plt.title("Correlation Matrix")
plt.show()


# Both red and blue indicate stronger coorelation and lighter shades shoes weak coorelation i,e; if high coorelation between call minutes and billing means if numbers of minutes spent by user increses then billing amount also increases.

# In[ ]:




