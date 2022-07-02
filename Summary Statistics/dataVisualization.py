#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 23:28:19 2022

@author: paulmason
"""
#Code of multiple different methods of data visualizations using matplotlib

#Import pyplot
import matplotlib.pyplot as plt

#Example of a sin line plot
from numpy import sin

#Consistent intervals for x-axis
x = [x * 0.1 for x in range(100)]

#Function of x for y-axis
y = sin(x)

#Create line plot
plt.plot(x, y)

#Show plot
plt.show()

#Example of a bar chart with 3 categories
#Import necessary methods
from random import seed, randint

#Seed the RNG
seed(1)

#Names for categories
x = ['red', 'blue', 'green']

#Quantities for each category
y = [randint(0, 100), randint(0, 100), randint(0, 100)]

#Create bar chart
plt.bar(x, y)

#Show chart
plt.show()

#Example of histogram plot using 1000 random numbers from a standard Gaussian dist
#Import method for Gaussian dist
from numpy.random import randn, seed

#Seed the RNG
seed(1)

#Random numbers drawn from a Gaussian dist
x = randn(1000)

#Create histogram plot
plt.hist(x)

#Show plot
plt.show()

#Example of a box and whisker plot
#Seed the RNG
seed(1)

#Random numbers drawn from a Gaussian dist
x = [randn(1000), 5 * randn(1000), 10 * randn(1000)]

#Create the box and whisker plot
plt.boxplot(x)

#Show plot
plt.show()

#Example of a scatter plot
#Seed RNG
seed(1)

#First var
x = 20 * randn(1000) + 100

#Second var
y = x + (10 * randn(1000) + 50)

#Create scatter plot
plt.scatter(x, y)

#Show plot
plt.show()

