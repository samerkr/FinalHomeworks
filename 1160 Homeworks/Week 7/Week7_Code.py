# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:39:04 2019

@author: samer
"""
'''
################################ Basic
1. "refactor" your plotting code to work on the dataset as loaded by from sklearn.datasets import load_{yourdatasetname}
2. perform classification/regression on your dataset using Linear regression/Logistic regression, as applicable, and print performance

'''
from sklearn.datasets import load_wine
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression

print("Load Wine Dataset")
wine_df = load_wine()
columns_names = wine_df.feature_names
feature_x = wine_df.data
target_y = wine_df.target
print(columns_names)
print(feature_x)
print(target_y)
#####
# Splitting  features and target datasets into train and test  with test size 25%
feature_x_train, feature_x_test, target_y_train, target_y_test = train_test_split(feature_x, target_y, test_size=0.25)
################ train the Linear Regression model with fit() method
print("##################Linear Regression")
lrm = LinearRegression()
lrm.fit(feature_x_train, target_y_train)
# Output of the training is a model
print(f"Intercept: {lrm.intercept_}\n")
print(f"Coeficients: {lrm.coef_}\n")
print(f"Named Coeficients: {pd.DataFrame(lrm.coef_, columns_names)}")

################ train the Logistic Regression model with fit() method
print("##################Logistic Regression")
lorm = LogisticRegression()
lorm.fit(feature_x_train, target_y_train)
# Output of the training is a model
print(f"Intercept per class: {lorm.intercept_}\n")
print(f"Coeficients per class: {lorm.coef_}\n")

