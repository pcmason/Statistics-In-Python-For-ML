#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 16:12:08 2022

@author: paulmason
"""
#Worked example using the scikit-learn bootstrap method

#Import the method from scikit-learn
from sklearn.utils import resample

#Create the data sample 
data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

#Prepare and output the bootstrap sample
boot = resample(data, replace = True, n_samples = 4, random_state = 1)
print('Bootstrap Sample: %s' % boot)

#Get and output the out of bag observations
oob = [x for x in data if x not in boot]
print('Out of Bag Observations: %s' % oob)