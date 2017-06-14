#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:23:44 2017

@author: dito-maf
"""

import pandas as pd

reviews = pd.read_csv("../Data/AmazonBookReviews/Donna-Tartt-The-Goldfinch.csv",sep="\t")
print(reviews.describe())