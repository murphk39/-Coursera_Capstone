#!/usr/bin/env python
# coding: utf-8

# # Import modules

# In[1]:


import numpy as np 
import pandas as pd


# ## Data processing 

# Had to download the csv file online as my foursquare API was not working. 

# In[2]:


toronto_data = pd.read_csv('toronto_data.csv')
geospatial_coords = pd.read_csv('Geospatial_Coordinates.csv')
geospatial_coords.columns = ['Postcode', 'Latitude', 'Longitude']


# In[3]:


print(geospatial_coords.shape)
geospatial_coords.head()


# In[4]:


toronto_data_w_gsptl = pd.merge(toronto_data,geospatial_coords,on='Postcode', how='inner')
toronto_data_w_gsptl.head(12)


# In[5]:


toronto_data_w_gsptl.to_csv('toronto_data_w_gsptl.csv', index=False)

