#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 01:55:14 2017

@author: dito-maf
"""

y_predicted = model.predict(np.array(test))
Prediction = list()
for i in range(len(y_predicted) ) :
    if (y_predicted[i][0]> y_predicted[i][1]) :
        Prediction.append(0)
    else:
        Prediction.append(1)
test2 = pd.read_csv("../Data/TitanicSurvival/test.csv",sep=",")
df= pd.DataFrame(columns=['PassengerId', 'Survived'])
df['PassengerId']= test2['PassengerId']
df['Survived']= Prediction
df.to_csv('TitanicResult.csv',index=False)