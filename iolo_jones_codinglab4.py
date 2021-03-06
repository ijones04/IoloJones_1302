# -*- coding: utf-8 -*-
"""Iolo_Jones_CodingLab4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qC-QVHvvFIn0lLNEL2xJ4yu-p-4o1V7o

Coding Lab 4 - Iolo Jones

Q1. Use matplotlib to draw a same plot as Q1.jpg (attached). Requirements:

1. (20%) plot two curves: 2sin(x) in solid line and 2cos(x) in dotted line
2. (10%) plot three periods for each function as shown in Q1.jpg
3. (10%) plot legend, axis labels (font size is 15), and grid (color is blue, alpha=0.2)
4. (10%) the range of y-axis is [-4, 4]
5. (10%) color: use red when the function is increasing and use green when it is decreasing
"""

import matplotlib.pyplot as pplot
import numpy as np

size = 200 # set size of x and y arrays to 200 to give smooth lines
x1 = np.linspace(-3*np.pi+(np.pi / 2), 3*np.pi+(np.pi / 2), size) # create a numpy array in the range [-3*pi + (pi/2), 3*pi + (pi/2)]
x2 = np.linspace(-3*np.pi, 3*np.pi, size) # create a numpy array in the range [-3*pi, 3*pi]
y1 = 2 * np.sin(x1) # set up the one line
y2 = 2 * np.cos(x2) # set up the other line

def plot(x, y, label, marker="-"): # create a method that gives red increasing and green decreasing lines
    i = 1 # initialise i
    while i < len(x): # iterate through the length of array
        ylst = [y[i-1]] # first y point to plot
        xlst = [x[i-1]] # first x point to plot
        if y[i] > y[i-1]: # if INCREASING
            while i < len(y) and y[i] > y[i-1]: # add the elements to the increasing list if increasing (until no longer increasing)
                ylst.append(y[i]) # append
                xlst.append(x[i]) # append
                i += 1 # increment i by 1
            colour = "red" # when increasing colour is red
        else: # if NOT INCREASING
            while i < len(y) and y[i] <= y[i-1]: # add the elements to the decreasing list if increasing (until no longer decreasing)
                ylst.append(y[i]) # append
                xlst.append(x[i]) # append
                i += 1 # increment i by 1
            colour = "green" # colour when decreasing is green
        if i == len(x-1): # last element 
            pplot.plot(xlst, ylst, marker, color = colour, label = label) # define label to avoid multiple legends
        else:
            pplot.plot(xlst, ylst, marker, color = colour) # everything before last element

plot(x1, y1, label="2sin(x)", marker = "-") # plot the first line
plot(x2, y2, label="2cos(x)", marker = "--") # plot the second line with dotted line to differentiate
pplot.xlabel('X', fontsize = 15) # label x axis
pplot.ylabel('Y', fontsize = 15) # label y axis
pplot.ylim(-4, 4) # set the range of the y axis to -4 and 4
pplot.grid(color="blue", alpha = 0.1) # plot the grid that the lines are graphed on
pplot.legend() # legend to show which line is which

"""Q2. Consider following code:

X = np.random.rand(1000) * 100
Y = np.random.normal(50, 10, 1000)
1. (10%) Explain the meaning of the code. You may refer to the numpy documentation.
2. (10%) Calculate the mean and standard deviation of X and Y.
3. (10%) Plot the histograms of X and Y. Each histrogram should have 20 bins. Set appropriate alpha to make the overlapped area visible.
4. (10%) Describe the shape of each histogram.
"""

import matplotlib.pyplot as pplot
import numpy as np

X = np.random.rand(1000) * 100 # define X
Y = np.random.normal(50, 10, 1000) # define Y
# np.random.rand(1000) generates an array of a length of 1000 and populates it with elements from a random sample from a uniform distribution on [0, 1)
# X is however 100 * each element, so X is an array of length 1000 with elements from from a random sample from a uniform distribution on [0, 100)
# Y = np.random.normal(50,10,1000) creates an array taken from random sample from normal distribution for mean 50, standard deviation 10 and size of 100

X_mean = X.mean() # mean of X
X_std = X.std() # st dev of X
Y_mean = Y.mean() # mean of Y
Y_std = Y.std() # st dev of Y

pplot.hist(X, bins = 20, edgecolor='black', alpha = 0.5, label = 'X') # plot histogram for X
pplot.hist(Y, bins = 20, edgecolor='black', alpha = 0.5, label = 'Y') # plot histogram for Y
pplot.legend() # add the legend
pplot.show() # show figure

# Histogram of X is uniform 'consistently sized' rectangle (uniform distribution), Histogram of Y is bell-shaped with centred mean, no skew (normal distribution).