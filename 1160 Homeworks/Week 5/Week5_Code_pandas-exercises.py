# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:50:15 2019

@author: samer
"""

'''
BASIC
1. Do exercises 1-12 (all) from the DataFrames with Pandas section on the https://cce-bigdataintro-1160.github.io/CEBD-1160-fall-2019-site/5-pythonadv.html:

You can put all the solutions in a single script named pandas-exercises.py. If you prefer, you can split it into multiple scripts for each exercise like pandas-exercises-1.py ... pandas-exercises-n.py

'''
import pandas as pd
import matplotlib.pyplot as plt

'''
1: In pandas-notebook project do the following exercise in pairs
2: Load the insurance.csv in a DataFrame using pandas. Explore the dataset using functions like to_string(), columns, index, dtypes, shape, info() and describe(). Use this DataFrame for the following exercises.
3: Print only the column age
4: Print only the columns age,children and charges
5: Print only the first 5 lines and only the columns age,children and charges
6: What is the average, minimum and maximum charges ?
7: What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?
8: What is the age of the person who paid the maximum charge?
9: How many insured people do we have for each region?
10: How many insured people are children?
11: What do you expect to be the correlation between charges and age, bmi and children?
12: Using the method corr(), check if your assumptions were correct.
'''
# 2 
insurance_df = pd.read_csv('insurance.csv')
print("################Data Frame")
print(insurance_df)
print("################Data Frame - to_string()")
print(insurance_df.to_string())
print("################Data Frame - columns")
print(insurance_df.columns)
print("################Data Frame - index")
print(insurance_df.index)
print("################Data Frame - dtypes")
print(insurance_df.dtypes)
print("################Data Frame - shape")
print(insurance_df.shape)
print("################Data Frame - info()")
print(insurance_df.info())
print("################Data Frame - describe()")
print(insurance_df.describe())
# 3 
print("################ 3- Print only the column age")
print(insurance_df['age']) 
# 4
print("################ 4- Print only the columns age,children and charges")
print(insurance_df[['age','children','charges']]) 
# 5
print("################ 5- Print only the first 5 lines and only the columns age,children and charges")
print(insurance_df[['age','children','charges']].head(5)) 
# 6
print("################ 6-  What is the average, minimum and maximum charges ?")
print('Maximum charges =',insurance_df['charges'].max()) 
print('Minimum charges =',insurance_df['charges'].min()) 
print('Average charges =',insurance_df['charges'].mean()) 
# another way by using describe()
print(insurance_df['charges'].describe()) 
# 7
print("################ 7- What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?")
print(insurance_df[insurance_df['charges'] == 10797.3362][['age', 'sex','smoker']])
# 8
print("################ 8- What is the age of the person who paid the maximum charge?")
print(insurance_df[insurance_df['charges'] == insurance_df['charges'].max()][['age','charges']])
# 9
print("################ 9- How many insured people do we have for each region?")
print(insurance_df['region'].value_counts())
# 10
print("################ 10- How many insured people are children?")
print(insurance_df['age'].describe()) 
print("the result is 0 based on 18 years old",insurance_df[insurance_df['age'] < 18])
# 11
print("################ 11 & 12- correlation between charges and age, bmi and children")
print(insurance_df[['age', 'charges', 'bmi']].corr())
insurance_corr=insurance_df[['age', 'charges', 'bmi']].corr()
plt.matshow(insurance_df[['age', 'charges', 'bmi']].corr())
plt.xticks(range(len(insurance_corr.columns)), insurance_corr.columns, rotation=45 )
plt.yticks(range(len(insurance_corr.columns)), insurance_corr.columns, rotation=0 )
plt.colorbar()
plt.tight_layout()
print("we have negative high correlation between bmi & age also bmi & charges ")
