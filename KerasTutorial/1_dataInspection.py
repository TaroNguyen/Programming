# -*- coding: utf-8 -*-
"""
Created on Tue May 23 23:26:22 2017

@author: dito-maf
"""

# Load data
import pandas as pd
white = pd.read_csv("../Data/Wine/winequality-white.csv",sep=";")
red = pd.read_csv("../Data/Wine/winequality-red.csv",sep=";")
print(white.describe())
white.info()