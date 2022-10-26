#!/usr/bin/env python
# coding: utf-8

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[85]:


import pandas as pd
import numpy as np


# ** Read Salaries.csv as a dataframe called sal.**

# In[86]:


sal = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **

# In[87]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[88]:


sal.info()


# **What is the average BasePay ?**

# In[89]:


sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[90]:


sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[91]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# In[ ]:





# In[ ]:





# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[92]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']


# In[93]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# In[ ]:





# ** What is the name of highest paid person (including benefits)?**

# In[94]:


sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]


# In[ ]:





# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[95]:


sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]


# In[ ]:





# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[97]:


sal.groupby(['Year'])['BasePay'].mean()


# In[16]:





# In[ ]:





# In[ ]:





# ** How many unique job titles are there? **

# In[103]:


job_titles_count= len(sal['JobTitle'].unique().tolist())


# In[104]:


job_titles_count


# In[105]:


sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[107]:


sal['JobTitle'].value_counts().head()


# In[18]:





# In[ ]:





# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[108]:


(sal[sal['Year']==2013]['JobTitle'].value_counts()==1).sum()


# In[19]:





# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[123]:


len(sal[sal.JobTitle.str.contains('Chief')]) + len(sal[sal.JobTitle.str.contains('CHIEF')]) # returns for 'Chief' regardless of case


# In[21]:





# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[22]:





# In[23]:





# # Great Job!
