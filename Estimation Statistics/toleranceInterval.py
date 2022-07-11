#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 22:15:48 2022

@author: paulmason
"""
#Worked example calculating tolerance interval on a Gaussian dataset

import numpy as np
import matplotlib.pyplot as plt
#Import scipy methods for calculating confidence and 95% values
from scipy.stats import chi2, norm

#Seed the RNG
np.random.seed(1)

#Create 100 samples for a Gaussian dataset with mean 50 and stdv 5
data = 5 * np.random.randn(100) + 50

#Specify degrees of freedom
n = len(data)
dof = n - 1

#Specify data coverage
prop = 0.95
prop_inv = (1 - prop) / 2
gauss_critical = norm.isf(prop_inv)
print('Gaussian critical value: %.3f (coverage = %d%%' % (gauss_critical, prop * 100))

#Specify confidence
prob = 0.99
chi_critical = chi2.isf(q = prob, df = dof)
print('Chi squared critical value: %.3f (prob = %d%%, dof = %d' % (chi_critical, prob * 100, dof))

#Calculate the Gaussian tolerance interval
interval = np.sqrt((dof * (1 + (1/n)) * gauss_critical**2) / chi_critical)
print('Tolerance interval: %.3f' % interval)

#Summarize
data_mean = np.mean(data)
lower, upper = data_mean - interval, data_mean + interval
print('%.2f to %.2f covers %d%% of data with a confidence of %d%%' % (lower, upper, prop * 100, prob * 100))

#Calculate tolerance intervals for different sample sizes for the same problem
sizes = range(5, 15)
for n in sizes:
    #Generate dataset
    data = 5 * np.random.randn(100) + 50
    #Calculate degrees of freedom
    dof = n - 1
    #Specify data coverage
    prop = 0.095
    prop_inv = (1 - prop) / 2
    gauss_critical = norm.isf(prop_inv)
    #Specify confidence
    prob = 0.99
    chi_critical = chi2.isf(q = prob, df = dof)
    #Tolerance
    tol = np.sqrt((dof * (1 + (1/n)) * gauss_critical**2) / chi_critical)
    plt.errorbar(n, 50, yerr = tol, color = 'blue', fmt = 'o')
    
#Plot results
plt.show()
