# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:05:49 2019

@author: samer
"""
'''
############################## ##################Basic
#1. make sure you can access the Slack channels for CEBD-1160!
#done 
#2. create a Github account at https://github.com/ 
# https://github.com/samerkr
#2. Project Kick-Off: pick a dataset from the sklearn toys dataset 
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine
# 3. Send to me as a private message through slack: your github account url and the dataset you chose
'''
from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
'''
########################################## Advanced &  Reach
#1. formulate a research question for your dataset - it can be a one line question or a more complex development. 
#2. Send to me as a private message
#3 write the steps detailing your preliminary idea of how to answer it 
#assumption question: what is the average alcohol rate for each class and the variance between those averages for each row based on its class
implemnation
1 : get alcohol mean grouping by class
2: create new function in order to return the specific mean value for each class
3: populate two new column to answer the above question 
'''

wine =load_wine()
# review the existing features inside the wine dataset 
print(wine.feature_names)
features = wine.data
target = wine.target
## Create a new data frame by merging feature_names & features & target by using pandas DataFrame(rows or data, columns) as below 
wine_df = pd.DataFrame(data=np.c_[features, target], columns=wine.feature_names + ['class'])
print(wine_df)
wine_df.to_csv('wine_df.csv', sep=';', encoding='utf-8')
print("#######Average Alcohol Rate for each wine class")
print(wine_df.groupby('class')['alcohol'].mean())
average_alcohol_per_class=wine_df.groupby('class')['alcohol'].mean()
mean_class0 =round(average_alcohol_per_class[0],2)
print(f'mean_class0={mean_class0}')
mean_class1 =round(average_alcohol_per_class[1],2)
print(f'mean_class1={mean_class1}')
mean_class2 =round(average_alcohol_per_class[2],2)
print(f'mean_class2={mean_class2}')
print("Describe The Data Frame")
print(wine_df.describe())
print("#####variance between those averages for each row based on its class ")
res=wine_df[['alcohol','class']]
####### New Function for code clarity  
def setMean(row):  
    if row['class'] == 0:
        return mean_class0
    elif row['class'] ==1:
        return mean_class1
    elif row['class'] ==2:
        return mean_class2
####        
res['mean_per_class'] = res.apply (lambda row: setMean(row), axis=1)
res['variance_mean'] = res['alcohol']-res['mean_per_class']
## save the result into csv file 
res.to_csv('wine_df_question_answer.csv', sep=';', encoding='utf-8')
    
print(res)
 