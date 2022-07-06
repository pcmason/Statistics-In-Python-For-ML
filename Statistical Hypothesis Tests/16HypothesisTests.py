#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 20:40:56 2022

@author: paulmason
"""
#Example of 16 different Hypothesis Tests in Python

#Normality Tests
#Create example dataset for normality tests
data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]

#1: Shapiro Wilk Test
from scipy.stats import shapiro
stat, p = shapiro(data)

#Output result of the test
print('Shaprio Wilk Test:')
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')


#2: D'Agostino's K^2 Test
from scipy.stats import normaltest
stat, p = normaltest(data)

#Output result of the test
print("D'Agostino's K^2 Test:")
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')
    
    
#3: Anderson-Darling Test
from scipy.stats import anderson
result = anderson(data)

#Output result of the test
print('Anderson-Darling Test:')
print('stat = %.3f' % (result.statistic))
for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < cv:
        print('Probably Gaussian at the %.1f%% level' % sl)
    else:
        print('Probably not Gaussian at the %.1f%% level' % sl)
        
        
        
#Correlation Tests
#Create extra dataset
data2 = [0.353, 3.517, 0.125, -7.545, -0.555, -1.536, 3.350, -1.578, -3.537, -1.579]

#4: Pearson's Correlation Test
from scipy.stats import pearsonr
stat, p = pearsonr(data, data2)

#Output result of the test
print("Pearson's Correlation Test:")
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably independent')
else:
    print('Probably dependent')
    
#5: Spearman's Rank Correlation
from scipy.stats import spearmanr
stat, p = spearmanr(data, data2)

#Output result of the test
print("Spearman's Rank Correlation:")
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably independent')
else:
    print('Probably dependent')

#6: Kendall's Rank Correlation
from scipy.stats import kendalltau
stat, p = kendalltau(data, data2)

#Output result of the test
print("Kendall's Rank Correlation:")
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably independent')
else:
    print('Probably dependent')
    
#7: Chi-Squared Test
from scipy.stats import chi2_contingency
table = [[10, 20, 30], [6, 9, 17]]
stat, p, dof, expected = chi2_contingency(table)

#Output result of the test
print('Chi-Squared Test:')
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably independent')
else:
    print('Probably dependent')
    
#Stationary Tests
#Data for stationary tests
data3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#8: Augmented Dickey-Fuller Unit Root Test
from statsmodels.tsa.stattools import adfuller
stat, p, lags, obs, crit, t = adfuller(data3)

#Output result of the test
print('Augmented Fuller-Dickey Unit Root Test:')
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably not stationary')
else:
    print('Probably stationary')
    
#9: Kwiatkowski-Phillips-Schmidt-Shin
from statsmodels.tsa.stattools import kpss
stat, p, lags, crit = kpss(data3)

#Output result of the test
print('Kwiatkowski-Phillips-Schmidt-Shin:')
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably stationary')
else:
    print('Probably not stationary')
    
#Parametric Tests
#Data for parametric tests, will also use data var above for most examples
data4 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]

#10: Student's T-Test
from scipy.stats import ttest_ind
stat, p = ttest_ind(data, data4)

#Output result of the test
print("Student's T-Test:")
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')

#11: Paired Student's T-Test
from scipy.stats import ttest_rel
stat, p = ttest_rel(data, data4)

#Output result of the test
print("Paired Student's T-Test:")
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
    
    
#12: Analysis of Variance Test (ANOVA)
from scipy.stats import f_oneway
#Add another dataset to show it workes with 2+ inputs
data5 = [-0.208, 0.696, 0.928, -1.148, -0.213, 0.229, 0.137, 0.269, -0.870, -1.204]
stat, p = f_oneway(data, data4, data5)

#Output result of the test
print('Analysis of Variance Test (ANOVA):')
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
    
    
#Nonparametric Tests
#13: Mann-Whitney U Test
from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(data, data4)

#Output result of the test
print('Mann-Whitney U Test:')
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
    

#14: Wilcoxon Signed-Rank Test
from scipy.stats import wilcoxon
stat, p = wilcoxon(data, data4)

#Output result of the test
print('Wilcoxon Signed-Rank Test:')
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
    
#15: Kruskal-Wallis H Test
from scipy.stats import kruskal
stat, p = kruskal(data, data4)

#Output result of the test
print('Kruskal-Wallis H Test:')
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
    
    
#16: Friedman Test
from scipy.stats import friedmanchisquare
stat, p = friedmanchisquare(data, data4, data5)

#Output result of the test
print('Friedman Test:')
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
    

    