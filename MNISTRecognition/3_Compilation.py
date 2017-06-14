#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 20:24:39 2017

@author: dito-maf
"""

from keras.models import Sequential

# Import `Dense` from `keras.layers`
from keras.layers import Dense
from keras.optimizers import SGD

# Initialize the constructor
import gzip
import pickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

# Use gzip to open a file
with gzip.open('../Data/HandWriting/mnist.pkl.gz', 'rb') as f:  # 'rb' ?????
    train_set, valid_set, test_set = pickle.load(f, encoding='latin1')

# Value in tuples cannot be changed and we use parentheses instead of brackets for tuples


train_x, train_y = train_set
train_y_Edited=list()
for i in range(len(train_y)):
    s= list()
    for j in range(10):
        if j==train_y[i]:
            s.append(1)
        else:
            s.append(0)
    train_y_Edited.append(s)
model = Sequential()


#Add a dense layer of 15 sigmoid neuron 
model.add(Dense(15,activation='sigmoid', input_dim=784))
#Add a dense layer of 10 sigmoid neuron 
model.add(Dense(10,activation='sigmoid'))

model.summary()

sgd = SGD(lr=0.3, decay=1e-6, momentum=0.9, nesterov=True) # ????
model.compile(optimizer=sgd,
              loss='mse',
              metrics=['accuracy'])

model.fit(train_x, train_y_Edited, epochs=40, batch_size=10) #???
#Remark
