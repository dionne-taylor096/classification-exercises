#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder


def detect_column_types(df):
    """
    Returns a dictionary with column names grouped by their data types.
    """
    column_info = df.dtypes.groupby(df.dtypes).groups
    column_groups = {}
    for dtype, column_list in column_info.items():
        column_groups[dtype] = column_list.tolist()
    return column_groups


def clean_data(df):
    """
    Cleans the dataset by lowercase column names, removing nulls, and dropping unnecessary columns.
    """
    df.columns = df.columns.str.lower()
    df = df.dropna()
    columns_to_drop = ['customerid']
    df.drop(columns_to_drop, axis=1, inplace=True)
    return df


def encode_categorical_columns(df, categorical_columns, encoding_method='ordinal'):
    """
    Encodes categorical columns using the specified encoding method.
    """
    if encoding_method == 'ordinal':
        encoder = OrdinalEncoder()
        df[categorical_columns] = encoder.fit_transform(df[categorical_columns])
    # Add other encoding methods if needed
    return df


def change_numerical_columns_datatype(df, numerical_columns, datatype='float64'):
    """
    Changes the datatype of numerical columns.
    """
    for column in numerical_columns:
        df[column] = df[column].astype(datatype)
    return df


def encode_binary_columns(df, columns, encoding_method='ordinal'):
    """
    Encodes binary columns using the specified encoding method.
    """
    if encoding_method == 'ordinal':
        for col in columns:
            unique_values = df[col].unique()
            value_map = {value: i for i, value in enumerate(unique_values)}
            df[col] = df[col].replace(value_map).astype(int)
    # Add other encoding methods as needed
    return df

def get_numerical_columns(df):
    """
    Returns a list of column names for numerical columns.
    """
    numerical_columns = list(df.select_dtypes(include=[np.number]).columns)
    return numerical_columns

def get_categorical_columns(df):
    """
    Returns a list of column names containing categorical data in the given DataFrame.
    """
    object_columns = df.select_dtypes(include=['object']).columns.to_list()
    boolean_columns = df.select_dtypes(include=['bool']).columns.to_list()
    categorical_columns = object_columns + boolean_columns
    return categorical_columns

def prepare_telco_data(df):
    """
    Prepares the telco customer churn dataset for modeling by cleaning the data and encoding categorical and binary features.
    """
    # Clean the data
    df = clean_data(df)

    # Group columns by data types
    column_groups = detect_column_types(df)
    object_columns = column_groups[np.dtype('object')]
    int_columns = column_groups[np.dtype('int64')]
    float_columns = column_groups[np.dtype('float64')]

    # Identify binary, categorical, and numerical columns
    binary_columns = [col for col in object_columns if df[col].nunique() == 2]
    categorical_columns = [col for col in object_columns if df[col].nunique() > 2]
    numerical_columns = column_groups[np.dtype('int64')] + column_groups[np.dtype('float64')]

    # Encode categorical and binary columns
    df = encode_categorical_columns(df, categorical_columns)
    df = encode_binary_columns(df, binary_columns)

    # Change the datatype of numerical columns
    df = change_numerical_columns_datatype(df, numerical_columns)

    
    return df, categorical_columns

