#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 20:24:39 2017

@author: dito-maf
"""

from keras.models import Sequential

# Import `Dense` from `keras.layers`
from keras.layers import Dense
import gzip
import pickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# Use gzip to open a file
with gzip.open('../Data/HandWriting/mnist.pkl.gz', 'rb') as f:  # 'rb' ?????
    train_set, valid_set, test_set = pickle.load(f, encoding='latin1')

# Value in tuples cannot be changed and we use parentheses instead of brackets for tuples

print( len(train_set[0]))

train_x, train_y = train_set
# Initialize the constructor
model = Sequential()

#Add a dense layer of 15 sigmoid neuron 
model.add(Dense(15,activation='sigmoid', input_dim=784),)
#Add a dense layer of 10 sigmoid neuron 
model.add(Dense(10,activation='sigmoid'))

model.summary()
