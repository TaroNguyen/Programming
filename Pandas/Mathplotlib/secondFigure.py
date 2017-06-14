# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:40:05 2017

@author: dito-maf
"""

import matplotlib.pyplot as plt

# Initialize the plot
x = np.linspace(0, 10, 100) 
y= np.linspace(0, 10, 100) 
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Plot the data
ax.scatter(x,y)
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax1.axvline(0.65)

# Show the plot

# Save Figure
plt.savefig("foo.png")
plt.show()
# Save Transparent Figure