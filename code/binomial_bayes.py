#!/bin/python
#-----------------------------------------------------------------------------
# File Name : binomial_bayes.py
# Author: Emre Neftci
#
# Creation Date : Mon 13 May 2019 03:45:09 PM PDT
# Last Modified : 
#
# Copyright : (c) UC Regents, Emre Neftci
# Licence : GPLv2
#-----------------------------------------------------------------------------

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import scipy.special
import scipy.stats

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 15}

matplotlib.rc('font', **font)

def partfact(a,b):
    return np.prod(np.arange(a,b+1))

def binomial_posterior_uniform(r, n, k):
    return partfact(k+1,n+1)/partfact(1,n-k) *r**k * (1-r)**(n-k)

r = np.linspace(0,1,100)
plt.figure()
plt.plot(r, binomial_posterior_uniform(r,n=10,k=9))
plt.xlabel('r')
plt.ylabel('Posterior P(r|n,k)')
plt.savefig('../slides/img/binomial_bayes_posterior_uniform.png')


r = np.linspace(0,1,100)
plt.figure()
plt.plot(r, binomial_posterior_uniform(r,n=20,k=18), label = "subject 2")
plt.plot(r, binomial_posterior_uniform(r,n=10,k=9), label= "subject 1")
plt.xlabel('r')
plt.legend()
plt.axvline(0.9)
plt.ylabel('Posterior P(r|n,k)')
plt.savefig('../slides/img/binomial_bayes_posterior_uniform_subject12.png')

r = np.linspace(0,1,100)
plt.figure()
plt.plot(r, np.cumsum(binomial_posterior_uniform(r,n=20,k=18))*1./100, label = "subject 2")
plt.plot(r, np.cumsum(binomial_posterior_uniform(r,n=10,k=9))*1./100, label= "subject 1")
plt.xlabel('r')
plt.legend()
plt.axvline(0.9)
plt.ylabel('Posterior CDF(r|n,k)')
plt.savefig('../slides/img/binomial_bayes_cumposterior_uniform_subject12.png')



plt.figure()
beta = lambda r: scipy.stats.beta.pdf(r,4,4)
r = np.linspace(0,1,100)
plt.plot(r, beta(r))
plt.xlabel('r')
plt.ylabel('Prior P(r)')
plt.savefig('../slides/img/binomial_bayes_prior_beta.png')
plt.show()

plt.figure()

def binomial_posterior_beta(r, n, k):
    return scipy.stats.beta.pdf(r,4+k,4+n-k)
r = np.linspace(0,1,100)
plt.plot(r, binomial_posterior_uniform(r,n=10,k=9), label='Posterior with \n Uniform Prior')
plt.plot(r, binomial_posterior_beta(r, 10, 9), label='Posterior with \n Beta Prior')
plt.xlabel('r')
plt.xlabel('r')
plt.ylabel('Posterior P(r|n,k)')
plt.legend()
plt.savefig('../slides/img/binomial_bayes_posterior_beta.png')
plt.show()

