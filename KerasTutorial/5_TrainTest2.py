#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:25:16 2017

@author: dito-maf
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:59:29 2017

@author: dito-maf
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
white = pd.read_csv("../Data/Wine/winequality-white.csv",sep=";")
red = pd.read_csv("../Data/Wine/winequality-red.csv",sep=";")
white['type']=0
red['type']=1
wines=red.append(white,ignore_index='True' )#??
#specify data
X=wines.ix[:,0:11]

#specify target
y=np.ravel( wines.type)

X_train, X_test, y_train, y_test = train_test_split( X,y,test_size=0.33,random_state=42)

#Standarize data

scaler = StandardScaler().fit(X_train)  # ????
X_train= scaler.transform( X_train)
X_test= scaler.transform( X_test)
