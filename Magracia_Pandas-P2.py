#!/usr/bin/env python
# coding: utf-8

# ## EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS) - Part 2
# ### _Magracia, Marc Reggie Sean S.   |   2ECE-C  |  September 17, 2024_
# Instructions: _Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin._

# In[96]:


# For accessing Pandas library
import pandas as pd


# ________

# #### PROBLEM 2: 
# ##### _(Save your file as Magracia_Pandas-P2.py)_ 

# In[100]:


# load the .csv file 
cars = pd.read_csv('cars.csv')


# In[102]:


# Display the first 5 rows of the database with odd-numbered column 
oddcars = cars.iloc[[1,3,5,7,9],: ]
oddcars


# In[103]:


# Display the row that contains the ‘Model’ of ‘Mazda RX4’
cars.loc[cars['Model'] == 'Mazda RX4']


# In[104]:


# Amount of cylinders (‘cyl’) the ‘Camaro Z28’ has
cars.loc[cars['Model'] == 'Camaro Z28',['cyl']]


# In[106]:


# Amount of cylinders (‘cyl’) and gear type (‘gear’) the ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have  
cars.loc[[1,18,28],['cyl','gear']]

