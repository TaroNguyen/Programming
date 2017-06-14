#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 22:24:23 2017

@author: dito-maf
"""
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import time
y_pred = model.predict(test_set[0])


def predict( y):
    pos=0
    max=-1
    for i in range(len(y)):
        if (y[i]>max):
            max=y[i]
            pos=i
    return pos

i=0

for i in range(20) : 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow( test_set[0][i].reshape((28, 28)), cmap=cm.Greys_r,label='test')
    '''
    ax.annotate(str(predict(y_pred[i])), fontsize=20, xy=(.25, .75),
                xycoords='data', xytext=(150, -6),
                textcoords='offset points',color='white'
                )
    '''

    plt.show()
    
    print( 'Predicted Number : '+str(predict(y_pred[i])) )
    time.sleep(2)
