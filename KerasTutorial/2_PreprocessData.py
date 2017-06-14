# -*- coding: utf-8 -*-
"""
Created on Tue May 23 23:26:22 2017

@author: dito-maf
"""

# Load data
import pandas as pd
import seaborn as sns
white = pd.read_csv("../Data/Wine/winequality-white.csv",sep=";")
red = pd.read_csv("../Data/Wine/winequality-red.csv",sep=";")
#add new column 'type' in the existing DataFrame
#0= white, 1= red
white['type']=0
red['type']=1
wines=red.append(white,ignore_index='True' )#??
print(wines.describe())

corr= wines.corr()
sns.heatmap(corr, xticklabels=corr.columns.values , yticklabels=corr.columns.values )
sns.plt.savefig("Corr")
sns.plt.show()