#!/bin/python
#-----------------------------------------------------------------------------
# File Name : do_plot.py
# Author: Emre Neftci
#
# Creation Date : Wed 24 Apr 2019 03:41:18 PM PDT
# Last Modified : 
#
# Copyright : (c) UC Regents, Emre Neftci
# Licence : GPLv2
#-----------------------------------------------------------------------------
import matplotlib
from matplotlib.pyplot import *
import numpy as np

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 15}

matplotlib.rc('font', **font)

import scipy.stats

figure(figsize=(6,4))
plot(np.linspace(-3,3), scipy.stats.norm.pdf(np.linspace(-3,3),loc=0,scale=1))
ylabel('Probability density')
xlabel('X')
title('N($\mu=0$,$\sigma=1$)')
tight_layout()
savefig('../slides/img/normal_0_1.png')


figure(figsize=(6,4))
q = np.arange(10)
step(q, scipy.stats.binom.pmf(q,n=10,p=.7))
ylabel('Probability Mass Function')
xlabel('Number of correct responses')
title('Bin(n=10,p=.7)')
tight_layout()
xticks([0,5,10])
savefig('../slides/img/binom_10_70.png')

figure(figsize=(6,4))
q = np.arange(0,60,1)
step(q, scipy.stats.binom.pmf(q,n=60,p=.87))
ylabel('Probability Mass Function')
xlabel('Number of correct responses')
y0 = scipy.stats.binom.pmf(50,n=60,p=.87)
plot([0,50],[y0,y0])
title('Bin(n=60,p=.87)')
tight_layout()
yticks([0,y0,.25])
xticks(range(0,60,10))
savefig('../slides/img/binom_60_87.png')

figure(figsize=(6,4))
q = np.arange(0,1000,1)
step(q, scipy.stats.binom.pmf(q,n=1000,p=.87))
ylabel('Probability Mass Function')
xlabel('Number of correct responses')
title('Bin(n=1000,p=.87)')
tight_layout()
savefig('../slides/img/binom_1000_87.png')

figure(figsize=(6,4))
samples = np.random.binomial(60,.87,100)
hist(samples, bins = range(0,60))
ylabel('Count')
xlabel('k')
yticks([0,25])
xticks(range(0,60,10))
title('Histogram for 100 samples $\sim$ Bin(n=60,p=.87)')
tight_layout()
savefig('../slides/img/binom_samples.png')

figure(figsize=(6,4))
q = np.arange(0,60,1)
step(q, scipy.stats.binom.pmf(q,n=60,p=.87))
ylabel('Probability Mass Function')
xlabel('k')
y0 = scipy.stats.binom.pmf(50,n=60,p=.87)
title('Bin(n=60,p=.87)')
tight_layout()
yticks([0,.25])
xticks(range(0,60,10))
savefig('../slides/img/binom_60_87_.png')


figure(figsize=(6,4))
plot(np.linspace(-3,3), scipy.stats.norm.pdf(np.linspace(-3,3),loc=0,scale=1))
x = np.linspace(-1,1)
fill_between(x, scipy.stats.norm.pdf(x,loc=0,scale=1), alpha=.5, color='b')
ylabel('Probability density')
xticks([-1,1],['a','b'])
xlabel('X')
title('N($\mu=0$,$\sigma=1$)')
text(-.5,.2,'P(a<X<b)=.68')
tight_layout()
savefig('../slides/img/normal_0_1_a_b.png')

figure(figsize=(6,4))
plot(np.linspace(-3,3), scipy.stats.norm.cdf(np.linspace(-3,3),loc=0,scale=1))
y0 = scipy.stats.norm.cdf(-1,loc=0,scale=1)
y1 = scipy.stats.norm.cdf(1,loc=0,scale=1)
plot([-3,-1],[y0, y0])
plot([-3,1],[y1, y1] )
ylabel('Cumulative Density Function')
xticks([-1,1],['a','b'])
yticks([0,y0,y1,1])
xlabel('X')
title('CDF($\mu=0$,$\sigma=1$)')
tight_layout()
savefig('../slides/img/normal_0_1_cdf.png')

figure(figsize=(6,4))
plot(np.linspace(-1,1), scipy.stats.norm.pdf(np.linspace(-1,1),loc=0,scale=.25))
ylabel('Probability density')
xlabel('Xt')
xlim([-1.1,1.1])
axvline(0)
title('N($\mu=0$,$\sigma=.25$)')
tight_layout()
savefig('../slides/img/normal_0_1_Xt.png')

figure(figsize=(6,4))
plot(np.linspace(-1,1), scipy.stats.norm.pdf(np.linspace(-1,1),loc=0.03,scale=.25))
ylabel('Probability density')
xlabel('Xt')
xlim([-1.1,1.1])
axvline(0)
title('N($\mu=0.03$,$\sigma=.25$)')
tight_layout()
savefig('../slides/img/normal_0_03_1_Xt.png')

