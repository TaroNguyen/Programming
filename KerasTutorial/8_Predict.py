#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 18:31:33 2017

@author: dito-maf
"""

y_pred = model.predict(X_test)
print( y_pred[:5])
print( y_test[:5])
score = model.evaluate( X_test, y_test, verbose=1)
print(score)