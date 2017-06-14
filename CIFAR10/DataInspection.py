# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import gzip
import pickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd


# Use gzip to open a file
with open('../Data/CIFAR-10/data_batch_1', 'rb') as f:  # 'rb' ?????
    data = pickle.load(f, encoding='latin1')

a,b,c,d= data;
#df= pd.DataFrame.from_dict( data , orient='columns')