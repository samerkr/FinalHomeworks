# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:19:04 2019

@author: samer
"""
'''
ADVANCED & REACH
1. This step should help you kickoff the final project for the course. All the steps should be done on the dataset you chose earlier in the course.
2. Create a python script myproject.py. Your script should:
 * load and organize the data in a pandas data frame format, please notice that some datasets will require that you manually fix the headers as they're not present in the dataset.
   * Tip: For the boston dataset, your separator will be sep='\\s+'. This will mitigate the problem with multiple spaces!
   * Tip: In order to fix the column names, you might have to manually assign the values to it as in the examples!
 * compute and print information and summary statistics on the dataset
 * compute and print correlations on the dataset
 '''
 # Im going to use my final project dataset winequality-white
import pandas as pd
import matplotlib.pyplot as plt
print("load and organize the data in a pandas data frame format")
whiteWine_df = pd.read_csv('winequality-white.csv', sep=';', encoding='utf-8')
print(whiteWine_df.describe())
print("################Data Frame")
print(whiteWine_df)
print("################Data Frame - to_string()")
print(whiteWine_df.to_string())
print("################Data Frame - columns")
print(whiteWine_df.columns)
print("################Data Frame - index")
print(whiteWine_df.index)
print("################Data Frame - dtypes")
print(whiteWine_df.dtypes)
print("################Data Frame - shape")
print(whiteWine_df.shape)
print("################Data Frame - info()")
print(whiteWine_df.info())
print("################Data Frame - describe()")
print(whiteWine_df.describe())
print("################ find correlation between the all features and plot them")
whiteWineCorr = whiteWine_df.corr(method='pearson')
print(whiteWineCorr.to_string())
plt.matshow(whiteWineCorr)
plt.xticks(range(len(whiteWine_df.columns)), whiteWine_df.columns, rotation=45 )
plt.yticks(range(len(whiteWine_df.columns)), whiteWine_df.columns, rotation=0 )
plt.colorbar()
plt.tight_layout()
print("we have high correlation between density & residual sugar also same between quality & alcohol ")