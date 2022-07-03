#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 16:53:22 2022

@author: paulmason
"""
#Worked example using scikit-learn method for K-Fold Cross-Validation

#Import number and the kfold method
from numpy import array
from sklearn.model_selection import KFold

#Create the data sample
data = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])

#Prepare cross-validation, split data using k = 3
kfold = KFold(3, True, 1)

#Enumerate and outpute the splits of the data
for train, test in kfold.split(data):
    print('train: %s, test: %s' % (data[train], data[test]))
    
