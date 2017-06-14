#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 01:31:17 2017

@author: dito-maf
"""

from keras.models import Sequential

# Import `Dense` from `keras.layers`
from keras.layers import Dense
from keras.optimizers import SGD
import numpy as np




X_train_E= np.array(X_train)
y_train_E=np.ndarray( (len(y_train),2))
print( type(y_train_E[0][0]))

for i in range(len(y_train)):
    if (y_train[i]==0):
        y_train_E[i][0]=1
    else:
        y_train_E[i][0]=0
    y_train_E[i][1]=1-y_train_E[i][0]



model = Sequential()


#Add a dense layer of 15 sigmoid neuron 
model.add(Dense(10,activation='sigmoid', input_dim=6))
model.add(Dense(4,activation='sigmoid', input_dim=6))
model.add(Dense(2,activation='sigmoid'))


sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True) # ????
model.compile(optimizer=sgd,
              loss='mse',
              metrics=['accuracy'])

model.fit(X_train_E, y_train_E, epochs=1000, batch_size=714) #???
