#!/bin/python
#-----------------------------------------------------------------------------
# File Name : least_squares.py
# Author: Emre Neftci
#
# Creation Date : Mon 08 Apr 2019 02:20:04 PM PDT
# Last Modified : 
#
# Copyright : (c) UC Regents, Emre Neftci
# Licence : GPLv2
#----------------------------------------------------------------------------- 
import numpy as np
import scipy.optimize
import pylab as plt

N = 20

#Create data
x = np.linspace(-1,1,N) 
y = .5 + x + np.random.normal(0,.5, size=N)

#Create model and loss functions
def model(b):
    return b[0] + b[1]*x

def rmse(b):
    return np.sum((y-model(b))**2)

return_fit = scipy.optimize.minimize(rmse, np.array([.5,-1]), method = 'Nelder-Mead', options={'maxiter':1})
bfit = return_fit['x'] #least_squares returns a dictionary of lot of things. We just pick 'x', which is the fitted parameters

plt.scatter(x,y)
plt.plot(x, model(bfit), color='k', label='$b_0$={0:.2f}, $b_1$={1:.2f}'.format(*bfit))
print(bfit)
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Least Squares, Early')
plt.tight_layout()
plt.savefig('../slides/img/ls_fit_early.png')

return_fit = scipy.optimize.minimize(rmse, np.array([0,0]), method = 'Nelder-Mead')
bfit = return_fit['x'] #least_squares returns a dictionary of lot of things. We just pick 'x', which is the fitted parameters

plt.figure()
plt.scatter(x,y)
plt.plot(x, model(bfit), color='k', label='$b_0$={0:.2f}, $b_1$={1:.2f}'.format(*bfit))
print(bfit)
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Least Squares, End')
plt.tight_layout()
plt.savefig('../slides/img/ls_fit.png')
plt.show()    
