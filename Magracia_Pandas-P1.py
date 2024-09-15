#!/usr/bin/env python
# coding: utf-8

# ## EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS) - Part 1
# ### _Magracia, Marc Reggie Sean S.   |   2ECE-C  |  September 17, 2024_
# Instructions: _Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin._

# In[37]:


# For accessing Pandas library
import pandas as pd


# ________

# #### PROBLEM 1: 
# ##### _(Save your file as Magracia_Pandas-P1.py)_ 

# In[55]:


# load the .csv file 
cars = pd.read_csv('cars.csv')
cars


# In[69]:


# Display the first and last 5 rows of the database 
firstcars = cars.head()
lastcars = cars.tail()
firstlastcars = pd.concat([firstcars, lastcars])
firstlastcars


# In[ ]:




