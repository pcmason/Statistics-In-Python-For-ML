#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 00:24:40 2022

@author: paulmason
"""
#Examples of different correlation methods

#Import numpy and pyplot
import numpy as np
import matplotlib.pyplot as plt

#Seed RNG
np.random.seed(1)

#First var is Gaussian dist with mean = 100 and std = 20
x = 20 * np.random.randn(1000) + 100

#Second var is first with Gaussian noise added with mean = 50 and std = 10
y = x + (10 * np.random.randn(1000) + 50)

#Summarize data
print('X: mean = %.3f, stdv = %.3f' % (np.mean(x), np.std(x)))
print('Y: mean = %.3f, stdv = %.3f' % (np.mean(y), np.std(y)))

#Plot x and y on a scatter plot
plt.scatter(x, y)
plt.show()

#Calculate and output covariance matrix
covariance = np.cov(x, y)
print(covariance)

#Import the method for the pearson correlation coefficient and method for spearman's correlation coef
from scipy.stats import pearsonr, spearmanr

#Get the pearson correlation coefficient for the data and output it
pcc, _ = pearsonr(x, y)
print('Pearson correlation coefficient: %.3f' % pcc)

#Get the spearman correlation coefficient for the data and output it
scc, _ = spearmanr(x, y)
print('Spearman correlation coefficient: %.3f' % scc)