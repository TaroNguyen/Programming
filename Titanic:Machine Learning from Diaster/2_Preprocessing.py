#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 01:02:12 2017

@author: dito-maf
"""

import pandas as pd
gender = pd.read_csv("../Data/TitanicSurvival/gender_submission.csv",sep=",")
test = pd.read_csv("../Data/TitanicSurvival/test.csv",sep=",")
train = pd.read_csv("../Data/TitanicSurvival/train.csv",sep=",")

#delete column
train.drop( 'PassengerId' , 1, inplace=True) #axis=1 for columns
train.drop( 'Name' , 1, inplace=True)
train.drop( 'Cabin' , 1, inplace=True)
train.drop( 'Embarked' , 1, inplace=True)
train.drop( 'Ticket' , 1, inplace=True)
#Change value
train['Sex']=train['Sex'].map({'female': 0, 'male': 1})
#train['Embarked']=train['Embarked'].map({'C': 0, 'S': 1, 'Q':2})
train['Age']=train['Age'].fillna(train['Age'].mean())
train['Age'] = np.where(train['Age'] > 15, 1, 0)

#delete column
test.drop( 'PassengerId' , 1, inplace=True) #axis=1 for columns
test.drop( 'Name' , 1, inplace=True)
test.drop( 'Cabin' , 1, inplace=True)
test.drop( 'Embarked' , 1, inplace=True)
test.drop( 'Ticket' , 1, inplace=True)
#Change value
test['Sex']=test['Sex'].map({'female': 0, 'male': 1})
test['Age']=test['Age'].fillna(test['Age'].mean())
test['Age'] = np.where(test['Age'] > 15, 1, 0)
test['Fare']=test['Fare'].fillna(test['Fare'].mean())