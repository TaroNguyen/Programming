#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 19:48:09 2017

@author: dito-maf
"""


import gzip
import pickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# Use gzip to open a file
with gzip.open('../Data/HandWriting/mnist.pkl.gz', 'rb') as f:  # 'rb' ?????
    train_set, valid_set, test_set = pickle.load(f, encoding='latin1')

# Value in tuples cannot be changed and we use parentheses instead of brackets for tuples
with gzip.open('../Data/HandWriting/mnist.pkl.gz', 'rb') as f:  # 'rb' ?????
    s= pickle.load(f, encoding='latin1')
print( len(train_set[0]))

train_x, train_y = train_set

#Those would be the inputs (digits) and outputs (labels) of your sets.

#If you want to display the digits:



plt.imshow(train_x[0].reshape((28, 28)), cmap=cm.Greys_r)
#plt.savefig( 'FirstImage.png')
plt.show()