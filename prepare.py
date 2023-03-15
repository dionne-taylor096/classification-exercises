#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
from sklearn.model_selection import train_test_split


# Load the Iris dataset
iris = pd.read_csv('iris.csv')
iris = acquire.get_iris_data()

# Split the Iris dataset into training, testing, and validation sets
train, validate, test = split_data(iris)

# Load the Titanic dataset
titanic = pd.read_csv('titanic.csv')
titanic = acquire.get_titanic_data()

# Split the Titanic dataset into training, testing, and validation sets
train, validate, test = split_data(titanic)

# Load the Telco dataset
telco_churn = pd.read_csv('telco_churn.csv')
telco_churn = acquire.get_telco_data()
# Split the Telco dataset into training, testing, and validation sets
train, validate, test = split_data(telco_churn)


def split_data(df):
    # Split the data into training, testing, and validation sets
    train, test = train_test_split(df, test_size=0.2, random_state=123)
    train, validate = train_test_split(train, test_size=0.25, random_state=123)
    return train, validate, test


def prep_iris(iris):
    # Drop the 'species_id' and 'measurement_id' columns
    iris = iris.drop(['species_id', 'measurement_id'], axis=1)
    # Rename the 'species_name' column to 'species'
    iris = iris.rename(columns={'species_name': 'species'})
    # Create dummy variables of the 'species' column
    species_dummies = pd.get_dummies(iris['species'], prefix='species')
    # Concatenate the dummy variables onto the original DataFrame
    iris = pd.concat([iris, species_dummies], axis=1)
    return iris


def prep_telco(telco_churn):
    # Drop unnecessary columns
    telco_churn = telco_churn.drop(['customerID', 'gender', 'Partner', 'Dependents', 'PhoneService',          'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',      'StreamingMovies', 'PaperlessBilling', 'PaymentMethod'], axis=1)
    # Encode categorical columns using dummy variables
    telco = pd.get_dummies(telco, columns=['InternetService', 'Contract'])
    return telco_churn


def prep_titanic(titanic):
    # Drop the unnecessary columns
    titanic = titanic.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    # Create dummy variables of the categorical columns
    sex_dummies = pd.get_dummies(titanic['Sex'], prefix='sex')
    embarked_dummies = pd.get_dummies(titanic['Embarked'], prefix='embarked')
    pclass_dummies = pd.get_dummies(titanic['Pclass'], prefix='pclass')
    # Concatenate the dummy variables onto the original DataFrame
    titanic = pd.concat([titanic, sex_dummies, embarked_dummies, pclass_dummies], axis=1)
    # Drop the original categorical columns
    titanic = titanic.drop(['Sex', 'Embarked', 'Pclass'], axis=1)
    return titanic
