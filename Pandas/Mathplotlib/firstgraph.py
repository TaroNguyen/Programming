# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:24:11 2017

@author: dito-maf
"""

import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(1960, 2015, 56) #create an equi-length array


# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()