#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import os
import env
from env import host, user, password


# In[4]:


def get_connection(db):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[21]:


def get_data():
    # Check if the data has already been cached
    cache_file = input("Enter a name for the CSV file: ")
    cache_file_csv = cache_file + ".csv"
    user = env.user
    password = env.password
    host = env.host
    #db = input('Enter the name of the database you want to access: ')
    #table = input('Enter the name of the table you want to access: ')
    
    if os.path.isfile(cache_file_csv):
        print(f'Loading data from {cache_file_csv}')
        df = pd.read_csv(cache_file_csv)
        print(df)
    else: 
        print("File doesn't exist.")
        db = input('Enter the name of the database you want to access: ')
        print("Establishing connection and diplaying query")
        conn = get_connection(db)
        table = input('Enter the name of the table you want to access: ')
        print("Diplaying query")
        
        # query and open table in pandas
        df = pd.read_sql(f'SELECT * FROM {table}', conn)
        
        # Cache the data by writing it to a CSV file
        new_cache_file = input("Enter a name for the CSV file to cache the data: ")
        new_cache_file_csv = new_cache_file + ".csv"
        df.to_csv(new_cache_file_csv, index=False)
        print(f'Saved data to {new_cache_file_csv}')
    return df


# In[ ]:


import os

def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)

        # Return the dataframe to the calling code
        return df  


# In[ ]:


import os

def get_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM species JOIN measurements USING (species_id)', get_connection('titanic_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)

        # Return the dataframe to the calling code
        return df  


# In[24]:


import os

def get_telco_data():
    filename = "telco_churn.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM customers LEFT JOIN contract_types USING (contract_type_id)LEFT JOIN internet_service_types USING (internet_service_type_id) LEFT JOIN payment_types USING (payment_type_id)', get_connection('titanic_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)

        # Return the dataframe to the calling code
        return df  


# In[ ]:




