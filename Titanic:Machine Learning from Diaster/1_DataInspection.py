# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import seaborn as sns
gender = pd.read_csv("../Data/TitanicSurvival/gender_submission.csv",sep=",")
test = pd.read_csv("../Data/TitanicSurvival/test.csv",sep=",")
train = pd.read_csv("../Data/TitanicSurvival/train.csv",sep=",")

#delete column
train.drop( 'PassengerId' , 1, inplace=True) #axis=1 for columns
train.drop( 'Name' , 1, inplace=True)
train.drop( 'Cabin' , 1, inplace=True)
train.drop( 'Embarked' , 1, inplace=True)
#Change value
train['Sex']=train['Sex'].map({'female': 0, 'male': 1})
train = train[pd.notnull(train['Age'])]


corr= train.corr()
sns.heatmap(corr, xticklabels=corr.columns.values , yticklabels=corr.columns.values )
sns.plt.savefig("CorrTitanic.png")
sns.plt.show()