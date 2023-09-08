#!/usr/bin/env python
# coding: utf-8

# In[43]:


"""
MSDS 530 (FUNDAMENTALS OF DATA SCIENCE)
WEEK 2 ASSIGNMENT
TOPIC: SCALES OF MEASUREMENT
DATE: SEPTEMBER 7, 2023
STUDENT/AUTHOR: STEPHEN SARPONG LARTEY
STUDENT ID: 005015848
"""


# In[1]:


pip install pandas


# In[2]:


import pandas as pd
import numpy as np
import statistics


# In[3]:


path = r"C:\Users\stevl\OneDrive\Desktop\UoC Lectures\MSDS 530-FUNDAMENTALS OF DS\Week 2\MSDSWeek2Assignment.xlsx"
df = pd.read_excel(path)


# In[4]:


print(df.columns)


# In[5]:


# Remove trailing spaces from column names
df.columns = df.columns.str.strip()

# Verify the cleaned column names
print(df.columns)


# In[6]:


# Calculate the mean for Age
mean_age = np.mean(df['Age'])
mean_age


# In[8]:


# Calculate the median for Age
median_age = np.median(df['Age'])
median_age


# In[10]:


# Calculate the standard deviation for Age
std_dev_age = np.std(df['Age'], ddof=0)  # ddof=0 for population standard deviation
std_dev_age


# In[11]:


# Calculate the variance for Age
variance_age = np.var(df['Age'], ddof=0)
variance_age


# In[20]:


# There is no mode for Age in NumPy, so we'll use statistics.mode from the statistics library
try:
    mode_age = statistics.mode(df['Age'])
except statistics.StatisticsError:
    mode_age = "N/A (No unique mode)"
else:
    print('mode_age N/A')


# In[31]:


# Calculate the mean for Purchase Amount
mean_purchase_amount = np.mean(df['Purchase Amount'])
mean_purchase_amount


# In[32]:


# Calculate the median for Purchase Amount
median_purchase_amount = np.median(df['Purchase Amount'])
median_purchase_amount


# In[33]:


# Calculate the standard deviation for Purchase Amount
std_dev_purchase_amount = np.std(df['Purchase Amount'], ddof=0)
std_dev_purchase_amount


# In[34]:


# Calculate the variance for Purchase Amount
variance_purchase_amount = np.var(df['Purchase Amount'], ddof=0)
variance_purchase_amount


# In[36]:


# Calculate the mode for Purchase Amount
try:
    mode_purchase_amount = statistics.mode(df['Purchase Amount'])
except statistics.StatisticsError:
    mode_purchase_amount = "N/A (No unique mode)"
mode_purchase_amount


# In[37]:


df.describe()


# In[39]:


get_ipython().system('pip install prettytable')


# In[40]:


from prettytable import PrettyTable


# In[41]:


# Create a table to display the results
table = PrettyTable()
table.field_names = ["Measure", "Age", "Purchase Amount"]
table.add_row(["Mean", round(mean_age, 2), round(mean_purchase_amount, 2)])
table.add_row(["Median", round(median_age, 2), round(median_purchase_amount, 2)])
table.add_row(["Mode", mode_age, mode_purchase_amount])
table.add_row(["Std Deviation", round(std_dev_age, 2), round(std_dev_purchase_amount, 2)])
table.add_row(["Variance", round(variance_age, 2), round(variance_purchase_amount, 2)])


# In[42]:


# Print the table
print(table)

