#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 01:20:56 2017

@author: dito-maf
"""


from sklearn.preprocessing import StandardScaler
import numpy as np
#Standarize data
X_train =train.ix[:,1:7]

#specify target
y_train=np.ravel( train.Survived)

scaler = StandardScaler().fit(X_train)  # ????
#X_train= scaler.transform( X_train )
X_test= scaler.transform(test)
